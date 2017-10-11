#   Jeff W. Ferrell 10/11/17
#   Python Course, item 65
#   Moving recently updated (within 24 hours).txt files from one folder to another
#   Made with Python 3.6 using tkinter, datetime, filedialog, shutil, and os modules

from tkinter import *
import tkinter as tk
import tkinter.filedialog

import datetime as dt
import shutil
import os

root = Tk()

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.minsize(375,50)
        self.master.maxsize(375,50)
        self.master.title("Press Button to Move Recents from Source")

        self.btn_MoveFiles = tk.Button(self.master,width=48,height=2, text='Move .txt Files Modified in last 24 hours to Destination Folder',command = lambda: self.MoveRecentlyModified(source,destination))
        self.btn_MoveFiles.grid(row=0,column=0,padx=(15,0),pady=(5,0),sticky=N+S+E+W)


    def SelectSource():
        global source
        source = tkinter.filedialog.askdirectory(parent=root,initialdir="/Source_Options",title='Select a Folder to Sort and Move Recent Text Files From')   
        print(source)
        return source
    SelectSource()
    

    def SelectDestination():
        global destination
        destination = tkinter.filedialog.askdirectory(parent=root,initialdir="/Destination_Options",title='Select a Folder to Move Text Files Modified Within the Last 24 Hours To')
        print(destination)
        return destination
    SelectDestination()


    def MoveRecentlyModified(self,source,destination):
    
        folder = os.listdir(source)
    
        for files in folder:
            path = os.path.join(source, files)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                recents = ('%s modified %s'%(path, mtime))
                if files.endswith('.txt'):
                    shutil.move(os.path.join(source, files), os.path.join(destination))
                

if __name__== '__main__':
    App=ParentWindow(root)
