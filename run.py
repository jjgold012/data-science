import os

files_to_run = ["drop_tables.py", "remove_db.py", "create_db.py", "create_tables.py"]

data_files = ["australian football/run_australian_football.py", "basketball/run_basketball.py", "cricket/run_cricket.py",
              "football/run_football.py", "hockey/run_hockey.py", "rugby/run_rugby.py", "soccer/run_soccer.py",
              "tennis/run_tennis.py"]

for file in files_to_run:
    execfile(file)

for file in data_files:
    f = file.split('/')
    os.chdir(f[0])
    execfile(f[1])
    os.chdir("..")

