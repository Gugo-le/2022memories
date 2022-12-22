import dropbox
 
class DropBoxManager:
    def __init__(self,token, filename,pathname):
        
        self.appkey = "mvyjbkm3xeb49l7"
        self.refreshtoekn = "vvygxCYxIGEAAAAAAAAAAbksYhjobm7RRWXBs_sRlaErc1-C6nFn55eAyhJhQGf-"
        
        self.fileName = filename
        self.pathName = pathname
 
    def UpLoadFile(self):
        dbx = dropbox.Dropbox(oauth2_refresh_token=self.refreshtoken, app_key=self.appkey, timeout=900)
        with open(self.fileName, "rb") as f:
            dbx.files_upload(f.read(), self.pathName, mode=dropbox.files.WriteMode.overwrite)
 
    def GetFileLink(self):
        dbx = dropbox.Dropbox(oauth2_refresh_token=self.refreshtoken, app_key=self.appkey, timeout=900)
        shared_URL = dbx.sharing_create_shared_link_with_settings(self.pathName).url
        modified_URL = shared_URL[:-1] + '1'
        return modified_URL