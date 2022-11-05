import string, secrets

chrs = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter the length of ur password (length >= 10): "))

while length <= 10:
    print("Password must be greater than 10")
    length = int(input("Enter the length of ur password (length >= 10): "))

password = ''.join(secrets.choice(chrs) for i in range(length+1))

print(password)