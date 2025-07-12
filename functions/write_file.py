import os
def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    if os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        pass
    else:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(os.path.abspath(full_path)), exist_ok=True)
    except Exception as e:
        return f'Error: {e}'
    
    try:
        with open(os.path.abspath(full_path), "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
    
