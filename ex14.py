from sys import argv

script, user_name = argv
prompt = 'Your anwser is... '

print(f"Hello {user_name}, I'm {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you want buy?")
computer = input(prompt)

print(f"""
Well, so you said {likes} about liking me.
You live in {lives}. Not sure where it is.
And you want to buy {computer}.
But I guess, you don't have enough money, lol lol.
""")
