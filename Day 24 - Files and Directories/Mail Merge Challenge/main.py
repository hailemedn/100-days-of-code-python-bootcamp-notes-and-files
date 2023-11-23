# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.docx") as file:
    content = file.read()


for name in names:
    stripped_name = name.rstrip()
    new_letter = content.replace("[name]", stripped_name)
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as file:
        file.write(new_letter)
