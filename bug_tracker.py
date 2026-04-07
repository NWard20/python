"""
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""
"""Assignment Name: Lesson 11A: Writing to files 🆕🆕🆕🆕🆕 Replacement for next semester but please do!
Date: 4/6/2026
File Name: bug_tracker.py
"""

from datetime import datetime

def main():
    bugs = {}

    while True:
        user_input = input("Type 'log' to file a bug, or 'quit' to quit: ")

        if user_input.lower() == "quit":
            print("Log updated")
            break

        elif user_input.lower() == "log":
            file_name = input("File name: ")
            description = input("Description of error: ")
            priority = input("Priority (High, Medium, Low): ")

            # Gathering current date and time 
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Store the data
            bugs[time] = [file_name, description, priority]

            # Write to a file
            with open("bug_log.txt", "a") as f:
                f.write(f"""
        [{time}]
        File: {file_name}
        Status: {description}
        Priority: {priority}
        {"-" * 50}
        """)

        else:
            print("Type 'log' or 'quit'")

if __name__ == "__main__":
    main()