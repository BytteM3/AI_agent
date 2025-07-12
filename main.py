import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")



client = genai.Client(api_key=api_key)

system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

def main():
    if len(sys.argv) < 2:
        print("Please provide input!")
        sys.exit(1)
    
    else:
        messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])])
    ]
        result = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=messages)
    
    prompt_tokens = result.usage_metadata.prompt_token_count
    response_tokens = result.usage_metadata.candidates_token_count

    if "--verbose" in sys.argv:
        print(f"User prompt: {sys.argv[1]}")
        print(result.text)
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    else:
        print(result.text)

if __name__ == "__main__":
    main()
