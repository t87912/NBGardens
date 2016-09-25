# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 19:57:08 2016

@author: user
"""

# test

from userStoryInfo import userStories

from mainTUI import MainLogic

noUserStories = len(userStories)
print (noUserStories)

sqlMenuLines = ["\nPlease select an option: ",
              "User Story Number | Description",
              "0. Quit",
              "1. Input a custom SQL query.",
              "2. Go back to the main menu"]

for x in range(0, len(userStories)):
    #print (userStories[x])
    sqlMenuLines.append(userStories[x][0])

#print (len(sqlMenuLines))

if __name__ == "__main__":
    app = MainLogic(sqlMenuLines)