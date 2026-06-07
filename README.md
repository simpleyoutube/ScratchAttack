# Scratch Cloud Variable Editor

A small Python script that lets you log into Scratch, view cloud variables, and change them from the terminal using `scratchattach`.

---

## Features

- Logs into Scratch with your username and password  
- Saves login details locally (so you don’t have to type them every time)  
- Connects to a Scratch project’s cloud variables  
- Shows all current cloud variables  
- Lets you update values quickly  

---

## Requirements

Install the only dependency:

```bash
pip install scratchattach
```bash
How to use it

Run the script:

python main.py

Then follow the prompts:

Enter your Scratch username and password (saved to login.txt)
Enter the project ID
View the cloud variables
Pick one and set a new value
Example
Username: your_username
Password: your_password
Project ID: 123456789

Cloud Variables:
score = 10
coins = 5

Variable to change: score
New value: 999
Variable score was set to 999
Files
main.py – main script
login.txt – created automatically to store login info
Note on security

Your login is saved as plain text in login.txt.
It’s convenient, but not secure. If you care about that, switch to something like keyring.

Requirements
Scratch account
Cloud variables enabled in the project
Project must be shared for cloud variables to work
License

Do whatever you want with it, just don’t blame me if it breaks 😄
