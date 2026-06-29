# AI Website Summarizer 🚀

An AI-powered web application that takes any website URL, fetches its content, and generates a concise, intelligent summary in seconds. Built using Google's Gemini LLM and Gradio.

## 🌟 Features
- **Instant Summarization**: Extracts core insights from lengthy web articles instantly.
- **Powered by Gemini**: Uses Google's state-of-the-art Generative AI for high-quality text understanding.
- **User-Friendly Interface**: Clean and interactive UI built entirely with Gradio.

## 🛠️ Tech Stack
- **Language:** Python
- **LLM:** Google Gemini API (`google-generativeai`)
- **UI Framework:** Gradio
- **Web Scraping:** BeautifulSoup4 / Requests

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd ai-website-summarizer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API Key (Create a `.env` file):
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. Run the app:
   ```bash
   python app.py
   ```