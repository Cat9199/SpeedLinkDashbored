import subprocess
import datetime

# Set your repository's path here
repo_path = './'
# Set the branch you want to commit to
branch = 'main'

# Function to run shell commands
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=repo_path)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print("Error:", stderr)
    else:
        print(stdout)

# Function to make a commit on a specific date
def make_commit(date):
    formatted_date = date.strftime("%Y-%m-%dT%H:%M:%S")
    env_variables = f'GIT_COMMITTER_DATE="{formatted_date}" GIT_AUTHOR_DATE="{formatted_date}"'
    commit_message = f'Commit on {date.strftime("%Y-%m-%d")}'
    # Add your file changes here. For example, creating a file named by date.
    with open(f"{repo_path}/{date.strftime('%Y-%m-%d')}.txt", 'w') as file:
        file.write(f"Commit on {date.strftime('%Y-%m-%d')}")
    run_command(f'git add .')
    run_command(f'{env_variables} git commit -m "{commit_message}"')

# Main script to loop through dates
def main():
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date.today()
    delta = datetime.timedelta(days=1)
    
    current_date = start_date
    while current_date <= end_date:
        make_commit(current_date)
        current_date += delta
    
    # Push the changes to the repository
    run_command(f'git push origin {branch}')

if __name__ == "__main__":
    main()
