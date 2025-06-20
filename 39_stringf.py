name = "The easylearn Academy"

print(f"Welcome to {name}!")
print("length is",len(name))
print("isalnum",str.isalnum(name))

print("isalpha",str.isalpha(name))
print("islower",str.islower(name.lower()))
print("isupper",str.isupper(name.upper()))
print("isnumeric",str.isnumeric(name))
print("isspace",str.isspace(name))
print("istitle",str.istitle(name.title()))
list = ["India","usa","UK","Canada","Australia"]
s = ","
print (s.join(list))
name = "The easylearn Academy"
print("replace",name.replace('e','E',1))
alphabets = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9"
print("-".join(alphabets))
print(str.split(alphabets,sep=" "))
print(str.split(name))