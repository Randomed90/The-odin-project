name = input("What's your name?: ")

print(f"\nhello, {name} how are you doing today?")

response = input("""Options: [Type "good" for good] [Type "bad" for bad]\n""")

if response == "good":
    print("\nThat's great!, I hope you continue to have a good day!\n")
else:
    print("\nOh, keep your chin up and don't give up! o7\n")
