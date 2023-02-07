import bcrypt

password = input("enter password")

# converting password to array of bytes
bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
# Hashing the password
hash = bcrypt.hashpw(bytes, salt)

print("password hashed")
print(salt)

# Taking user entered password
userPassword = input("enter again")

# encoding user password
userBytes = userPassword.encode('utf-8')

# checking password
result = bcrypt.checkpw(userBytes, hash)

print(result)

# bcrypt password contains the original salt after hashed
