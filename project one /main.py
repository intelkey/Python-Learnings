'''
1. Smart Name Greeter (A2 – Input + String Formatting)
User ka naam lo aur different greetings generate karo using string formatting
'''

a = input("write your name: ", )
b = (a.strip())
c = (b.title())
print(f"Hello {c}")
print(f"Good morning {c}")
print(f"Nice to meet you {c}")
print(f"How are you doing {c}")


# ⚙️ ──[ MORE CLEANER VERSION ]────────────────────────────────── ⚙️

clean_version = input("write your name ", ).strip().title()
print(f"Hello {clean_version}")
print(f"Good morning {clean_version}")
print(f"Nice to meet you {clean_version}")
print(f"How are you doing {clean_version}")


# ⚙️ ──[ MORE ADVANCED VERSION ]────────────────────────────────── ⚙️
variable = input("Enter your name ", ).strip().title()
greetings = ["Hello", "Good Morning", "Nice to meet you", "How are you doing"]
for message in greetings:
    print(f"{message} {variable}")
