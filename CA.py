user_char = input("Enter a character: ")

if ('a' <= user_char <= 'z') or ('A' <= user_char <= 'Z'):
    print(f"'{user_char}' is an alphabet letter.")
else:
    print(f"'{user_char}' is not an alphabet letter.")