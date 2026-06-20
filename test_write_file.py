from functions.write_file import write_file
working_directory = "calculator"
contents = ["wait, this isn't lorem ipsum", "lorem ipsum dolor sit amet", "this should not be allowed"]
files = ["lorem.txt", "pkg/morelorem.txt", "/tmp/temp.txt"]

for file, content in zip(files, contents):
    print(write_file(working_directory, file, content))
