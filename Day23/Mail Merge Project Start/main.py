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
    with open('./Input/Letters/starting_letter.txt') as f:
        content = f.read()

    for name in names:
        modified_content = content.replace("[name]", name)
        output_file_name = f'./Output/ReadyToSend/{name}.txt'
        with open(output_file_name, 'w') as file:
            file.write(modified_content)

write()
