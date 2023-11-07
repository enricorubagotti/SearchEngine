import os
import csv
import PyPDF2
import sys

def circular_shifts(word, K):
    """Generate all circular shifts of length K for a given word."""
    shifts = []
    n = len(word)
    for i in range(n):
        shift = word[i:] + word[:i]
        if len(shift) >= K:
            shifts.append(shift[:K])
    return shifts

# Define the directory path
directory_path = sys.argv[1]

# Create an empty list to store the processed data
processed_data = []

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    # Only process PDF files
    if filename.endswith('.pdf'):
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)
        
        # Open the PDF file and read the content
        with open(file_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                content = page.extract_text()
                
                # Process the content into an array with three columns
                words = content.strip().split()
                for position, word in enumerate(words):
                    # Generate circular shifts of length K (assume K=3 for now)
                    shifts = circular_shifts(word, 3)
                    
                    for shift in shifts:
                        processed_data.append([shift, filename, position])

# Sort the processed data based on the first column
processed_data.sort(key=lambda x: x[0])

# Write the sorted data into a CSV file
with open('sorted_processed_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['CircularShift', 'FileName', 'Position'])  # Header
    writer.writerows(processed_data)
