# Was-it-rufus
Coding take-home for Pronto.ai
## How to run
Run the following command in your terminal
```
python main.py -g GIT_DIR
```
where `GIT_DIR` is a local git repository directory.

The program should print something like
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
