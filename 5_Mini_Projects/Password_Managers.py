from IPython.utils import text
from cryptography.fernet import fernet

def write_key():
  key=fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)

def load_key():
  file = open("key.key", "rb")
  key=file.read()
  file.close()
  return key

master_pwd= input("Enter your master password>> ")
key = load_key() + master_pwd.encode()
fer = fernet(key)

def view():
  with open('passwords.txt', "r") as f:
    for line in f.readlines():
      data=line.rstrip()
      user,password=data.split(" : ")
      print(f"User : {user}, Password : {fer.decrypt(password.encode()).decode()}")

def add():
  name = input("Account name: ")
  pwd=input("Password: ")

  with open('passwords.txt', 'a') as f:
    f.write(name + " : " + str(fer.encrypt(pwd.encode())) + "\n")

while True:
  mode=input("Would you like to ad a new password or view the existing ones?(add/view) ")
  if mode.lower() == "add":
    add()
  elif mode.lower() == "view":
    view()
  else:
    break
