#######################################################################
#
# Purpose:
# The purpose of this program is to easily allow the user to install all
# dependencies within the system, using pip as well as creating any necessary directories.
#
# Extra Info:
# Should be the first run program to ensure all imports are installed
# & the data directory / subdirectories are created
#
# Works by iterating through a list of libraries that must be installed
# for the programs to work correctly. It will check to see if the library
# has already been installed, if not, it will install it using pip command.
#
# After the libraries are installed, the program will create the Data directory
# and the subdirectories 
#
# Run:
# python ./Setup.py 'Install Required Modules (True/False)'
# python ./Setup.py True
#
#######################################################################
def main():
    Install_Imports()
    Create_Directories()

####################################################################### 
# install all of the required imports using pip
def Install_Imports():
    import subprocess, sys
    if sys.argv[1].lower() == 'true':
        print("Installing imports")
        imports = ['speechrecognition', 'pyaudio', 'pocketsphinx', 'pywin32', 'flask', 'celery']

        for i in range (len(imports)):
            subprocess.call([sys.executable, "-m", "pip", "install", imports[i]])

#######################################################################
# Create the Data directory and the subdirectories of it
def Create_Directories():
    import os
    
    requiredDirectories = ["Data/", "Data/temp/", "Data/temp/xml/", "Data/Test/"]
    for directory in requiredDirectories:
        try: 
            os.mkdir(directory)
            print(directory + ' was created')
        except: print(directory + ' was already created')

#######################################################################
main()
