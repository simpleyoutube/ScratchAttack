# Scratch Cloud Variable Editor

A simple terminal tool that lets you log into Scratch, view cloud variables, and change them using Python and `scratchattach`.

---

## What it does

- Logs into Scratch using your account
- Saves your login locally so you don’t need to retype it every time
- Connects to a Scratch project
- Lists all cloud variables in that project
- Lets you edit a variable instantly from the terminal

---

## Setup

Install the required library:

```md
# Scratch Cloud Variable Editor

A simple terminal tool that lets you log into Scratch, view cloud variables, and change them using Python and `scratchattach`.

---

## Install

```bash
pip install scratchattach
```

---

## How to run

```bash
python main.py
```

Then follow the prompts:

- Enter your Scratch username and password (first run only)
- Enter a project ID
- View cloud variables
- Pick one and change its value

---

## Example

```
Username: your_username
Password: your_password
Project ID: 123456789

Cloud Variables:
score = 10
coins = 5

Variable to change: score
New value: 999
Variable 'score' was set to 999
```

---

## Files

- `main.py` – main script  
- `login.txt` – created automatically to store your login info  

---

## Notes

- The project must have cloud variables enabled  
- The project must be shared on Scratch  
- Cloud variables only work in supported projects  

---

## Security

Your username and password are stored in plain text in `login.txt`.

---

## License

Do whatever you want with it. Just don’t expect it to be perfect.
```
DO NOT BLAME IT ON ME FOR WHAT YOU DO
