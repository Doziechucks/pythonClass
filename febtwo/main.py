import bcrypt

CRYPTIC = "encrypted.txt"


def hash_password(password):
    salt = bcrypt.gensalt()
    mybytes = password.encode('utf-8')
    return bcrypt.hashpw(mybytes, salt)


def register_user():
    while True:
        username = input("Enter your username: ")
        if not username:
            print("username cannot be empty.")
            continue
        break

    while True:
        password = input("Enter your password: ")
        if not password:
            print("Invalid password. ")
            continue
        break

    save_to_file(username, password)

def save_to_file(username, password):
    with open(CRYPTIC, 'a') as file:
        file.write(f'{username} : {hash_password(password)}\n')


def validate_user(username, password):
    with open(CRYPTIC, 'r') as file:
        data = file.read()
        for line in data.split("\n"):
            if line:
                stored_username, stored_password = line.split(":")
                if stored_username == username:
                    return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
    return False


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if validate_user(username, password):
        print("login successful")
    else:
        print("login not successful")


def main():
    menu = """
    1 to register
    2 to login user
    3 to exit
    """
    choice = int(input(menu))

    match choice:
        case 1:
            register_user()
        case 2:
            login()
        case 3:
            pass


main()
