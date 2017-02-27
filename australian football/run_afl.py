import os

files_to_run = [r"afl.py"]

for file in files_to_run:
    file_path = os.path.abspath(file) if "australian football" in os.path.abspath(file) else\
        os.path.abspath(file)[:-6] + "/australian football" + '/' + file
    execfile(file_path)
