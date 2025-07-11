import os
from .config import *

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    if os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        pass
    else:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isfile(os.path.abspath(full_path)) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(os.path.abspath(full_path), "r") as f:
            file_content_string = f.read(CHAR_LIMIT)
            remaining_chars = f.read(1)
            if remaining_chars:
                return f'{file_content_string}[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"