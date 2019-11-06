import os 
  
# Function to rename multiple files 
file=''
notExist=0
for label in os.listdir("../../Documents/data/labels/"): 
    exist=False
    for img in os.listdir("../../Documents/data/JPEGImages/"): 
        if(label[:-4]==img[:-4]):
            # exist=exist+1
            exist=True
            break
    if(exist):
        print(label + "   exist")
    else:
        print(label + "   not exist")
        notExist=notExist+1
        os.remove("../../Documents/data/labels/"+label)
print(notExist)

                