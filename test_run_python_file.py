from functions.run_python_file import run_python_file
working_directory = "calculator"
file_paths = ["main.py", "main.py", "tests.py", "../main.py", "nonexistent.py", "lorem.txt"]
args = [None,["3 + 5"],None,None,None,None,]

for file, argument in zip(file_paths, args):
    print(run_python_file(working_directory, file, argument))
