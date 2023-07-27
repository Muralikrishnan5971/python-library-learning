import sys
import time

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import logging
import getpass
import shutil
import os

"""
   print(sys.argv)
   sys.argv is list of all arguments passed to the script as string, 
   which has the name of the script as the first value.

   try running python learn_watchdog.py -r -3 -4 -44

   we get: ['learn_watchdog.py', '-r', '-3', '-4', '-44']

   getpass module has two function

   getpass.getuser() --> gives the username
   getpass.getpass() --> prompts for a password string and then prints the entered string

   the propmt msg can be changed as getpass.getpass(prompt='Please enter passphrase')

   Shutil module offers high-level operation on a file like a copy, create,
   and remote operation on the file. It comes under Pythons standard utility modules.
   This module helps in automating the process of copying and removal of files and directories.

   copies the content of source to destination
   shutil.copy(source, dest)
   this method also returs the dest path as string

   shutil.copy2() method in Python is used to copy the content of the source file
   to the destination file or directory. This method is identical to shutil.copy() method
   but it also tries to preserve the files metadata.

   shutil.copy2(source, dest)
   also returns the dest path as string

   shutil.copyfile(source, dest)
   copies the file content for source to dest and returns dest path as string

   """

# To back up our directory to another folder

def on_modified(event):
    """
    Back up the directory by coping the folder to another location,
      if there is a modification.
    """
    backup_directory_path = "/Users/muralikrishnan/Desktop/murali/learn_modules/backup/"
     
    # fetch all files in path
    for filename in os.listdir(path):
        #construct full file path
        source = path + "/" + filename
        dest = backup_directory_path + filename

        print('*' * 50)
        print(source)
        print(dest)
        print('*' * 50)

        #copy file if it is a file
        if os.path.isfile(source):
            shutil.copy(source, dest)
            print(f"Backed up {filename} to {dest}")



if __name__ == '__main__':

    user = getpass.getuser()

    logging.basicConfig(
        filename='monitor.log',  # store logs to a file
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(process)d - %(message)s' +
        f'user: {user}',    # store logs with username
        datefmt='%Y-%m-%d %H:%M:%S') 

    path = sys.argv[1] if len(sys.argv[1]) > 1 else '.'
    
    event_handler = LoggingEventHandler()
    # overriding the event_handler.on_modified method to our custom on_modified,
    # so that everytime there is a modification, our on_modified() fucntion is called.
    event_handler.on_modified = on_modified
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


     