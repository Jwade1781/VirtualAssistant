class DesktopActions:
    def __init__(self):
        return
    
    def AddFile(self, fileName: str)->bool:
        from FileActions import FileActions
        fileActions = FileActions()
        return fileActions.AddFile(fileName)
              
    def AddFolder(self, folderName: str)->bool:
        from FileActions import FileActions
        fileActions = FileActions()
        return fileActions.AddFolder(folderName)
        
    def Delete(self, fileName: str)->bool:
        from FileActions import FileActions
        fileActions = FileActions()
        return fileActions.Delete(fileName)
    
    def OpenFileExplorer(self, path: str)->bool:
        from FileActions import FileActions
        fileActions = FileActions()
        return fileActions.OpenFileExplorer(path)
