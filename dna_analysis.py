# Name: Koushal S Modi
# CS 110
# Project 1: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq
# 
# This program is based on Michael Ernt's assignment on DNA Analysis 

###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys
from datetime import datetime as dt # Needed for date/time display
output = open('output.txt','w') # First open file in write mode
output.write('') # Write empty string to erase entire content from previous run
output.close() # Close file
output = open('output.txt','a') # Now open file in append mode

###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print ("You must supply a file name as an argument when running this program.")
    sys.exit(2)


# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0

print('Reading input file at:',dt.now())
for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        output.write(line) # Writing line to file without linebreak rather than storing in memory
        #seq = seq + line
print('Finished reading file:',dt.now())
output.close() # Close output file
###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
# Number of A and T nucleotides seen so far. # Problem 2a 
at_count = 0 # Problem 2a 

        

# Open file output in read mode
file = open('output.txt','r') # All data is one line
# for each base pair in the string
seq = file.readline() # Store entire line in variable seq
print('Start processing data at:',dt.now())
for bp in seq: # Loop over line char by char
    # increment the total number of bp's we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
    # next, if the bp is a A or a T, 
    elif bp == 'A' or bp == 'T': # Problem 2a 
        # increment the count of at
        at_count += 1 # Problem 2a 
# G count initialization # Problem 2b
g_count = 0 # Problem 2b
# C count initialization # Problem 2b
c_count = 0 # Problem 2b
# A count initialization # Problem 2b
a_count = 0 # Problem 2b
# T count initialization # Problem 2b
t_count = 0 # Problem 2b

for bp in seq: # Loop over line char by char # Problem 2b
     if bp == 'G':    # Problem 2b
         # increment the count of G # Problem 2b
         g_count += 1 # Problem 2b
     elif bp == 'C': # Problem 2b
         # increment the count of C # Problem 2b
         c_count += 1 # Problem 2b
     elif bp == 'A': # Problem 2b
         # increment the count of A # Problem 2b
         a_count += 1 # Problem 2b
     elif bp == 'T': # Problem 2b
         # increment the count of T # Problem 2b
         t_count += 1 # Problem 2b
        
    
         
print('Finished processing data at:',dt.now())
file.close()
# divide the gc_count by the total_count
gc_content = float(gc_count) / (g_count + c_count + a_count + t_count) # Problem 2d
# divide the at_count by the total_count
at_content = float(at_count) / (g_count + c_count + a_count + t_count) # Problem 2d

     
# Print the problem number 2e
print("Problem Number: 2e") # Problem 2e

# Print the answer for gc content and at content
print("GC-content:", round(gc_content, 12))
print("AT-content:", round(at_content, 12)) # Problem 2a 
print('G count: ', g_count) # Problem 2b # g count print
print('C count: ', c_count) # Problem 2b # c count print
print('A count: ', a_count) # Problem 2b # a count print
print('T count: ', t_count) # Problem 2b # t count print  
print('Sum count: ', g_count + c_count + a_count + t_count) # Problem 2c #individual sum
print('Total count:', total_count)    # Problem 2c #total sum
print('seq length: ', len(seq)) # Problem 2c #using len to find sum of sequence of characters
print('AT/GC Ratio:', round(at_content / gc_content, 11)) # Problem 2d #calculating AT/GT ration and rounding to 11 decimal points to match the expected output


if gc_content > 0.6:   # Problem 2e #greater than 60%, high GC content
    print('GC content: high GC content')    # Problem 2e 
elif gc_content < 0.4: # Problem 2e # less than 40%, less GS content
    print('GC content: low GC content') # Problem 2e
else:   # Problem 2e
    print('GC content: moderate GC content')    # Problem 2e # moderate for less than 60% and greater than 40%

    








