#this program opens .txt files and converts the info into question answer format for simulating taking a quiz

import os

directory = "C:/Users/dadur/Documents/PatentBarPrep"

for subdirectories, directories, files in os.walk(directory):
    if(subdirectories.startswith('C:/Users/dadur/Documents/PatentBarPrep\M')):
        for file in files:    
            length = len(file)
            if(f"{file[(length-3):]}" == 'txt'):
                with open(f'C:/Users/dadur/Documents/PatentBarPrep/{subdirectories[39:]}/{file}', 'r+') as f:
                    text = f.read()
                newtext = text.replace('© ', '').replace()

                          
        
