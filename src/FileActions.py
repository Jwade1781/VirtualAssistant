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
            print("File not created: Prexisting file found\t")
            file.close()
            return False
        
        except:
            print("Unexpected Error")
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
            print("No File/Folder Exists")
            return False
    
    def OpenFileExplorer(self, path: str)->bool:
        try:
            import subprocess
            subprocess.Popen(r'explorer /select,' + path)
            return True
        
        except:
            print("Error occured upon opening the given path: " + path)
            return False