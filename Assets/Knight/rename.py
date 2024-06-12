#7>0
#8>1

#1>2
#2>3
#3>4
#4>5
#5>6
#6>7

import os


def join_string(list_string):
 
    # Join the string based on '-' delimiter
    string = '_'.join(list_string)
    return string

directory = os.getcwd() +"\\Jump\\"
files = os.listdir(directory)

cont =1
# rename each file one by one
for file_name in files:


    extension = file_name.split(".")
    splited = file_name.split("_")
    name =str(cont) 

##    if cont <7:
##        if ( "dir" + name in splited[2]):
##            if cont <7:
##                cont+=1
##            name = str(cont)
##            splited[2]= "dir"+name+'.' +extension[1]
##            newName = join_string(splited)
##            print(newName)
            #os.renameame(file_name, newName)

    
    if("dir10" in splited[2]):
        splited[2]= "dir2"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir20" in splited[2]):
        splited[2]= "dir3"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir30" in splited[2]):
        splited[2]= "dir4"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir40" in splited[2]):
        splited[2]= "dir5"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir50" in splited[2]):
        splited[2]= "dir6"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir60" in splited[2]):
        splited[2]= "dir7"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName) 
    elif("dir70" in splited[2]):
        splited[2]= "dir0"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)
    elif("dir00" in splited[2]):
        splited[2]= "dir1"+'.' +extension[1]
        newName = join_string(splited)
        print(newName)
        os.rename( directory+file_name,directory+newName)


