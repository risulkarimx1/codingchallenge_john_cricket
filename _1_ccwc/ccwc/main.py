import os.path
import sys

arguments = sys.argv[1:]

for arg in arguments:
    if arg.startswith("-"):
        command: str = arg
    else:
        fileName: str = arg

print("command: ", command)
print("filename: ", fileName)

if os.path.isfile(fileName):
    print("exists")
else:
    print("doesn't")


def get_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None


def get_bytes():
        text = get_file(fileName)
        count = 0
        for c in text:
            count += 1
        print(count)


if command == '-c':
    get_bytes()
else:
    print("command not known")
