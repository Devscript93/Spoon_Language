spoon = [
    "        _________",
    "     .-'         `-.",
    "   .'                 `.",
    "  /                     \\",
    " |                       |",
    " |                       |",
    "  \\                     /",
    "   `.                 .'",
    "     `-.___________.-'",
    "              ||",
    "              ||",
    "              ||",
    "              ||",
    "              ||",
    "              ||",
    "              ||",
    "              ||",
    "              ||",
    "              ||",
    "              ||",
    "         Spoon Language",
]

for line in spoon:
    print(line)




print("Text verlöffelen enter 1, Text entlöffeln enter 2", end="")
onetwo = int(input(": "))

print("enter your text :", end="")
text = input()

vokale = "aeiouAEIOU"

if onetwo == 1:
    
    for char in text:
        if char in vokale:
            print(char + "v" + char, end="")
        else:
            print(char, end="")

elif onetwo == 2:
    
    i = 0
    while i < len(text):
        char = text[i]
        if (
            char in vokale
            and i + 2 < len(text)
            and text[i + 1] == "v"
            and text[i + 2] == char
        ):
            print(char, end="")
            i += 3  
        else:
            print(char, end="")
            i += 1

else:
    print("Invalid choice")
