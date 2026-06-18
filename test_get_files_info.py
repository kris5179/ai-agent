from functions.get_files_info import get_files_info

file = "calculator"
paths = [".", "pkg", "/bin", "../"]

for path in paths:
    if path == ".":
        print(f"Result for current directory: ")
    else:
        print(f"Result for '{path}' directory:")
    print(f"{get_files_info(file, path)}")
    print()
