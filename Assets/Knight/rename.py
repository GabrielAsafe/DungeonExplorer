#7>0
#8>1
#1>2
#2>3
#3>4
#4>5
#5>6
#6>7

#0 must be east


#7>1
#8>2
#1>3
#2>4
#3>5
#4>6
#5>7
#6>0


import os


def join_string(list_string):
 
    # Join the string based on '-' delimiter
    string = '_'.join(list_string)
    return string

directory = os.getcwd() +"\\Walk\\"
files = os.listdir(directory)

cont =1
# rename each file one by one
for file_name in files:


    extension = file_name.split(".")
    splited = file_name.split("_")
    name =str(cont) 

    if("dir8" in splited[2]):
        splited[2]= "dir2"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir1" in splited[2]):
        splited[2]= "dir3"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir2" in splited[2]):
        splited[2]= "dir4"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir3" in splited[2]):
        splited[2]= "dir5"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir4" in splited[2]):
        splited[2]= "dir6"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir5" in splited[2]):
        splited[2]= "dir7"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName) 
    elif("dir6" in splited[2]):
        splited[2]= "dir0"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir7" in splited[2]):
        splited[2]= "dir1"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)


