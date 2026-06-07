import scratchattach as sa
import warnings
warnings.filterwarnings('ignore', category=sa.LoginDataWarning)


try:
    with open("login.txt", "r") as f:
        username = f.readline().strip()
        password = f.readline().strip()
except FileNotFoundError:
    username = input("Username: ")
    password = input("Password: ")

    with open("login.txt", "w") as f:
        f.write(username + "\n")
        f.write(password + "\n")


session = sa.login(username, password)

project_id = input("Project ID: ")
cloud = session.connect_cloud(project_id)

print("\nCloud Variables:")
variables = cloud.get_all_vars()

for name, value in variables.items():
    print(f"{name} = {value}")

var = input("\nVariable to change: ")
value = input("New value: ")

cloud.set_var(var, value)

print("Variable", var, "was set to", value)
