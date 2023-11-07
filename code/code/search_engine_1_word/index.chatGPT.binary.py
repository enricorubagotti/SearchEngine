import os
import csv
import PyPDF2
import sys
import re
import pdb

def circular_shifts(word, K):
    """Generate all circular shifts of length K for a given word."""
    shifts = []
    if (re.match('^[a-zA-Z]+$', word)):
        n = len(word)
        for i in range(n):
            if len(word[i:]) > 3:
                shifts.append(word[i:])
            if len(word[:i]) > 3:
                shifts.append(word[:i])
    return shifts

print("Please note if (re.match([a-zA-Z], line[0])): before")
print("It does not index numerical words, only alphabetic ones")
print("The shift is only for n-grams > 3")

# Define the directory path
directory_path = sys.argv[1]

# Create an empty list to store the processed data
processed_data = []

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    # Only process PDF files
    if filename.endswith('.pdf'):
        print("I am working on " + filename)
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)
        fileNameArray = filename.split('.')

        # Open the PDF file and read the content
        with open(file_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                content = page.extract_text()
#                print("page N=" + str(page_num))
#               print(content)
                text_file37 = directory_path + "/pages/" + fileNameArray[0] + "_" + str(page_num) + '.txt'
                with open(text_file37, 'w', newline='') as f:
                    writer = open(text_file37, "w")
                    separator = ""
                    writer.write(separator.join(str(element) for element in content))
                    writer.close()

                # Process the content into an array with three columns
                words = content.strip().split()
                for position, word in enumerate(words):
                    # Generate circular shifts of length K
                    shifts = circular_shifts(word, 12)
                    # Append shifts to processed_data
                    for shift in shifts:
                        processed_data.append([shift, str(filename[0]) + "_" + str(page_num), position])

# Sort the processed data based on the first column
processed_data.sort(key=lambda x: x[0])

# Remove duplicates by creating a new list
sorted_data = []
previous_line = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
n=0
fp=open('sorted_processed_data.csv', 'w')
for line in processed_data:
    if line[0] != previous_line[0]:
        if previous_line != "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA":
            fp.write(','.join([str(n) for n in previous_line]))
            fp.write('\n')
        previous_line = line
    else:
        # Concatenate the second and third elements
        previous_line.append(str(line[1]))
        previous_line.append(str(line[2]))
        
# Append the last line
#if previous_line is not None:
#    sorted_data.append(previous_line)

# Write the sorted data into a CSV file
#with open('sorted_processed_data.csv', 'w') as fp:
#    for item in sorted_data:
#        fp.write(','.join(str(e) for e in item) + '\n')
fp.close()