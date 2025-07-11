import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import schema_get_files_info

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")



client = genai.Client(api_key=api_key)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

def main():
    if len(sys.argv) < 2:
        print("Please provide input!")
        sys.exit(1)
    
    else:
        messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])])
    ]
        result = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
    
    prompt_tokens = result.usage_metadata.prompt_token_count
    response_tokens = result.usage_metadata.candidates_token_count

    if "--verbose" in sys.argv:
        print(f"User prompt: {sys.argv[1]}")
        print(result.text)
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    else:
        if result.function_calls:
            print(f"Calling function: {result.function_calls[0].name}({result.function_calls[0].args})")
            if result.text:
                print(result.text)
        else:
            print(result.text)

if __name__ == "__main__":
    main()
