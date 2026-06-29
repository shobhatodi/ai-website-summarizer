import os
from google import genai
from google.genai import types  # Required for setting system prompts
from dotenv import load_dotenv
from scraper import fetch_website_contents

load_dotenv()  # Reads GEMINI_API_KEY from your .env file

# Initialize the official Google GenAI client
# It will automatically pick up GEMINI_API_KEY from your environment variable
client = genai.Client()

system_prompt = """You analyze the contents of a website and
give a short, friendly summary. Ignore navigation menus.
Respond in markdown."""

def summarize(url):
    website = fetch_website_contents(url)
    
    # Correct native Gemini syntax with system instruction configuration
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"Summarize this website:\n\n{website}",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
        ),
    )
    
    # Extract response text directly using .text
    return response.text