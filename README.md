# git-update-dirs

## description
simple script which pushes local git repos of directories with similar prefix/substrings all at once.


## some notes on git flags used:
```
    --git-dir=<path>.git 
```
- specifies the location of the repository's .git folder which contains the CONFIG file, which in turn contains your github repository and account's credentials.
```
    --work-tree=<path> 
```
- specifies current directory tree where current repo belongs to.

## requirements
- your personal access token (don't share with anyone else).

- edit `.git/config` file - and edit the `url` line's value:
```
url = "https://<yourusername>:<your personal access token>@github.com/<yourusername>/<yourreponame>.git
```

## final notes
- i personally use this script to automate / 'sync' certain repositories on multiple platforms i use. 
- you *can* convert this as a headless push / puller (sync with remote, sync with local) script
- do *not* share your personal access token (especially if you wish to use and/or fork this script.
- be very specific in what files you have to ignore in your `.gitingore` files.
