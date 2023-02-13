# This file contians the code for creating the chapter heading games and study aides. The actual content of the files isn't included due to potential copyright issues but
# could be modified to work with files containing chapter summaries like those mentioned in this file i.e. Chap_1_summary.py. 

#words not to remove: a, and, for, which, to, an, or, if, of, be, that, is, as, was, in, this, the, on, had, was, its, too, may, shall, <=3 characters

import random

do_not_remove = ['a', 'and', 'are', 'for', 'which', 'to', 'an', 'or', 'if', 'of', 'be', 'that', 'is', 'as', 'was', 'in', 'this', 'the', 'on', 'had', 'was', 'its', 'too','may', 'shall']

chapter = input("What chapter would you like to study? (1-29): ")
file_name = f"C:/Users/dadur/Documents/Github/patent_bar_chapter_files/Chap_{chapter}_Summary.py"

separated_file = []

with open(file_name) as file:
    lines = file.readlines()
    for line in lines:
        separated_file.append(line)
separated_file.pop(0)
separated_file.pop(-1)

sections_to_memorize = {}
section_name = ""
for section in separated_file:
    if(section[0:3].isdigit()):
        section_name = section.strip() 
        sections_to_memorize[section_name] = []
    else:
        sections_to_memorize[section_name].append(section.strip())

#Study Mode: No randomization. Only one or two words missing per line
hint = ''
for key in sections_to_memorize:
    print('\n')
    print(f'Section to Study: {key}')
    print(f'Complete the following sentences-')
    #print(type(sections_to_memorize[key]))
    for item in sections_to_memorize[key]:
        option = item.split()    
        if len(option) == 0:
            hint = ''
            continue
        else:    
            first = random.randrange(len(option))
            while option[first] in do_not_remove:
                first = random.randrange(len(option))
            #cycle through words and replace specific words with blanks if necessary
            for word in option:
                if word == option[first]:
                    hint += f'_____ '
                else:
                    hint += f'{word} ' 
            guess = input(f'Your hint is:\n {hint}\n')
                
            if guess != item:
                print(f'Sorry "{guess}" is not the correct answer, the correct answer is "{item}"')
            else:
                print(f"That's correct! '{guess}' is the correct answer.")
            #without this line hint is printed out including all the previous clues. 
            hint = ''



