

files_to_run = [r"nrl.py", r"super_rugby.py"]

print "inserting rugby data ..."
print ""

for file in files_to_run:
    execfile(file)
print ""

print "Finished"