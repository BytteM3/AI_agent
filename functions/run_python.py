import os
import subprocess

def run_python_file(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if full_path.startswith(os.path.abspath(working_directory)):
        pass
    else:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if os.path.exists(full_path) != True:
        return f'Error: File "{file_path}" not found.'
    elif not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    args_list = ["python3", full_path]
    
    try:
        result = subprocess.run(args_list, cwd=os.path.abspath(working_directory), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    return_string = ""
    stdout_string = f'STDOUT: "{result.stdout.decode('utf-8')}"'
    stderr_string = f'\nSTDERR:"{result.stderr.decode('utf-8')}"'
    if result.stdout:
        return_string += stdout_string
    if result.stderr:
        return_string += stderr_string
    if result.returncode != 0:
        return_string += f'\nProcess exited with code "{result.returncode}"'
    if not return_string:
        return_string = "No output produced."
    return return_string