#!/usr/bin/python3
import sys


def name_verification(name):
    if not name[0].isupper():
        raise Exception(f"Name '{name}' needs to start uppercase!")
    for letter in name:
        if not letter.isalpha():
            raise Exception(f"Name '{name}' contains an invalid character!")


if sys.stdin.isatty():
    try:
        while True:
            try:
                name = input("What's your name?\n")
                name_verification(name)
                print(f"Nice to see you {name}!")

            except Exception as e:
                print("Error:", e, file=sys.stderr)

    except KeyboardInterrupt:
        print("\nGoodbye!")

else:
    names = sys.stdin.readlines()
    for name in names:
        try:
            name_verification(name.strip())
            print(f"Nice to see you {name.strip()}!")

        except Exception as e:
            print("Error:", e, file=sys.stderr)
