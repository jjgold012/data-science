files_to_run = [r"2002m.py", r"2003m.py", r"2004m.py", r"2005m.py", r"2006m.py",
                r"2007m.py", r"2007w.py", r"2008m.py", r"2008w.py", r"2009m.py", r"2009w.py", r"2010m.py",
                r"2010w.py", r"2011m.py", r"2011w.py", r"2012m.py", r"2012w.py", r"2013m.py", r"2013w.py",
                r"2014m.py", r"2014w.py", r"2015m.py", r"2015w.py", r"2016m.py", r"2016w.py", r"2017m.py",
                r"2017w.py"]

print "inserting tennis data ..."
print ""

for file in files_to_run:
    execfile(file)
print ""

print "Finished"