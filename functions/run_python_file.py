import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    # working_directory - where the LLM is supposed to be doing it's work
    # file_path - file that is supposed to be inside the working directory
    working_dir_abs_path = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs_path, file_path))
    common_path = os.path.commonpath([working_dir_abs_path, target_file])

    # path validation 
    if common_path != working_dir_abs_path:
        return f'Error: Cannot execute "{file_path}" as it is outside permitted working directory ({working_dir_abs_path})'
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    try:
        command = ["python3", target_file]
        if args:
            command.extend(args)
            print(command)
        process = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if process.returncode != 0:
            return f"Process exited with code {process.returncode}"
        if not process.stdout and not process.stderr:
            return "No output produced"
        else:
            return f"STDOUT: {process.stdout} \nSTDERR: {process.stderr}"
    except Exception as err_msg:
        return f"Error: executing python file: {err_msg}"

            

