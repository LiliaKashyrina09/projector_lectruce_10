file_1 = open("text_1.txt", "r") 

file_2 = open("text_2.txt", "w") 
  
for line in file_1: 
    file_2.write(line.upper())   