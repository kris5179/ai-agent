import os

def get_files_info(working_directory: str, directory: str = ".") -> str: 
    # working_directory - where the LLM is supposed to be doing it's work
    # directory - directory INSIDE the working_directory
    working_dir_abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs_path, directory))
    common_path = os.path.commonpath([working_dir_abs_path, target_dir])

    # path validation 
    if common_path != working_dir_abs_path:
        return f'Error: Cannot list "{directory}", as it is outside permitted working directory ({working_dir_abs_path})'
    if not os.path.isdir(target_dir):
        return f'Error: {directory} is not a directory'

    # if directory is ok 
    subdirs = os.listdir(target_dir)
    results = []
    for subdir in subdirs:
        abs_file = os.path.normpath(os.path.join(target_dir, subdir))
        file_size = os.path.getsize(abs_file)
        is_dir = os.path.isdir(abs_file)
        results.append(f"- {subdir}, file_size={file_size} bytes, is_dir={is_dir}")
    return "\n".join(results) 

from google.genai import types
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

