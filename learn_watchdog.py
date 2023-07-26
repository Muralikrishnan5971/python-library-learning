import sys
import time

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import logging
import getpass

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

   """

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
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


     