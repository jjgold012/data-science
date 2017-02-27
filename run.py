files_to_run = [r"drop_tables.py", r"remove_db.py", r"create_db.py", r"create_tables.py"]

for file in files_to_run:
    execfile(file)
