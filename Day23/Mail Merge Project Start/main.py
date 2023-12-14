#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []

with open('./Input/Names/invited_names.txt') as f:
    for line in f:
        strip_line = line.strip()
        names.append(strip_line)


def write():
    index = 0
    with open('./Inout/Letters/starting_letter.txt') as f:
        for line in f:
            line.replace("[name]", names[index])

