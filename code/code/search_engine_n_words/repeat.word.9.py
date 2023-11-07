import subprocess
import re
import sys
import os
import csv
#import numpy as np
#Import the coordinates of the word
directory_path='/home/ubuntu/search_engine/pdf/pages/'
file_content={}#{} #file_content[fileName][wordNumber]=word
moving_average_length=5
for filename64 in os.listdir(directory_path):
    #open the file
    filename64_handle=open(directory_path+filename64)
    content=filename64_handle.read()
    filename64_handle.close()
    words = content.strip().split() #This is an array
    for i in range(0,len(words),1):
        if filename64 not in file_content:
            file_content[filename64] = {}
        else:
            file_content[filename64][str(i)]=words[i]
    #load it in a hash
os.remove("out")
f = open("out", "a")

for i in range(1, len(sys.argv)):
    subprocess.call(['python3', 'seek.binary.5.reformat.py', str(sys.argv[i])], stdout=f)
    print("I am executing"+str(sys.argv[i]))
f.close()

#Remove empty lines

with open( 
    "out", 'r') as r, open( 
        'out.clean', 'w') as o: 
      
    for line in r: 
        #strip() function 
        if line.strip(): 
            o.write(line) 
o.close()

csv_file_path = 'out.clean'
tabular_result=[]
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file,delimiter='_')
    for row in csv_reader:
        row.append(0)
        row.append(0)
        tabular_result.append(row)

sorted_data = sorted(tabular_result, key=lambda x: (x[0], x[1], x[2] ))
file_before=-1
page_before=-1
word_before=-1
point_before=-1
sixBefore=0 #It stores the number of times this line was hit
for row in  sorted_data:
    #Remove the '' around the numeric data
    row[0]=float(row[0].strip('\''))
    row[1]=float(row[1].strip('\''))
    row[2]=float(row[2].strip('\''))
    row[3]=float(row[3].strip('\''))
    #is the same file of before?
    if (int(row[0]) != file_before):
        file_before=int(row[0])
        page_before=int(row[1])
        word_before=int(row[2])
        point_before=int(row[5])
        sixBefore=0
    #is the same page of before?
    elif (int(row[1]) !=  page_before ):
        file_before=int(row[0])
        page_before=int(row[1])
        word_before=int(row[2])
        point_before=int(row[5])
        sixBefore=0
    #Is it near the last word?
    elif ((int(row[0]) == file_before) and (int(row[1]) ==  page_before) and ((word_before-int(row[2]))<5) and (row[0]!=0) and (row[1]!=0) and row[2]!=0):
    #    print("Line_78_Bingo!!! at line "+row[4])
        if (word_before-row[2]!=0):
            row[5]=float(point_before)+float(abs(row[3]/(word_before-row[2])))
            row[6]=sixBefore+1
        else:
            row[5]=float(point_before)+float(abs(row[3]))
            row[6]=sixBefore+1
        
sixBefore=row[6]
word_before=int(row[2])
        
#    print(row)
sorted_data_by_point = sorted(tabular_result, key=lambda x: (x[6],x[5]), reverse=True )

for row in  sorted_data_by_point:
    print(row)



'''
#It imports the data into an array
I CANNOT USE ARRAYS!!!!!
CSVData = open("out.clean")
#Sort the data by file(0), page(1), word(2)

b = np.genfromtxt(CSVData, delimiter="_")
b = b[b[:, 2].argsort()]  # sort by day
b = b[b[:, 1].argsort(kind='mergesort')]  # sort by month
b = b[b[:, 0].argsort(kind='mergesort')]  # sort by year
np.set_printoptions(threshold=np.inf)
print(np.matrix(b))
'''
'''
tabular_result=[]
tabular_result = [[float(0) for j in range(3)] for i in range(2000)]

line_n_out=0

for line in f:
    line = line.rstrip()
    elements = line.split("_")
    if len(elements) == 5:
        tabular_result.append([float(elements[0]), float(elements[1]),float(elements[2]),float(elements[3]),str(elements[4]),float(0)])
    else:
        print("Line43_The line "+line+"does not have 5 fields!!!!!!")
    line_n_out += 1
# Sort the data based on the first column (index 0)
sorted_data = sorted(tabular_result, key=lambda x: (x[0],x[1],x[2]))
#Will te problem be here?

#Print for debugging reason
count_i=0
for i in sorted_data:
    count_j =0
    for j in i:
#        print(j, end="_")
        #stores the moving average  in the last field!!!! if it is more than sum length query joins the sentences previous file,page, word number, and 
        #it calculates the average
        if (count_j==5):
            for diff60 in range(max([0,count_i-moving_average_length]),min(len(sorted_data)-1,count_i+5)):#This section is to include
                sorted_data[count_i][5]+=sorted_data[diff60][3]
        count_j+=1
    count_i+=1
    print(count_i)
    print(i)
#    print()
'''
'''
#sort by score

sorted_by_score = sorted(sorted_data, key=lambda x: x[5])

#How to highlight queries.....??????

for i in sorted_by_score:
    for j in i:
        print(j, end="_")
    print()

'''




'''
# Calculate the sum of matches in the +/5 
lineN=0
for item in sorted_data:
    #sorted_data[2][lineN]=0
    if (lineN<5):
        for j in range(0,lineN+1):
            if (j!=0):
                sorted_data[lineN][2]+=float(sorted_data[lineN+j][1]/(abs(j)+1))
            else:
                sorted_data[lineN][2]+=float(sorted_data[lineN+j][1])
    elif (len(sorted_data)<lineN+5):
        for j in range(0,len(sorted_data)-lineN):
            if(j!=0):
                sorted_data[lineN][2]+=float((sorted_data[lineN+j][1])/(abs(j)+1))
            else:
                sorted_data[lineN][2]+=float(sorted_data[lineN+j][1])
    else:
        for j in range(-5,5):
            if(j!=0):
                sorted_data[lineN][2]+=float((sorted_data[lineN+j][1])/(abs(j)+1))
            else:
                sorted_data[lineN][2]+=float(sorted_data[lineN+j][1])
    lineN+=1

#It sorts by the third column, containing the score 

sorted_by_score = sorted(sorted_data, key=lambda x: x[2], reverse=True)

#subprocess.run('sort -k 2 -r /home/ubuntu/search_engine/code/out >> out.sorted')
#Print the 10 best results
printN=0
for key, value, score  in sorted_by_score:
    print("key="+str(key)+" value="+str(value)+"score="+str(score))
    #print the +/-5 from the point
    printN+=1
    #if (printN>10):
    #    break


#It loads the file into an array


#It sorts by the word number the array
#sorted_tabular_data = sorted(tabular_result, key=lambda x: x[0])

#The third column is the weighted sum of the second column in the 5 previous and next position
#for line in results:
#sort by the third column

#print the results and the previous 5 and next 5 words

#import subprocess
#import re
#import sys

# Run the script and capture its output
#result = []
#for i in range(1, len(sys.argv)):
#    process = subprocess.run(['python3', 'seek.binary.position.2.py', str(sys.argv[i]), stdout=subprocess.PIPE, text=True, check=True])
#    result.append(process.stdout)
#result=[]
#for i in range(1, len(sys.argv)):
#    result.extend(subprocess.run(['python3', 'seek.binary.position.2.py '+str(sys.argv[i])+' >> out'], stdout=subprocess.PIPE, text=True))    
#Read into a bidimensinal array results

#Now all results are in the 2-d array tabular_result 
#tabular_result.sort(reverse=True)

#Calculate the array of distances

'''