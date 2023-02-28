#This program cycled through a large number of png files and converted them to text files for further manipulation. 


import cv2
import pytesseract
import os

directory = "C:/Users/dadur/Documents/PatentBarPrep"

for subdirectories, directories, files in os.walk(directory):
    if(subdirectories.startswith('C:/Users/dadur/Documents/PatentBarPrep\M')):
        #print(subdirectories[39:])
        for f in files:
            # Load the image file
            img = cv2.imread(f"C:/Users/dadur/Documents/PatentBarPrep/{subdirectories[39:]}/{f}")

            # Preprocess the image
            try:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                #Selecting download directory for pytesseract
                pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

                #Extract text using Pytesseract
                text = pytesseract.image_to_string(gray)

                #Print the extracted text
                with open(f'C:/Users/dadur/Documents/PatentBarPrep/{subdirectories[39:]}/{f[:-3]}txt', 'w') as file: 
                    file.write(text)
            except:
                print(f"C:/Users/dadur/Documents/PatentBarPrep/{subdirectories[39:]}/{f} failed!")
                

