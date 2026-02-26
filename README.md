# 🌍 AI Translator & Text-to-Image Generator

An AI-powered web application that provides **high-accuracy English ⇄ Urdu translation** and **text-to-image generation** using **Groq LLaMA 3.3** and **Stable Diffusion**, built with **Gradio** and deployed on **Hugging Face Spaces**.

---

## 🚀 Features

### 🔤 Language Translation
- **English → Urdu** (natural, fluent, context-aware)
- **Urdu → English** (clear, professional translation)
- Preserves:
  - Proper nouns
  - English technical words
  - Numbers and formatting
- Avoids literal word-by-word translation

### 🖼️ Text-to-Image Generation
- Generate high-quality images from text prompts
- Powered by **Stable Diffusion v1.5**
- Optimized to avoid scheduler and timestep errors
- Fast and reliable image generation

### 🎨 User Interface
- Clean, professional Gradio UI
- Separate sections for translation and image generation
- Portfolio-ready design

---

## 🛠️ Tech Stack

- **Frontend/UI:** Gradio  
- **LLM API:** Groq (LLaMA-3.3-70B-Versatile)  
- **Image Generation:** Stable Diffusion v1.5  
- **Frameworks:** Diffusers, PyTorch  
- **Deployment:** Hugging Face Spaces  

---

## 📂 Project Structure

```text
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
```
⚙️ Installation (Local / Google Colab)
1️⃣ Clone Repository
```bash
git clone https://github.com/Maria-Chaudhary/eng-urdu-translator.git
cd eng-urdu-translator
```
2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
3️⃣ Set Groq API Key
```bash
export translator=YOUR_GROQ_API_KEY
```

Windows (PowerShell):
```bash
setx translator "YOUR_GROQ_API_KEY"
```
4️⃣ Run Application
```bash
python app.py
```
### 🔴 Live Demo  
https://huggingface.co/spaces/Mariaaa123/eng-to-urdu
