# Was-it-rufus
Coding take-home for Pronto.ai
## How to run
Run the following command in your terminal
```
python main.py -g GIT_DIR
```
where `GIT_DIR` is a local git repository directory. Both full path and relative path are acceptable.

The program should print the following things:

- active branch (boolean)

- whether repository files have been modified (boolean)

- whether the current head commit was authored in the last week (boolean)

- whether the current head commit was authored by Rufus (boolean)
```
active branch: main
local changes: False
recent commit: True
blame Rufus: True
```
or
```
Not a git repository.
```
if the `GIT_DIR` is not a directory of a git repository.
