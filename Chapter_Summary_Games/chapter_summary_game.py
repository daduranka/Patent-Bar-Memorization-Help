# This file contians the code for creating the chapter heading games and study aides. The actual content of the files isn't included due to potential copyright issues but
# could be modified to work with files containing chapter summaries like those mentioned in this file i.e. Chap_1_summary.py. 

#words not to remove: a, and, for, which, to, an, or, if, of, be, that, is, as, was, in, this, the, on, had, was, its, too, may, shall, <=3 characters

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

print(sections_to_memorize)
