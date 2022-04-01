import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filesname in files:
                local_path=os.path.join(root, filesname)

                relative_path=os.path.relpath(local_path, file_from)
                dropbox_path=os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BE4169n21dJvFkbUjpFejxnWuBbXwE2mEY6bAR8KE4SLl7UBaeul-XxNvnbjXc9oDinyvMTkh063cvIi1-Pe8UkKHlWGXncgCyMK3ZWeuB3RirLV_BpGa95apEXZKOY0s_F3eyo'
    transferData = TransferData(access_token)

    src = str(input("Enter the path or file you want to upload to dropbox. "))
    dest = input("enter the full path to upload to dropbox:- ") 

    transferData.upload_file(src,dest)
    print("Your file has been uploaded to the dropbox!")

main()