files_to_run = [r"drop_tables.py", r"remove_db.py", r"create_db.py", r"create_tables.py"]

data_files = [r"australian football/run_afl.py", r"basketball/run_basketball.py", r"cricket/run_cricket.py",
              r"football/run_football.py", r"hockey/run_hockey.py", r"rugby/run_rugby.py", r"soccer/run_soccer.py",
              r"tennis/run_tennis.py"]

for file in files_to_run:
    execfile(file)

for file in data_files:
    execfile(file)
