import os

def write_file(working_directory: str, file: str, content: str) -> str:
    # working_directory - where the LLM is supposed to be doing it's work
    # file - file that is supposed to be inside the working directory
    working_dir_abs_path = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs_path, file))
    common_path = os.path.commonpath([working_dir_abs_path, target_file])

    # path validation 
    if common_path != working_dir_abs_path:
        return f'Error: Cannot write "{file}", as it is outside permitted working directory ({working_dir_abs_path})'
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file}", as it is a directory'

    try:
        # os.path.dirname(target_file) - extracts the directory in which the target file should be placed
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)
    except Exception as err:
        return f"Error: {err}"

    return f'Successfully wrote to "{target_file}" ({len(content)} characters written)'

from google.genai import types
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            # working_directory: str, file: str, content: str
            "file": types.Schema(
                type=types.Type.STRING,
                description="File to be written in/created",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written to the given file",
            ),
        },
    ),
)
