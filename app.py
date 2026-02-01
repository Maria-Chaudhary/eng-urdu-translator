import os
import gradio as gr
from groq import Groq

# Groq client (API key will come from HF Secrets)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def translate(text):
    if not text.strip():
        return ""

    prompt = f"Translate the following English text into Urdu:\n\n{text}"

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=500,
    )

    return completion.choices[0].message.content


with gr.Blocks() as demo:
    gr.Markdown("# 🌐 English → Urdu Translator (Groq + Gradio)")

    inp = gr.Textbox(label="Enter English Text", lines=5)
    out = gr.Textbox(label="Urdu Translation", lines=5)

    btn = gr.Button("Translate")

    btn.click(fn=translate, inputs=inp, outputs=out)

demo.launch()
