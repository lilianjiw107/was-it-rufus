from datetime import datetime
import argparse
import subprocess

parser = argparse.ArgumentParser(
    description="This program prints specific facts about a local git repository.", 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
parser.add_argument("-g", "--git-dir", help="local directory in which to assess git status", required=True)

args = parser.parse_args()

def check_status():
    # Run command `git status`
    output = subprocess.check_output(['git', 'status'], cwd=args.git_dir).decode()
    lines = output.split('\n')

    # Get current branch
    assert lines[0].startswith('On branch')
    branch_name = lines[0].removeprefix('On branch ')
    print('active branch: ' + branch_name)
    
    # Check whether repository files have been modified
    changed = 'nothing to commit, working tree clean' != lines[-2]
    print('local changes: '+ str(changed))


def check_head():
    # Run command `git show HEAD`
    output = subprocess.check_output(['git', 'show', 'HEAD'], cwd=args.git_dir).decode()
    lines = output.split('\n')

    author_line, date_line = lines[1], lines[2]
    assert author_line.startswith('Author: ')
    assert date_line.startswith('Date:')

    # Check whether the current head commit was authored in the last week
    time_string = date_line.removeprefix('Date:')[:-5].strip()
    dt = datetime.strptime(time_string, "%a %b %d %H:%M:%S %Y")
    dt_now = datetime.now()
    is_recent = (dt_now - dt).days <= 7
    print('recent commit: ' + str(is_recent))

    # Check whether the current head commit was authored by Rufus
    author_name = author_line.removeprefix('Author:').strip().split(' ')[0]
    print('blame Rufus: ' + str(author_name == 'Rufus'))

if __name__ == "__main__":
    try:
        check_status()
        check_head()

    except Exception as e:
        # print(e)
        print('Not a git repository.')
