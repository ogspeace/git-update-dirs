'''
simple script which pushes local git repos of directories with similar
prefix/substrings all at once. 

some notes on git flags used:
    --git-dir=<path>.git - specifies the location of the repository's .git folder which contains the CONFIG file, which in turn contains your github repository and account's credentials.
    
    --work-tree=<path> - specifies current directory tree where current repo belongs to.

'''


from datetime import datetime
from os import system
import os

# gets pwd output
dir_path = os.path.dirname(os.path.abspath(__file__))

# iterates through files within current directory
for filename in os.listdir('.'):

    #looks for files with 'repo_' prefix - ideally we work with dirs here
    if 'repo_' in filename:

        # gets current time (mm/dd/YYYY-HH:MM:SS) - to append to commit -m message
        curr_time = datetime.today().strftime("%m/%d/%Y-%H:%M:%S")
        curr_path = f"{dir_path}\\{filename}\\"
        print(f"[ updating {filename.split('_')[1]} repo . . . ]", flush=True)
        os.system(f"git --git-dir={curr_path}.git --work-tree={curr_path} add {curr_path}")
        os.system(f"git --git-dir={curr_path}.git --work-tree={curr_path} commit -m \"{curr_time} update\"")
        os.system(f"git --git-dir={curr_path}.git --work-tree={curr_path} push origin master")
        print("", flush=True)

