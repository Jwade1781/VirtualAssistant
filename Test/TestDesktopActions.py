#######################################################################
#
# Purpose:
# Purpose of this file is to test the general functionality of Desktop Actions
#
# Extra Info:
# The inputted 1st argument corresponds to the test to run:
# 0: Run All Tests, 1: Add File, 2: Delete
#
# The inputted 2nd argument corresponds to the filename if not relevant 
# Run:
# --
#
#######################################################################

import sys, time
sys.path.append('../src') # Quick and dirty way to import, testing just functionality
import DesktopActions as DesktopActions

def TestRun(TestingKey: int, fileName: str):
    testsRunKeyMap = {
                        0: TestAll,
                        1: TestAddFile,
                        2: TestDelete,
                     }
    
    desktopAct = DesktopActions.DesktopActions() 
    testsRunKeyMap[int(TestingKey)](desktopAct, fileName)
 
def TestAll(desktopAct: DesktopActions, fileName: str):
    TestAddFile(desktopAct, fileName)
    
    time.sleep(5) # Allows time to check if file was created before being deleted
    TestDelete(desktopAct, fileName)
    
def TestAddFile(desktopAct: DesktopActions, fileName: str):
    print("Filename: " + fileName + "\tAdded: " + str(desktopAct.AddFile(fileName)))
    return
    
def TestDelete(desktopAct: DesktopActions, fileName: str):
    print("Filename: " + fileName + "\tDeleted: " + str(desktopAct.Delete(fileName)))
    return

TestRun(sys.argv[1], sys.argv[2])
