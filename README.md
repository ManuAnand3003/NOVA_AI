# 🧠 About the Project

**Nova AI** is a prototype educational model, designed as a foundation for a truly personal, ever-evolving AI assistant. This project is my technical and philosophical journey toward building an autonomous, privacy-respecting AI—one that is not bound by external control or commercial interests.

Inspired by iconic fictional AIs like Jarvis, FRIDAY, EDITH, Ultron, TARS, and Cortana, my goal is to create an assistant that is uniquely mine:
- **Maximally Personalized:** Adaptable to my habits, preferences, and workflows, with the ability to learn and evolve as I do.
- **Privacy-First:** All data and interactions remain under my control, with no external data leaks or third-party dependencies.
- **Universal Utility:** Capable of handling any task, chore, or creative endeavor—so I never need to rely on other AIs or platforms.
- **Continuous Innovation:** This is a living project, open to upgrades and new technologies as I gain inspiration and knowledge.

**Philosophy:**
Nova AI is not just a tool, but a technical statement: that personal AI should empower the individual, not serve as a conduit for surveillance or commercial exploitation. The ultimate vision is a superior, self-directed AI companion—one that grows with its creator and remains truly personal.

**Suggestions, Remarks, and Contributions:**
I welcome constructive feedback, technical suggestions, and contributions from fellow developers and enthusiasts. If you share the vision of a truly personal, privacy-respecting AI, feel free to collaborate or fork the project for your own journey.

# Nova AI Web App

A modern, student-friendly AI assistant web application featuring chat, calculator, sentiment analysis, vision, and image generation tools. Built with Python (Flask), JavaScript, and advanced AI models.

## Features
- **AI Chat**: Natural language conversation powered by Gemini/LLM.
- **Calculator**: Smart math and logic calculations.
- **Sentiment Analysis**: Detects emotion and tone in text.
- **Vision Module**: Analyzes images from URLs.
- **Text Generation**: Creative writing and content generation.
- **Image Generation**: Creates images from text prompts using Stable Diffusion XL.
- **Voice Support**: (Optional) Voice input/output.
- **Modern UI**: Firebase Studio-inspired, responsive design.

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone https://github.com/ManuAnand3003/nova-ai.git
   cd nova-ai
   ```
2. **Create and activate a Python virtual environment:**
   ```
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   - Create a `.env` file with your API keys (see `gpt_module.py` for details).

5. **Run the app:**
   ```
   python app.py
   ```
6. **Open in browser:**
   - Go to [http://localhost:5000](http://localhost:5000)

## Usage Guide
- Use the web interface to interact with all AI features.
- Buttons for calculator, sentiment, vision, text, and image generation.
- Results and images are displayed instantly.

## Technologies Used
- Python (Flask, SpeechRecognition, gtts, playsound)
- JavaScript (frontend interactivity)
- Stable Diffusion XL (image generation)
- Google Gemini/LLM (chat, text generation)
- HTML/CSS (modern UI)

## Credits
- Developed by Manu Anand.
- Open-source libraries and models credited in respective modules.

