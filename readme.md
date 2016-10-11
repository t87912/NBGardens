# NBGardens ASAS

## Brief Project Description
This project is a shared project produced by a group of trainee consultants enrolled in August 2016 of QA Consulting. The project includes a python based program that serves as a customer purchasing system of gnomes and hot-tubs. The program makes use of the SQL language to query pre-stored data from a MySQL database as well as the use of Mongo queries to retrieved data from a developed distributed database. Both database tools are used as part of this program for different purpose. The MySQL database is predominant to manage the general functions of the company (e.g. logging of inventory) and recording an purchases by any customers. Whilst the distributed database, MongoDB, is used for the website providing a subset of tables available from the superset MySQL database. Several pre-structured queries are encapsulated into the system, allowing the user (a member of staff) to simply run the it as a feature while providing additional parameter to retrieve specific output data. -- TO BE CHANGED


## Previously Added
* Basic graphical interface support.


## New Features/ Changes
* To be filled.


## Next Upload
* Login Support
* Query log system
* To be filled.


## Highlighted Features
Below are some screenshots of the new features of the application;

<ul>
    <li>
        <div>Menu option list ..... some text:<br /> </div>
        <div><img src="https://raw.githubusercontent.com/t87912/NBGardens/master/qaShared-Python-Friday/img/nbgardensTUI.PNG" /></div>
    </li>
    <br />
    <li>
        <div>Query system.... some text :</div>
        <div><img src="https://raw.githubusercontent.com/t87912/NBGardens/master/qaShared-Python-Friday/img/nbscreenshot.PNG" /></div>
    </li>
    <!-- <br /> -->
    <!-- <li>
        <div>Modified API facility with additional statistical information for ease of comparison (e.g. mean and median density, precision, recall, f-measure, accuracy and error):</div>
        <div><img src="https://raw.githubusercontent.com/ameenhaq/VernacularPlaceNameFinder-Project/master/img/2.png" /></div>
    </li>
    <br />
    <li>
        <div>Webpage that visualizes the concave (blue = Comparison data, red = system/ social media data) and convex hull (purple = Comparison data, orange = system/ social media data). This example shows the concave and convex hull polygon of Canton:</div>
        <div><img src="https://raw.githubusercontent.com/ameenhaq/VernacularPlaceNameFinder-Project/master/img/3.png" /></div>
    </li> -->
</ul>
<br /><br />

## Instructions
#### Developers
In an effort of good version control the project makes use of git technology and the Github service. Below you will find a series of suitable and appropriate commands to achieve certain routine actions. Please follow the syntax and insert any relevant additional information as stated. <br />

**Clone the repository** - layman explanation: set up a link between the link repository to your local system. This should be your first git command and you should in theory only need it once.
<p align="center">
    _GIT CLONE + `<REPO>` + `<SAVE DIRECTORY>`_
</p> <br />


**Add and append in the repository individually** - layman explanation: update the repository of any local changes so that a shared version is generated on Github.
<p align="center">
    _GIT ADD + `<FILE NAME>`_
</p> <br />
**Add multiple files and changes to the repository** - layman explanation: Similarly to the above, but for multiple files and changes using the '.' operator.
<p align="center">
    _GIT ADD ._
</p> <br />


**Commit to the repository** - layman explanation: encapsulate everything added into one binded package update to be pushed. The 'm' in this instance can stand for message, please include this when using this command and describe any amendment and/ or update made.
<p align="center">
    _GIT COMMIT -M "`<SOME TEXT>`"_
</p> <br />


**Publish to the repository** - layman explanation: update the repository of any local changes so that a shared version is generated on Github. It is crucial to include the '-u' which specifies the branch for effectively control 'pushes'. Your branch maybe 'python', 'gui', 'master origin' - please only use the branch you've been allocated to.
<p align="center">
    _GIT PUSH -U `<BRANCH NAME>`_
</p> <br />


**Remove file from repository** - layman explanation: Should you wish to remove file(s) from repository.
<p align="center">
    _GIT RM `<FILE NAME>`_
</p> <br />
**Remove folder from repository** - layman explanation: Similarly to remove a folder use the following with the inclusion of '-R'.
<p align="center">
    _GIT RM -R `<FOLDER NAME>`_
</p> <br />

NOTE: Remember this is version control thus any mistake can be reversed. A full listing of further commands can be found by using are friendly search engine, Google or just ask Anthony.<br />

#### Normal Users
Download the application with the additional required material, there is no requirement in cloning the repository. <br /><br />



## Changelog
<!-- ### 0.3.0 — 01.05.2015
Included code for additional features suggest by Chris Jones - changing system parameter and improving query terms recognition.
### 0.2.2 — 01.05.2015
Resolved Edinburgh City Council dataset option issue.
### 0.2.1 — 01.05.2015
Fixed Website UI issues (i.e. some stat features not showing)
### 0.2.0 — 01.04.2016
Implemented concave hull for creating a polygon of system and gold-standard data - replacing convex hull. -->
#### 0.1.0 — 13.09.2016
Expected Alpha next week!!!  <br /><br />


## Libraries
Below are the internal libraries needed to execute the program; <br />
```
import tkinter	                 # tkinter: graphical user interface (GUI)
import csv                       # csv: save data to csv
import sys                       # sys: user input
```
More details on installation are provided in additional doxygen documentation. <br /><br />


## Support
This project is a part of QAC learning projects. The project will be continued in the near future under QAC.
