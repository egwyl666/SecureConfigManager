import json
from config_protector import hide_config_data, show_config_data

key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='

# Hide the configuration data
hide_config_data(key)
# Restore the hidden configuration data
show_config_data(key)


def load_config(filename='config.json'):
    # Load the configuration from a file
    with open(filename, 'r') as file:
        config = json.load(file)
    return config


def greet_user(login):
    # Greet the user
    print(f"Welcome, {login}!")


def check_password(users, max_attempts):
    # Check the user's password
    for _ in range(max_attempts):
        password = input("Please enter your password: ")
        # Check the password for each user in the list
        for user in users:
            if password == user['password']:
                return user['login']
        # Display a message about the wrong password
        print("Incorrect password. Try again.")
    return 'Intruder'


def check_auth_code(auth_code, max_attempts):
    # Check the authentication code
    for _ in range(max_attempts):
        entered_code = input("Please enter the authentication code: ")
        if entered_code == auth_code:
            return True
        # Display a message about the wrong authentication code
        print("Incorrect authentication code. Try again.")
    return False


def main():
    # Load the configuration
    config = load_config()
    users = config['users']
    auth_code = config['auth_code']
    max_attempts = config['attempts']

    # Check the user's password
    user = check_password(users, max_attempts)
    if user != 'Intruder':
        # Greet the user
        greet_user(user)
        # Check the authentication code
        if check_auth_code(auth_code, max_attempts):
            greet_user(user)
        else:
            print(
                "Maximum number of authentication code entry attempts reached. Access denied.")
    else:
        print("Maximum number of password entry attempts reached. Access denied.")


if __name__ == "__main__":
    main()
