import os 
i=0
text=''
for filename in os.listdir('Img3/' ): 
    with open('Img3/'+filename,'r+') as file:
        array = file.readlines() 
        arr=[]
        for item in array:
            item = item.split() 
            item[0]='0'
            arr.append(' '.join(item))
        arr='\n'.join(arr)
        print(arr)
        #print(array)
        # array[0]='0'
        # text=' '.join(array) 
        # print(text) 
        #file.seek(0) 
    with open('Img3/'+filename, 'w') as f:
        f.writelines(arr)
        #file.writelines(text)