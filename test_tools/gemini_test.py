import google.generativeai as genai
import os

PROMPT = "What is the Australian attack in the King's Indian Defense"

if __name__ == "__main__":
    api_key = os.environ["GOOGLE_API_KEY"]
    # print(api_key)
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(PROMPT)
    print(response.text)
