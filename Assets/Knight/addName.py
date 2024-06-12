import os


def join_string(list_string):
    # Join the string based on '-' delimiter
    string = '_'.join(list_string)
    return string

directory = os.getcwd() +"\\Jump\\"
files = os.listdir(directory)
# rename each file one by one
for file_name in files:
    extension = file_name.split(".")
    splited = file_name.split("_")

    #print(splited)

    if "dir" in splited[2]:
        #splited[2]= "dir5"+'.' +extension[1]
        

        splited[2] = splited[2].removesuffix("." + extension[1])
        splited[2] = splited[2] + "0" +"."+extension[1]
        newName = join_string(splited)
        print(newName)
        
        os.rename( directory+file_name,directory+newName)
        
