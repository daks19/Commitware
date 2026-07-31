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
    num_commits = 20
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
            print("Git add/commit failed. Are you in an initialized git repository?")
            print(f"Error details: {e.stderr.decode('utf-8').strip()}")
            return  # Exit the script early if committing fails

    # 4. Push the new commits to the remote repository
    print("\nPushing commits to remote repository...")
    try:
        subprocess.run(["git", "push"], check=True, capture_output=True)
        print("Successfully pushed to remote!")
    except subprocess.CalledProcessError as e:
        print("Git push failed. Do you have a remote configured and an upstream branch set?")
        print("You may need to run: git push -u origin <branch-name>")
        print(f"Error details: {e.stderr.decode('utf-8').strip()}")

if __name__ == "__main__":
    main()
# Auto-generated string: nQKxrhWusKwX
# Auto-generated string: xi6UUlrZtQ41
# Auto-generated string: ZRFYtsSz4Fga
# Auto-generated string: xfVM4jPHm7kP
# Auto-generated string: u8T4EUX6cCf8
# Auto-generated string: ElIzYD23Yogy
# Auto-generated string: GdEiIHvf2fyf
# Auto-generated string: tecgHmwHb1Ti
# Auto-generated string: l8wzBdKRMekz
# Auto-generated string: 2NyNzSykMkaj
# Auto-generated string: e9qkUelQsjEg
# Auto-generated string: 3syDH7ul62k3
# Auto-generated string: sIreOjxZSLfX
# Auto-generated string: 9WVMGQiMlpIE
# Auto-generated string: rg0jF3C2rmBb
# Auto-generated string: L65xbnBsMXTV
# Auto-generated string: mHcPA9wsQLKT
# Auto-generated string: x3sYWBUlhhZk
# Auto-generated string: i8m1i04SxdGi
# Auto-generated string: TXTRNcFqwon9
# Auto-generated string: 8OPOKkBSOW6h
# Auto-generated string: n8PIqHWYotiQ
# Auto-generated string: M8LQv8kXVYoK
# Auto-generated string: v3PlfO3jvh3g
# Auto-generated string: ZLhFhjG2ZHSE
# Auto-generated string: y9zY3NxaLHLc
# Auto-generated string: hVMzMJV2yE4m
# Auto-generated string: 6ZpcZLGpNmY2
# Auto-generated string: 72LJa2afrmqK
# Auto-generated string: eomto3epXn0I
# Auto-generated string: 7pdXj8t9DEBz
# Auto-generated string: D0YWskTPT9nJ
# Auto-generated string: Wj1QpgtEW9IV
# Auto-generated string: WmUySxIfxajm
# Auto-generated string: EfkF5QXvgqUi
# Auto-generated string: 9L0WT8C8gAzc
# Auto-generated string: vnCTJMIB0c8O
# Auto-generated string: dFhM0vh5uZk4
# Auto-generated string: sHuHO4l3AW4t
# Auto-generated string: Wpxt32G3sAG3
# Auto-generated string: cOGSlnzjyCGv
# Auto-generated string: wXSlzZ3xEUOr
# Auto-generated string: KsRRVAvzL15g
# Auto-generated string: Z3ILuMaFDqwY
# Auto-generated string: UoeAaxZ39jgs
# Auto-generated string: kke2vZiys53u
# Auto-generated string: Bpp5mNyYCdkd
# Auto-generated string: E1thYmFwAp5A
# Auto-generated string: dMZG9sxkJWOr
# Auto-generated string: 3YtczHuqH0SS
# Auto-generated string: YFqabKxdQvuz
# Auto-generated string: B92JaL5oemOL
# Auto-generated string: iaAsEpzArIJq
# Auto-generated string: 7Y1vZXKSbeEc
# Auto-generated string: 8N3u6XPHPRKi
# Auto-generated string: r6kN4SGZKk6z
# Auto-generated string: H3h34Ivrna4o
# Auto-generated string: y05Tn88SMKOI
# Auto-generated string: fqsy0UojZCg9
# Auto-generated string: 2EwpqswFJM8R
# Auto-generated string: xsoP4TqSvLx1
# Auto-generated string: K6AfvJeehDHY
# Auto-generated string: wT91O9UYiLov
# Auto-generated string: Q0WETFLzJmAM
# Auto-generated string: l8cjaxOhJRjt
# Auto-generated string: fTlU6BTt0UVj
# Auto-generated string: vj53v2kRY0w5
# Auto-generated string: VGPX43N89t6t
# Auto-generated string: PZvYyN9fFOsk
# Auto-generated string: fiHnzFJiWdlc
# Auto-generated string: vh0lRpwSKuxh
# Auto-generated string: YnerwDB5pwFq
# Auto-generated string: HdtdmCo5lIQt
# Auto-generated string: n6GXkVV0K2zf
# Auto-generated string: GHO1cjNeA2sr
# Auto-generated string: xdFazPAO4ciC
# Auto-generated string: sQs2gWrBBFDg
# Auto-generated string: fx8ojsJNZpvd
# Auto-generated string: 31MSBZe2CMyX
# Auto-generated string: pR2aMrY3BUy6
# Auto-generated string: 41rtG3IAkMn8
# Auto-generated string: CCdo1Wla5rv0
# Auto-generated string: MB9PEAecOxFq
# Auto-generated string: pUXzOSR9x6Ki
# Auto-generated string: rFGP0uf09Nc4
# Auto-generated string: gXxvd89AK0vF
# Auto-generated string: ItAt55fvmPfk
# Auto-generated string: KWTqip86tcGY
# Auto-generated string: SJPSW0LKr4E1
# Auto-generated string: mzSNlGlORDsw
# Auto-generated string: h35tcUm9cDgQ
# Auto-generated string: tH3cKLcXDmzI
# Auto-generated string: c1gLBnt1cflA
# Auto-generated string: W5VdV6O76cLT
# Auto-generated string: meq71HP0s249
# Auto-generated string: 6f1CVWXxNT53
# Auto-generated string: tV1E0itftbNQ
# Auto-generated string: 8YYYJwLUAkjP
# Auto-generated string: 0L5RmTaaPnph