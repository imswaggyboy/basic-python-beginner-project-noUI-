name = input("Enter your name: ") #the user will enter their name 
print(f"Welcome To Madlib, {name}!") #here i used the f string to concatenate with the name variable

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb = input("Verb: ")
famous_person = input("famous person name: ")

madlib = f"Computer programming is so {adj}, I like to {verb1}, \
stay hyderated and {verb} like a {famous_person}"

print(madlib)
