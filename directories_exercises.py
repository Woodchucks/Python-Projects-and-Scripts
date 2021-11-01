#All essential files in in Documents\day_25\Mail Merge Project Start on personal PC

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.txt") as data:
    contents = data.read()

names = open("Input/Names/invited_names.txt", "r")
all_names = names.readlines()
for name in all_names:
    formatted_name = name.strip("\n")
    personalized_letter = contents.replace("[name]", formatted_name)
    with open(f"Output/ReadyToSend/{formatted_name}.txt", "w") as new_letter:
        new_letter.write(personalized_letter)
