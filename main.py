import json
from config_protector import hide_config_data, show_config_data

key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='

# Сховати дані конфігурації
hide_config_data(key)
# Відновити сховані дані конфігурації
show_config_data(key)


def load_config(filename='config.json'):
    # Завантажуємо конфігурацію з файлу
    with open(filename, 'r') as file:
        config = json.load(file)
    return config


def greet_user(login):
    # Привітати користувача
    print(f"Вітаємо, {login}!")


def check_password(users, max_attempts):
    # Перевірка пароля користувача
    for _ in range(max_attempts):
        password = input("Будь ласка, введіть ваш пароль: ")
        # Перевіряємо пароль для кожного користувача в списку
        for user in users:
            if password == user['password']:
                return user['login']
        # Виводимо повідомлення про невірний пароль
        print("Невірний пароль. Повторна спроба.")
    return 'Intruder'


def check_auth_code(auth_code, max_attempts):
    # Перевірка коду аутентифікації
    for _ in range(max_attempts):
        entered_code = input("Будь ласка, введіть код автентифікації: ")
        if entered_code == auth_code:
            return True
        # Виводимо повідомлення про невірний код аутентифікації
        print("Невірний код аутентифікації. Повторна спроба.")
    return False


def main():
    # Завантажуємо конфігурацію
    config = load_config()
    users = config['users']
    auth_code = config['auth_code']
    max_attempts = config['attempts']

    # Перевіряємо пароль користувача
    user = check_password(users, max_attempts)
    if user != 'Intruder':
        # Привітати користувача
        greet_user(user)
        # Перевіряємо код аутентифікації
        if check_auth_code(auth_code, max_attempts):
            greet_user(user)
        else:
            print(
                "Досягнуто максимальну кількість спроб введення коду аутентифікації. Доступ заборонено.")
    else:
        print("Досягнуто максимальну кількість спроб введення пароля. Доступ заборонено.")


if __name__ == "__main__":
    main()
