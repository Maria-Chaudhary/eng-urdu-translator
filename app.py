import os
import gradio as gr
from groq import Groq

# Initialize Groq Client (HF Secret name: translator)
client = Groq(api_key=os.environ.get("translator"))

MODEL = "llama-3.3-70b-versatile"


def eng_to_urdu(text):
    if not text.strip():
        return ""

    prompt = f"""
You are a professional translator.

Translate the following English text into natural, fluent Urdu.

English:
{text}

Urdu:
"""

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500,
    )

    return completion.choices[0].message.content.strip()


def urdu_to_eng(text):
    if not text.strip():
        return ""

    prompt = f"""
You are a professional translator.

Translate the following Urdu text into natural, fluent English.

Urdu:
{text}

English:
"""

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500,
    )

    return completion.choices[0].message.content.strip()


with gr.Blocks() as demo:

    gr.Markdown("""
    # 🌍 AI Language Translator  
    ### English ⇄ Urdu (Powered by Groq LLaMA 3.3)
    """)

    gr.Markdown("## 🇬🇧 English → 🇵🇰 Urdu")

    eng_input = gr.Textbox(label="Enter English Text", lines=4)
    urdu_output = gr.Textbox(label="Urdu Translation", lines=4)
    eng_btn = gr.Button("Translate to Urdu")

    eng_btn.click(fn=eng_to_urdu, inputs=eng_input, outputs=urdu_output)

    gr.Markdown("---")

    gr.Markdown("## 🇵🇰 Urdu → 🇬🇧 English")

    urdu_input = gr.Textbox(label="اردو متن درج کریں", lines=4)
    eng_output = gr.Textbox(label="English Translation", lines=4)
    urdu_btn = gr.Button("Translate to English")

    urdu_btn.click(fn=urdu_to_eng, inputs=urdu_input, outputs=eng_output)

    gr.Markdown("""
    ---
    🚀 Built with Gradio + Groq API  
    Fast, accurate bilingual translation.
    """)

demo.launch(theme=gr.themes.Soft())
