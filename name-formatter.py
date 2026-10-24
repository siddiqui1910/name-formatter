#Name Formatter
#This is going to be a three word string. It's kind of hardcoded because I cannot apply loops. This code works for any three word string.
name = input("Enter the name: ") 
formatted = name.title()
print("The name is: ", formatted)
word = formatted.split()
initials_list = [word[0][0], word[1][0], word[2][0]]
initials = ".".join(initials_list)
print("The initials are: ", initials)