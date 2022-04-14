# Desktop Virtual Assistant
    
## Updates
  4/13/2022 - Initial README.MD created

## Description
This project is to create a virtual desktop assistant similar to Microsoft's Cortana.
Some highlights of the project will include accurate speech recognition, basic user interaction functions,
& potentially safety features such as secure password storage and password suggestion.

# Functions and tasks that will be implemented
    [1] Use speech recognition to understand and parse out user specifed actions such as:
        "Open new Word Document", "Delete Folder Tools", "Empty Recycling Bin"
      
    [2] Implement the previously parsed tasks.
    
    [3] Implement periodic emotion detection using the users camera. This could be used to
        offer advice or give relevant quotes that may aid the user.
    
# Dependencies [Tested versions in brackets]
    [1] Python 3 [3.9]
    [2] PyAudio [0.2.11] 
    [3] SpeechRecognition [3.8.1]

# Quick Setup
    Run /Setup/Setup.py to quickly install any dependent files & creation of any required additional folders. Uses pip for installation.

# How to Run Programs 
Setup the directories && Install Dependencies
    python ./Setup.py 'Install Required Modules (True/False)'


# TODO
[1] Create GUI using WPF or Electron & implement method that allows it to communicate with the python scripts. This will give the project a more user friendly interface     than running straight from the command line.

[2] Implement more functions that the user is able to carry out. File: /src/DesktopActions.py
[3] Investigate Speech Recognition accuracy. Seems to give inaccurate results at times, could be related to ambient noise. File: /src/SpeechRecognition.py
