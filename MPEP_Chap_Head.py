#This is a memorization game that has all the MPEP Chapter headings inside and will randomly quiz you on a specific chapter heading. There are three difficulty levels:
#1. Beginner - Two words are randomly missing from each title and the rest are given
#2. Intermediate - Only two words are given from each title and the rest are randomly missing
#3. Expert - No hints are given and you must write out the entire chapter heading on your own

import random

chap_heading_dict = {'Chapter 100': "Secrecy, Access, National Security, and Foreign Filing", 
                     'Chapter 200': "Types and Status of Application; Benefit and Priority Claims", 
                     'Chapter 300': "Ownership and Assignment", 
                     'Chapter 400': "Representative of Applicant or Owner", 
                     'Chapter 500': "Receipt and Handling of Mail and Papers", 
                     'Chapter 600': "Parts, Form, and Content of Application", 
                     'Chapter 700': "Examination of Applications", 
                     'Chapter 800': "Restriction in Applications Filed Under 35 U.S.C. 111; Double Patenting", 
                     'Chapter 900': "Prior Art, Classification, and Search",
                     'Chapter 1000': "Matters Decided by Various U.S. Patent and Trademark Office Officials", 
                     'Chapter 1100': "Statutory Invention Registration (SIR); Pre-Grant Publication (PGPub) and Preissuance Submissions", 
                     'Chapter 1200': "Appeal", 
                     'Chapter 1300': "Allowance and Issue", 
                     'Chapter 1400': "Correction of Patents", 
                     'Chapter 1500': "Design Patents",
                     'Chapter 1600': "Plant Patents",
                     'Chapter 1700': "Miscellaneous",
                     'Chapter 1800': "Patent Cooperation Treaty", 
                     'Chapter 1900': "Protest", 
                     'Chapter 2000': "Duty of Disclosure", 
                     'Chapter 2100': "Patentability", 
                     'Chapter 2200': "Citation of Prior Art and Ex Parte Reexamination of Patents", 
                     'Chapter 2300': "Interference and Derivation Proceedings", 
                     'Chapter 2400': "Biotechnology", 
                     'Chapter 2500': "Maintenance Fees",
                     'Chapter 2600': "Optional Inter Partes Reexamination",
                     'Chapter 2700': "Patent Terms, Adjustments, and Extensions", 
                     'Chapter 2800': "Supplemental Examination", 
                     'Chapter 2900': "International Design Applications"}


#Randomly shuffle the order the chapter headings appear in 
key_list = list(chap_heading_dict)
random.shuffle(key_list)
new_chap_heading_dict = {}
for key in key_list:
    new_chap_heading_dict[key] = chap_heading_dict[key] 

#Determine difficulty of the game
difficulty = input("What level of difficulty would you like to play with? (1 = beginner, 2 = intermediate, 3 = expert)? ")

#Make sure difficulty is a valid option
if difficulty not in ["1", "2", "3"]:
    print("Sorry that is not a valid option, please type 1, 2, or 3")
else:    
    #For beginner game randomly select two words or two letters to remove from the hint
    if difficulty == "1" :
        for chapter in new_chap_heading_dict:
            #checking if the value has more than two words or not           
            if ' ' not in  new_chap_heading_dict[chapter]:
                hint = ''
                option = new_chap_heading_dict[chapter].split() 
                if len(option) == 2:
                    zero_or_one = random.randrange(len(option))
                    if zero_or_one == 0:
                        hint = f"____ {option[1]}"
                    else:
                        hint = f"{option[0]} ____ "
                else:    
                    first = random.randrange(len(new_chap_heading_dict[chapter]))
                    second = random.randrange(len(new_chap_heading_dict[chapter]))
                    hint = ''
                    #Cycle through letters and substitute the letters with dashes if necessary
                    option = new_chap_heading_dict[chapter].split() 
                    for letter in new_chap_heading_dict[chapter]:
                        if letter == new_chap_heading_dict[chapter][first] or letter == new_chap_heading_dict[chapter][second]:
                            hint += f"_"
                        else:
                            hint += f"{letter}"
                    print(hint)
            else:
                option = new_chap_heading_dict[chapter].split() 
                first = random.randrange(len(option))
                second = random.randrange(len(option))
                while second == first:
                    second = random.randrange(len(option))
                hint = ""
                #cycle through words and replace specific words with blanks if necessary
                for word in option:
                    if word == option[first] or word == option[second]:
                        hint += f'_____ '
                    else:
                        hint += f'{word} ' 
                print(hint)             
            
    #elif difficulty == 2:
    
    #else: