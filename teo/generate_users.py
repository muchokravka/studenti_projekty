import bcrypt

meno = input("Username: ")
heslo = input("Password: ")

hash = bcrypt.hashpw(heslo.encode(), bcrypt.gensalt())

print("\nULOZ DO users.py:")
print(f'"{meno}": {hash}')