files_to_run = [r"soccer1.py", r"countries.py"]

print "inserting soccer data ..."
print ""

for file in files_to_run:
    execfile(file)
print ""

print "Finished"