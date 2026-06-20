import os

def get_file_content(working_directory: str, file: str) -> str:
    MAX_CHARS = 10000
    # working_directory - where the LLM is supposed to be doing its work
    # file - file that is supposed to be inside the working directory
    working_dir_abs_path = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs_path, file))
    common_path = os.path.commonpath([working_dir_abs_path, target_file])

    # path validation 
    if common_path != working_dir_abs_path:
        return f'Error: Cannot read "{file}", as it is outside permitted working directory ({working_dir_abs_path})'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file {file}'

    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1): 
                file_content_string += f'[...File "{target_file}" truncated at {MAX_CHARS} characters]'

    except Exception as err:
        return f"Error: {err}"

    return file_content_string
