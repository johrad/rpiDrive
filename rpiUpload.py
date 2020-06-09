from pydrive.drive import GoogleDrive
from quickAuth import g_login
#
import os
#
MyDrive = GoogleDrive(g_login)
folder_id = '1_Bs2Zy3x3aFADGf78l5QK5CKW8Kg7XBa'

# Create GoogleDriveFile instance with title 'Hello.txt'.
file1 = MyDrive.CreateFile({'title': 'Hello.txt',
                            'parents': [{'id': folder_id}]})
# Set content of the file from given string.
file1.SetContentString('Hello World!')
file1.Upload()
print("Upload complete.\n")
