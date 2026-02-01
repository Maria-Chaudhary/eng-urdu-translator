import os
import re
import gradio as gr
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.environ.get("translator"))

MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.02
MAX_TOKENS = 800


# --- Helper functions ---

# Protect English words (strike, AI, names, etc.)
def protect_english(text):
    words = re.findall(r"[A-Za-z]+", text)
    mapping = {w: f"<<{w}>>" for w in words}
    safe_text = text
    for w, p in mapping.items():
        safe_text = safe_text.replace(w, p)
    return safe_text, mapping

def restore_english(text, mapping):
    for w, p in mapping.items():
        text = text.replace(p, w)
    return text

# Remove unwanted foreign/Cyrillic characters
def clean_text(text):
    # Keep English letters, Urdu letters, numbers, and basic punctuation
    return re.sub(r"[^a-zA-Z0-9\u0600-\u06FF\s,.!?']", " ", text).strip()


# --- Translation functions ---

def eng_to_urdu(text):
    if not text.strip():
        return ""

    text = clean_text(text)          # remove foreign characters
    safe_text, mapping = protect_english(text)

    prompt = f"""
You are an expert professional translator.

Rules (must follow strictly):
- Translate ONLY into natural, fluent Urdu.
- Preserve meaning exactly.
- Do NOT transliterate foreign or non-English characters.
- Keep English words if no proper Urdu equivalent.
- Keep proper nouns in English.
- Keep numbers unchanged.
- Correct grammar, punctuation, and word order.

English:
{safe_text}

Urdu:
"""

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    result = completion.choices[0].message.content.strip()
    result = restore_english(result, mapping)
    result = result.replace('"', '').replace("  ", " ").strip()
    return result


def urdu_to_eng(text):
    if not text.strip():
        return ""

    text = clean_text(text)  # remove foreign characters

    prompt = f"""
You are an expert professional translator.

Rules (must follow strictly):
- Translate ONLY into clear, natural English.
- Preserve meaning exactly.
- Keep English words unchanged.
- Keep proper nouns unchanged.
- Keep numbers unchanged.
- Correct grammar, punctuation, and word order.

Urdu:
{text}

English:
"""

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    result = completion.choices[0].message.content.strip()
    result = result.replace('"', '').replace("  ", " ").strip()
    return result


# --- Gradio UI ---
with gr.Blocks() as demo:

    gr.Markdown("""
    # 🌍 AI Language Translator
    ### English ⇄ Urdu (Powered by Groq LLaMA 3.3)
    Fast, accurate, and professional bilingual translation.
    """)

    # English → Urdu
    gr.Markdown("## 🇬🇧 English → 🇵🇰 Urdu")
    eng_input = gr.Textbox(label="Enter English Text", placeholder="Type English here...", lines=4)
    urdu_output = gr.Textbox(label="Urdu Translation", lines=4)
    eng_btn = gr.Button("Translate to Urdu")
    eng_btn.click(fn=eng_to_urdu, inputs=eng_input, outputs=urdu_output)

    gr.Markdown("---")

    # Urdu → English
    gr.Markdown("## 🇵🇰 Urdu → 🇬🇧 English")
    urdu_input = gr.Textbox(label="اردو متن درج کریں", placeholder="یہاں اردو لکھیں...", lines=4)
    eng_output = gr.Textbox(label="English Translation", lines=4)
    urdu_btn = gr.Button("Translate to English")
    urdu_btn.click(fn=urdu_to_eng, inputs=urdu_input, outputs=eng_output)

    gr.Markdown("""
    ---
    🚀 Built with Gradio + Groq API  
    Professional, portfolio-ready bilingual translation.
    """)

demo.launch(theme=gr.themes.Soft())
