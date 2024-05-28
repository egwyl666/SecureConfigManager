import json
from cryptography.fernet import Fernet

# Function to load configuration from a file
def load_config(filename='config.json'):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config

# Function to save configuration to a file
def save_config(config, filename='unprotected_config.json'):
    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)

# Function to encrypt configuration data
def encrypt_config_data(config, key):
    # Create a Fernet object using the key
    fernet = Fernet(key)
    encrypted_config = {}
    # Encrypt the login and password of each user in the configuration
    for user in config['users']:
        encrypted_login = fernet.encrypt(user['login'].encode()).decode()
        encrypted_password = fernet.encrypt(user['password'].encode()).decode()
        encrypted_user = {'login': encrypted_login,
                          'password': encrypted_password}
        encrypted_config['users'] = encrypted_config.get(
            'users', []) + [encrypted_user]
    return encrypted_config

# Function to decrypt configuration data
def decrypt_config_data(encrypted_config, key):
    # Create a Fernet object using the key
    fernet = Fernet(key)
    decrypted_config = {'users': []}
    # Decrypt the login and password of each user in the configuration
    for user in encrypted_config['users']:
        decrypted_login = fernet.decrypt(user['login'].encode()).decode()
        decrypted_password = fernet.decrypt(user['password'].encode()).decode()
        decrypted_user = {'login': decrypted_login,
                          'password': decrypted_password}
        decrypted_config['users'].append(decrypted_user)
    return decrypted_config

# Function to hide configuration data by encrypting and saving in a new file
def hide_config_data(key, config_filename='config.json', protected_filename='protected_config.json'):
    # Load configuration from file
    config = load_config(config_filename)
    # Encrypt the configuration data
    encrypted_config = encrypt_config_data(config, key)
    # Save the encrypted configuration in a new file
    save_config(encrypted_config, protected_filename)
    print(f"Configuration data successfully protected and saved in the file '{protected_filename}'")

# Function to display configuration data by decrypting and saving in a new file
def show_config_data(key, protected_filename='protected_config.json', unprotected_filename='unprotected_config.json'):
    # Load the encrypted configuration from file
    encrypted_config = load_config(protected_filename)
    # Decrypt the configuration data
    decrypted_config = decrypt_config_data(encrypted_config, key)
    # Save the decrypted configuration in a new file
    save_config(decrypted_config, unprotected_filename)
    print(f"Configuration data successfully restored and saved in the file '{unprotected_filename}'")
