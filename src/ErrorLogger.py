def ErrorLogger(errorDescrip: str, errorFunction: str, errorFile: str, argument: str):
    import os
    from datetime import date
    
    errorDate = date.today().strftime("[%B %d, %Y] [%H %M %S]")
    
    fileName = "ErrorLogs.log"
    errorLogPath = os.path.normpath(os.getcwd() + os.sep + os.pardir) + "\Logs\\" # retrace back to the parent directory
    file = open(errorLogPath + fileName  , "a") # Open the error log file in the Logs directory
    
    fullWrite = "======================================================================================================\n"
    fullWrite += errorDate + "\tSource File: " + errorFile
    fullWrite += "\n\t\t\t\tFunction: " +  errorFunction
    fullWrite += "\n\t\t\t\tDescription: " + errorDescrip
    fullWrite += "\n\t\t\t\tArguments: " + argument + "\n"
    fullWrite += "======================================================================================================\n\n"
    
    file.write(fullWrite)
    file.close()
    return
    
    