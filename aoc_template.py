
from rich import print
from rich import traceback

# load the rich stuff
traceback.install()

file_name = "test.txt"


with open(file_name) as text:
    for line in text:
        data = line.strip().split('\n')
