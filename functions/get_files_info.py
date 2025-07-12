import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    if os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        pass
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isdir(os.path.abspath(full_path)) == False:
        return f'Error: "{directory}" is not a directory'
    
    results_list = []

    try:
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            result = f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            results_list.append(result)
    except Exception as e:
        return f"Error: {e}"

    return "\n".join(results_list)