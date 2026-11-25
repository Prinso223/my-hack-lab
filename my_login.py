import hashlib, secrets

# We go create user
print("=== CREATE ACCOUNT ===")
username = input("Choose username: ")
password = input("Choose password: ")

salt = secrets.token_hex(8)
hashed = hashlib.sha256((password + salt).encode()).hexdigest()

print(f"Account created for {username}!")
print(f"We no save your password, we save hash + salt only")

print("\n=== LOGIN NOW ===")
try_username = input("Username: ")
try_password = input("Password: ")

try_hash = hashlib.sha256((try_password + salt).encode()).hexdigest()

if try_username == username and try_hash == hashed:
    print("✅ LOGIN SUCCESS! Welcome hacker!")
else:
    print("❌ LOGIN FAILED! Wrong username or password")
