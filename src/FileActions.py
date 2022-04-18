class FileActions:
    def __init__(self):
        return
    
    # Attempts to create a new file with the given filename and opens the explorer for it
    def AddFile(self, fileName: str)->bool:
        try:
            file = open(fileName, "x")
            print("File Created")
            file.close()
            import os
            self.OpenFileExplorer(os.getcwd() + "\\" + fileName)
            return True
        
        except FileExistsError:
            self.ReportError("Cannot Add File: Prexisting file found", "AddFile(self, fileName: str)->bool", fileName)
            return False
        
        except:
            self.ReportError("Unexpected Error occured in AddFile", "AddFile(self, fileName: str)->bool", fileName)
            return False
              
    def AddFolder(self, folderName: str)->bool:
        return True
        
    def Delete(self, fileName: str)->bool:
        import os
        
        try:
            if (os.path.exists(fileName)):
                if (os.path.isfile(fileName)): os.remove(fileName)
                else: os.rmdir(fileName)
                return True
            
        except:
            self.ReportError("No File/Folder Exists to Delete", "Delete(self, fileName: str)->bool", fileName)
            return False
    
    def OpenFileExplorer(self, path: str)->bool:
        try:
            import subprocess
            subprocess.Popen(r'explorer /select,' + path)
            return True
        
        except:
            self.ReportError("Error occured upon opening the given path: " + path, "OpenFileExplorer(self, path: str)->bool", path)
            return False
        
    def ReportError(self, errorDescrip: str, errorFunction: str, argument: str):
        import os
        from ErrorLogger import ErrorLogger
        errorFile = os.getcwd()
        
        ErrorLogger(errorDescrip, errorFunction, errorFile, argument)
        
        