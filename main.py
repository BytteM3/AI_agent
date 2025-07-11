import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")



client = genai.Client(api_key=api_key)



def main():
    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])])
    ]

    if len(sys.argv) < 2:
        print("Please provide input!")
        sys.exit(1)
    
    else:
        result = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=messages)
    
    
    prompt_tokens = result.usage_metadata.prompt_token_count
    response_tokens = result.usage_metadata.candidates_token_count
    print(result.text)
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")

if __name__ == "__main__":
    main()
