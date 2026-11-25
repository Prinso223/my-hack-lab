password = input("Enter password to check: ")

if len(password) < 8:
    print("WEAK: Too short! Use 8+ characters")
elif password.isdigit():
    print("WEAK: Only numbers! Add letters")
elif password.isalpha():
    print("MEDIUM: Only letters! Add numbers & symbols")
else:
    print("STRONG: Good password!")
