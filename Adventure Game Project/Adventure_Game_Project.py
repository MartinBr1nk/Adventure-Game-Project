PlayerName = input("Name the protagonist: ")

if PlayerName == "":
    PlayerName = input("Enter a name, otherwise a default name will be chosen: ")
    if PlayerName == "":
        PlayerName = "Stanley"
        #this is a placeholder name, I'm not actually going to steal EVERY idea from the stanley parable
        print(f"Your name is {PlayerName}.")
    else:
        print(f"Your name is {PlayerName}.")
else:
    print(f"Your name is {PlayerName}.")