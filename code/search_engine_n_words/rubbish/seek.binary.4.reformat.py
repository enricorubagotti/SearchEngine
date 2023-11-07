import os
import csv
import sys
import pdb
import re
import ast

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

#############################################################################
#I should amend this function to use only the first column in the seek!!!!!!!
#############################################################################

def binary_search(arr, x):
    #print("I am seeking"+x)
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        #print(low)
        #print(mid)
        #print(high)
        #print("Line39_"+arr[mid])
        # If x is greater, ignore left half
        if (arr[mid] < x) and (mid<len(arr)-1):
            low = mid + 1
#            print("Line_43_"+arr[low])
 
        # If x is smaller, ignore right half
        elif ((arr[mid] > x) and  (mid>0)):
            high = mid - 1
#            print("Line_48_"+arr[high])
        # means x is present at mid
        else:
            #It prints the best results
#            print("Line_52_"+arr[mid-1])
#            print("Line_53_"+arr[mid])
#            print("Line_54_"+arr[mid+1]) 
            return mid
#    print("Line_56_"+arr[mid-1])
#    print("Line_57_"+arr[mid])
#    print("Line_58_"+arr[mid+1]) 
    return mid
 
    # If we reach here, then the element was not present
    #print(str(arr[mid])+"=" + str(x))
    #It confuses between 0 and False
    
    #x_data = ast.literal_eval(x)
    #arr_mid_data = ast.literal_eval(arr[mid])

    #if(re.search(arr_mid_data,x_data)):
    #    print(str(arr[mid]) == str(x))
    #    return mid
    #else:
    #    print(str(arr[mid]) != str(x))
    #    return "not_found"

#print("usage: seek.binary.1.py dir\n The directory should contain a single pdf file resulting from the merging of several files" )
index=[]
#It loads the indexes in memory, variable index
f = open(r'sorted_processed_data.csv', "r")
for line in f:
    index.append(line)
f.close()
#It loads the files in a dictionary as filename{file}=array of text one line, one word

#It obtain the list of all files in the page directory
#It loads them into an array
file_content={}#file_content[fileName+"_"+wordNumber]=word
freq_file_page_word_N={} #It maps the file name and the word number to the frequency

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
        #coordinates.replace("[","")
        #coordinates.replace("]","")
        coordinates_array=coordinates.split(',')
    #It opens the file and return the 5 words before and after for each occurrence
    #Assign points to each word in the text  addressed as file_name_pagenumber_word number
    #The first element is the n-grams I am seeking for
        n_gram=coordinates_array[0]
 #       print("Line_125")
        #file_content[filename64+"_"+str(i)]
        #The data should be in the format 
        #filename64 is file_page
        for i in range(1, len(coordinates_array)-1, 2):
            try:
                if freq_file_page_word_N.get(str(coordinates_array[i]+"_"+coordinates_array[i+1])) is not None:
                    freq_file_page_word_N[str(coordinates_array[i]+"_"+coordinates_array[i+1])]+=1
                else:
                    freq_file_page_word_N[str(coordinates_array[i]+"_"+coordinates_array[i+1])]=1
            except Exception as e:
                print(f'caught {type(e)}: e')


sorted_items = sorted(freq_file_page_word_N.items(), key=lambda x: x[1], reverse=True)

# Iterate over the 5 best sorted keys
j=0
# return the 5 highest score words with the context of +/- 3 words
#key is in the format file_name_word_number
#print("Line_143")
#print("File_Page_Word_Number_Context")
for key, value in sorted_items:
    j+=1
    key=key.strip()
    print(key+"_"+str(value)+"_",end='')
    #Here I should print  the word number
    #   
    try:
        file151, page151, wordN151=key.split('_')
    except Exception as e:
        print('0_0_0_0_0')
        print(key)
        print(file_content[file151+'_'+str(page151)+".txt_"+id160]+" ", end="") 

#    print()
#    print()
#    print()
#    print("Line_158_")
    for j158 in range (-5,5):
#  except Exception as e:
        #print("Line159_", end="")
        id160=str(int(wordN151)+(j158))
        try:
            if (j158!=0):
                print(file_content[file151+'_'+str(page151)+".txt_"+id160]+" ", end="")
            else:
                print(" <"+file_content[file151+'_'+str(page151)+".txt_"+id160]+">  ", end="")
        except Exception as e:
            print('0_0_0_0_0')


#       print(f'caught_156 {type(e)}: e')
    print()
#    if (j>5):
#        sys.exit()