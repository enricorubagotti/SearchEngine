import os
import csv
import sys
import pdb
import re
import ast

#############################################################################
#I should amend this function to use only the first column in the seek without [ or ]!!!!!!!
#############################################################################
def circular_shifts(word, K):
    #I am appending the direct and reverse shift
    """Generate all circular shifts of length K for a given word."""
    shifts = []
    n = len(word)
    for i in range(n):
        shifts.append(word[i:]) #Desde i en adelande
        shifts.append(word[:i]) #Desde i atras

    return shifts


def binary_search(arr, x):
    x=r'[\''+x
    print(x)
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if ((arr[mid] < x) and ((mid<len(arr)-1))):
            low = mid + 1
            print("The new low is"+str(arr[low]))
        # If x is smaller, ignore right half
        elif ((arr[mid] > x) and (mid>0)):
            high = mid - 1
            print("The new high is"+str(arr[high]))
        # means x is present at mid
        else:
            return mid
            print("match="+str(arr[mid]))
    # If we reach here, then the element was not present
    #print(str(arr[mid])+"=" + str(x))
    #It confuses between 0 and False
    x_data = ast.literal_eval(x)
    arr_mid_data = ast.literal_eval(arr[mid])
    if( re.search(arr_mid_data,x_data) ):
        print(str(arr[mid])+' == '+ str(x))
        return mid
    else:
        print(str(arr[mid])+'!='+str(x))
        return "not_found"

index=[]
#It loads the indexes in memory, variable index
f = open("sorted_processed_data.csv", "r")
for line in f:
    index.append(line)
#It loads the files in a dictionary as filename{file}=array of text one line, one word

#It obtain the list of all files in the page directory
#It loads them into an array
file_content={}
freq_file_page_word_N={} #It maps the file name to the array of words it contains

directory_path='/home/ubuntu/search_engine/pdf/pages/'
for filename64 in os.listdir(directory_path):
    #open the file
    filename64_handle=open(directory_path+filename64)
    content=filename64_handle.read()
    filename64_handle.close()
    words = content.strip().split() #This is an array
    for i in range(0,len(words),1):
        file_content[filename64+"_"+str(i)]=words[i]
    #load it in a hash


#It seeks all circular variation of a word and returns a dictionary as file_lineN;frequency
variations=circular_shifts(sys.argv[1],12)

#File Name:
# /home/ubuntu/search_engine/pdf/pages/1.pdf_8.txt
# Index standard: 
#['IV/AIDSH', '1_7', 120],1_7,155,1_7,181,1_7,207,1_7,237,1_7,260,1_7,289,1_7,320,1_38,727,1_43,281,1_44,10,1_44,103,1_45,191
#[subword, file_pagenumber, word_number],file_pagenumber1, word_number1, file_pagenumber2, word_number2,
# file_pagenumber3, word_number3  

for variation in variations:
    #Is this variation present in the list?
    find1 =binary_search(index,variation)
    if ( find1 != "not_found"):
        #It should be a number
        #Seek the word in the file and print it out
        
        coordinates=index[find1]
        coordinates.replace("[","")
        coordinates.replace("]","")
        coordinates_array=coordinates.split(',')
    #It opens the file and return the 5 words before and after for each occurrence
    #Assign points to each word in the text  addressed as file_name_pagenumber_word number
    #The first element is the n-grams I am seeking for
        n_gram=coordinates_array[0]
        for i in range(1, len(coordinates_array)-1, 2):
            if freq_file_page_word_N.get(str(coordinates_array[i]+"_"+coordinates_array[i+1])) is not None:
                freq_file_page_word_N[str(coordinates_array[i]+"_"+coordinates_array[i+1])]+=1
            else:
                freq_file_page_word_N[str(coordinates_array[i]+"_"+coordinates_array[i+1])]=1


sorted_items = sorted(freq_file_page_word_N.items(), key=lambda x: x[1], reverse=True)

# Iterate over the 5 best sorted keys
j=0
# return the 5 highest score words with the context of +/- 3 words
#key is in the format file_name_word_number
range=5
for key, value in sorted_items:
    #Which file is it?
    file_name, word_n=key.split(',')

    #Which word is it?
    for i in range(-range,+range,1):
        print(file_name)
        print(file_content[file_name+"_"+str(word_n+i)],end=' ')
    print()
    print()
    if (j>5):
        sys.exit()
    j+=1






#################################################################################
######I AM WORKING HERE !!!!!!###################################################
#################################################################################



  

