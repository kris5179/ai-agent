from functions.get_file_content import get_file_content

folder = "calculator"
files = ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

for example in files:
    print(f"Result for '{example}'")
    result = get_file_content(folder, example)
    print(result)

