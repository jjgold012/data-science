files_to_run = [r"basketball1.py", r"nbl.py"]


print "inserting basketball data ..."
print ""

for file in files_to_run:
    execfile(file)
print ""

print "Finished"
