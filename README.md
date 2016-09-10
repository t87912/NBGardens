# NBGardens ASAS

# NOTICE: "don't do anything to the master, work on the python/gui branch" - Tom.
Refer to the instruction - developer section for more details on using branches.

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
Below are some screenshots of the new features for application;

<!-- <ul>
    <li>
        <div>Website with new data type options such as Flickr and distinct user filters:</div>
        <div><img src="https://raw.githubusercontent.com/ameenhaq/VernacularPlaceNameFinder-Project/master/img/0.png" /></div>
    </li>
    <br />
    <li>
        <div>Website with new statistical data and GeoPy integration:</div>
        <div><img src="https://raw.githubusercontent.com/ameenhaq/VernacularPlaceNameFinder-Project/master/img/1.png" /></div>
    </li>
    <br />
    <li>
        <div>Modified API facility with additional statistical information for ease of comparison (e.g. mean and median density, precision, recall, f-measure, accuracy and error):</div>
        <div><img src="https://raw.githubusercontent.com/ameenhaq/VernacularPlaceNameFinder-Project/master/img/2.png" /></div>
    </li>
    <br />
    <li>
        <div>Webpage that visualizes the concave (blue = Comparison data, red = system/ social media data) and convex hull (purple = Comparison data, orange = system/ social media data). This example shows the concave and convex hull polygon of Canton:</div>
        <div><img src="https://raw.githubusercontent.com/ameenhaq/VernacularPlaceNameFinder-Project/master/img/3.png" /></div>
    </li>
</ul> -->
<br /><br />

## Instructions
#### Developers
In an effort of good version control the project makes use of git technology and the Github service. Below you will find a series of suitable and appropriate commands to achieve certain routine actions. Please follow the syntax and insert any relevant additional information as stated. <br />

**Clone the repository** - Laymen: set up a link between the link repoistory to your local system. This should be your first git command and you should in theory only need it once.
<p align="center">
    _GIT CLONE + `<REPO>` + `<SAVE DIRECTORY>`_
</p> <br />


**Add and append in the repository individually** - Laymen: update the repository of any local changes so that a shared version is generated on Github.
<p align="center">
    _GIT ADD + `<FILE NAME>`_
</p> <br />
**Add multiple to the repository** - Laymen: Similarly to the above, but for multiple files and changes.
<p align="center">
    _GIT ADD + `<FILE NAME>`_
</p> <br />


**Commit to the repository** - Laymen: encapsulate everything added into one binded package update to be pushed. The 'm' in this instance can stand for message, please include this when using this command and describe any amendment or other update made.
<p align="center">
    _GIT COMMIT -M "`<SOME TEXT>`"_
</p> <br />


**Publish to the repository** - Laymen: update the repository of any local changes so that a shared version is generated on Github. It is crucial to include the '-u' which specifies the branch for effectively control 'pushes'. Your branch maybe 'python', 'gui', 'master origin' - please only use the branch you've been allocated to.
<p align="center">
    _GIT PUSH -U `<BRANCH NAME>`_
</p> <br />


**Remove file from repository** - Laymen: Should you wish to remove file(s) from repository.
<p align="center">
    _GIT RM `<FILE NAME>`_
</p> <br />
**Remove folder from repository** - Laymen: Similarly to remove a folder use the following with the inclusion of '-R'.
<p align="center">
    _GIT RM -R `<FOLDER NAME>`_
</p> <br />

NOTE: Remember this is version control thus any mistake can be reversed. A full listing of further commands by using are friendly search engine, Google or just ask Anthony.<br />

#### Normal Users
Download the application with the additional required packages, there is no requirement in cloning the repository. <br /><br />



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
install tkinter	                 # tkinter: graphical user interface (GUI)
install csv                      # webpy: provide API facilities
install sys                      # mysqldb: retrieve mysql data
```
More details on installation are provided in additional doxygen documentation. <br /><br />


## Support
This project is a part of QAC learning projects. The project will be continued in the near future under QAC.
