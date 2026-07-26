import os
import random
import string
import subprocess
import time

def generate_random_text(length=12):
    """Generates a random alphanumeric string."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    # Get the absolute path of the script currently running
    script_path = os.path.abspath(__file__)
    
    # Randomly choose between 5 or 6 iterations
    num_commits = random.randint(5, 6)
    print(f"Starting {num_commits} automated commits for {os.path.basename(script_path)}...\n")

    for i in range(num_commits):
        random_text = generate_random_text()
        
        # 1. Modify the file by appending a comment with the random text
        with open(script_path, "a") as file:
            file.write(f"\n# Auto-generated string: {random_text}")
        
        try:
            # 2. Stage the modified file
            subprocess.run(["git", "add", script_path], check=True, capture_output=True)
            
            # 3. Commit the changes
            commit_message = f"Automated commit {i+1}/{num_commits}: Added {random_text}"
            subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True)
            
            print(f"[{i+1}/{num_commits}] Successfully committed with text: {random_text}")
            
            # Pause briefly to ensure commit timestamps are distinct
            time.sleep(1)
            
        except subprocess.CalledProcessError as e:
            print(f"Git command failed. Are you in an initialized git repository?")
            print(f"Error details: {e.stderr.decode('utf-8').strip()}")
            break

if __name__ == "__main__":
    main()
# Auto-generated string: wG5BdoeMeeVb
# Auto-generated string: 0e4uZTJoIw9i
# Auto-generated string: YU31wg2Lw4E6
# Auto-generated string: OBlhmY5Oxh0s
# Auto-generated string: UbBvOZZuEBG2