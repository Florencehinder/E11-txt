import re

def convert_text(text):
    # Split the text into lines
    lines = text.split('\n')

    # Split each line into sentences
    sentences = []
    for line in lines:
        sentences.extend(re.split(r'(?<=[.!?])\s+', line))

    # Remove empty sentences
    sentences = [sentence for sentence in sentences if sentence.strip()]

    # Save sentences to a file
    with open("sentences.txt", "w") as output_file:
        for sentence in sentences:
            output_file.write(sentence + '\n')

# Provide the correct file path here
file_path = '/Users/florencehinder/Documents/GitHub/react-listen-n-read/reactapp-listen-n-read/public/SocialBehavior/SocialBehavior.txt'

with open(file_path, 'r') as file:
    text = file.read()

# Call the function to convert and save the sentences to the file
convert_text(text)
