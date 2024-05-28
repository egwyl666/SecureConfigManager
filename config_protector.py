import json
from cryptography.fernet import Fernet

# Функція для завантаження конфігурації з файлу


def load_config(filename='config.json'):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config

# Функція для збереження конфігурації у файл


def save_config(config, filename='unprotected_config.json'):
    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)

# Функція для шифрування даних конфігурації


def encrypt_config_data(config, key):
    # Створюємо об'єкт Fernet з використанням ключа
    fernet = Fernet(key)
    encrypted_config = {}
    # Шифруємо логіни та паролі кожного користувача в конфігурації
    for user in config['users']:
        encrypted_login = fernet.encrypt(user['login'].encode()).decode()
        encrypted_password = fernet.encrypt(user['password'].encode()).decode()
        encrypted_user = {'login': encrypted_login,
                          'password': encrypted_password}
        encrypted_config['users'] = encrypted_config.get(
            'users', []) + [encrypted_user]
    return encrypted_config

# Функція для дешифрування даних конфігурації


def decrypt_config_data(encrypted_config, key):
    # Створюємо об'єкт Fernet з використанням ключа
    fernet = Fernet(key)
    decrypted_config = {'users': []}
    # Дешифруємо логіни та паролі кожного користувача в конфігурації
    for user in encrypted_config['users']:
        decrypted_login = fernet.decrypt(user['login'].encode()).decode()
        decrypted_password = fernet.decrypt(user['password'].encode()).decode()
        decrypted_user = {'login': decrypted_login,
                          'password': decrypted_password}
        decrypted_config['users'].append(decrypted_user)
    return decrypted_config

# Функція для приховування даних конфігурації шляхом їх шифрування та збереження в новому файлі


def hide_config_data(key, config_filename='config.json', protected_filename='protected_config.json'):
    # Завантажуємо конфігурацію з файлу
    config = load_config(config_filename)
    # Шифруємо дані конфігурації
    encrypted_config = encrypt_config_data(config, key)
    # Зберігаємо зашифровану конфігурацію у новому файлі
    save_config(encrypted_config, protected_filename)
    print(
        f"Дані конфігурації успішно захищено та збережено у файлі '{protected_filename}'")

# Функція для відображення даних конфігурації шляхом їх дешифрування та збереження у новому файлі


def show_config_data(key, protected_filename='protected_config.json', unprotected_filename='unprotected_config.json'):
    # Завантажуємо зашифровану конфігурацію з файлу
    encrypted_config = load_config(protected_filename)
    # Розшифровуємо дані конфігурації
    decrypted_config = decrypt_config_data(encrypted_config, key)
    # Зберігаємо розшифровану конфігурацію у новому файлі
    save_config(decrypted_config, unprotected_filename)
    print(
        f"Дані конфігурації успішно відновлено та збережено у файлі '{unprotected_filename}'")
