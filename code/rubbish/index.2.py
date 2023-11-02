import os
import csv
import PyPDF2
import sys
import pdb
import re
#line_6_THIS IS A TEST. MAY YOU READ ME?

def circular_shifts(word, K):
    #I am appending the direct and reverse shift
    """Generate all circular shifts of length K for a given word."""
    shifts = []
    n = len(word)
    for i in range(n):
        if(len(word[i:])>3):
            shifts.append(word[i:]) #Desde i en adelande
        if(len(word[:i])>3):
            shifts.append(word[:i]) #Desde i atras
    return shifts





print("Please note  if (re.match([a-zA-Z], line[0])):before")
print("It does not index numerical words, only alphabetic ones")
print("the shift is only for n-grams>3")

# Define the directory path
directory_path = sys.argv[1]

# Create an empty list to store the processed data
processed_data = []
sorted_data=[]

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    # Only process PDF files
    if filename.endswith('.pdf'):
        print("I am working on " + filename)
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)
        fileNameArray=filename.split('.')
        
        # Open the PDF file and read the content
        with open(file_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                content = page.extract_text()
                print("page N="+str(page_num))
                print(content)
                #Remove EOL
                #content.replace("\\n", "").replace("\\r","")
                text_file37=directory_path+"/pages/"+fileNameArray[0]+"_"+str(page_num)+'.txt'
                with open(text_file37, 'w', newline='') as f:

                    writer = open(text_file37, "w") 
                    separator=""
                    writer.write(separator.join(str(element) for element in  content))
                    writer.close()
                    #writer.writerow(separator.join(str(element) for element in  content))
                    #pdb.set_trace()

                #write the content in a file named file.page.txt
                #######################################################
                
                # Process the content into an array with three columns
                words = content.strip().split()
#                print("Line_55 words datatype is"+str(type(words)) )
                for position, word in enumerate(words):
                    # Generate circular shifts of length K
                    print("Line_58 position="+str(position)+" word="+"".join(word))
                    shifts = circular_shifts( word, 12)
                     # Write page to a file    
                    
                    for shift in shifts:
                        fileNameArray=filename.split('.')
                        processed_data.append([shift, str(filename[0])+"_"+str(page_num), position])
#                        pdb.set_trace()

# Sort the processed data based on the first column
processed_data.sort(key=lambda x: x[0])

#remove duplicates
before="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA,0,0"
buffer53=""
for line in processed_data:
    #Is the same line as before?
    #lineArray=line.split(",")
    #pdb.set_trace()
    try:
        pdb.set_trace()
        if (line[0]	== before):
            print("Line80="+str(before))
            #pdb.set_trace()
            line_1=str(line[1])
            line_2=str(line[2])
#            pdb.set_trace()
            try:
                buffer53=buffer53+","+line_1+","+line_2
                print("line_87"+str(buffer53))
            except Exception as e:
                print("Line_88_"+e)  
        else:
            if(len(buffer53)>0):
                sorted_data.append(buffer53)
            if (re.match('[a-zA-Z]', line[0])):
                before=line[0]
                buffer53=str(line)
    except Exception as e:
        print("Line_92_"+str(e))
    
#del processed_data

# Write the sorted data into a CSV file
with open('processed_data.csv', 'w') as fp:
    for item in processed_data:
        fp.write(str(item)+'\n')
fp.close()

with open('sorted_processed_data.csv', 'w') as fp:
    for item in sorted_data:
        fp.write(str(item)+'\n')
fp.close()
