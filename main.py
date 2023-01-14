import argparse
import subprocess

parser = argparse.ArgumentParser(
    description="This program prints specific facts about a local git repository.", 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
parser.add_argument("-g", "--git-dir", help="local directory in which to assess git status", required=True)

args = parser.parse_args()

if __name__ == "__main__":

    output = subprocess.check_output(['git', 'status'], cwd=args.git_dir)

    print(output)

