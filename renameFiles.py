import os 
import itertools  

# Function to rename multiple files 
j=6849
x=0
y=0
path="data/"
for filename in os.listdir(path): 
    if(filename[-3:]=='jpg'):
        src ='data/'  + filename 
        dst ='data/' + "0000" + str(j) + ".jpg"
        os.rename(src, dst)
        print(src)
        j=j+1


        