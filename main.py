import requests
import argparse
import os
from dotenv import load_dotenv

# --- Load API Key from .env ---
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("❌ Error: OPENROUTER_API_KEY not found in .env")
    exit(1)

# --- Command-line Prompt ---
parser = argparse.ArgumentParser(description="Ask OpenRouter AI something.")
parser.add_argument("prompt", nargs="+", help="Your prompt to the AI model")
args = parser.parse_args()
user_prompt = " ".join(args.prompt)

# --- API Setup ---
headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "http://localhost",  # or your actual domain
    "X-Title": "cli-openrouter"
}

data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [{"role": "user", "content": user_prompt}]
}

# --- Make Request ---
response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

# --- Output Response ---
if response.status_code == 200:
    print("AI:", response.json()["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)

# you will run "uv run main.py "your prompt here"" on command line to run the script
