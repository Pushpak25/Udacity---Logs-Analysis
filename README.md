# Udacity---Logs-Analysis

# About
<br/>
This project is a part of Udacity Full Stack Nanodegree. In this project, we build an internal reporting tool for a newpaper site to discover insights on what kind of articles the site's readers like, by building complex SQL queries on a large database with over a million rows to draw business conclusions for the data. The database contains newspaper articles, as well as the web server log for the site.
<br/>

# Setup Required

You will need:
<br/>
Python - 2.X
Vagrant
VirtualBox
Setup
<br/>
Vagrant virtual machine is required for this project which you can find here: https://github.com/udacity/fullstack-nanodegree-vm 
<br/>
First, fork the fullstack-nanodegree-vm repository so that you have a version of your own within your Github account. Next clone your fullstack-nanodegree-vm repo to your local machine. 
To use the Vagrant virtual machine, navigate to the full-stack-nanodegree-vm/tournament directory in the terminal, then use the command ```vagrant up (powers on the virtual machine)``` followed by ```vagrant ssh (logs into the virtual machine)```.
<br/>

To load the data, use the command ```psql -d news -f newsdata.sql``` to connect a database and run the necessary SQL statements.
<br/>

# Tables
The database includes three tables:
<br/>
<ul>
<li> Authors table  -  Includes information about the authors of articles </li>
<li> Articles table -  includes the articles </li>
<li> Log table      -  Includes one entry for each time a user has accessed the site
</ul>
<br/>

# Problem
<br/>
Here are the questions the reporting tool will answer:
<ol>
<li> What are the most popular three articles of all time? </li>
<li> Who are the most popular article authors of all time?</li>
<li> On which days did more than 1% of requests lead to errors?</li>
</ol>
<br/>

# Output
To execute the program, run ```python logs.py``` from the command line. You can see the output in the file output.txt in the same folder. For sample output, you can check output.txt file in this repo.
