# data-science

#######  Project technical information  #######

- The database is stored on localhost MySQL Server 5.7

- We used python 2.7.13 for establishing the database, while the GUI runs with python 3.

- The database runs on 'root' user with no password using charset 'utf-8'.

- Some of the queries we used can be found in 'queries.txt' which is placed in the main folder 'data-science'.

- We included a video sample of the project's GUI found as 'project_clip.mp4.

####### Installation instructions #######

1. Download and install MySQL Server 5.7:  https://dev.mysql.com/downloads/installer/

2. Download and install the prefered python version: https://www.python.org/downloads/

3. Install the required packages (see below).

4. Run the file 'run.py'
   This should create and fill the database which then can be queried using SQL statements.

5. Run the file 'projectGUI.py', using python 3.
   This should display the GUI as shown in the video.

####### Pip modules required for the project to run  #######

DB modules: (using pip2)

- pymysql
- xlrd
- dateutil
- calendar

GUI modules: (using pip)

- tkinter
- matplotlib
- pymysql

