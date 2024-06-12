import os


#get current directory
directory = os.getcwd()
#get the folders
files = os.listdir(directory)
finalFolder=[]
correlacao = {
        "dir00":"a",
        "dir01":"c",
        "dir02":"b",
        "dir03":"v",
        "dir04":"d",
        "dir05":"s",
        "dir06":"t",
        "dir07":"aas"
}



def join_string(list_string):
    # Join the string based on '-' delimiter
    string = '_'.join(list_string)
    return string


def RemoveImportFiles(finalFolders,nome):
        currentFolder = os.listdir(finalFolders)


        for file_name in currentFolder:
            extension = file_name.split(".")#split the strind on .
            if "import" in extension:

                print(file_name)
                #print(nome+"\\"+file_name)
                #os.remove(nome+"\\"+file_name)
                break;
               
            


def addZeroToName(finalFolders):
        currentFolder = os.listdir(finalFolders)
        for file_name in currentFolder:
            extension = file_name.split(".")#split the strind on .
            splited = file_name.split("_")#split the strind on _
            print(splited)
        if "dir" in splited[2]:
            splited[2] = splited[2].removesuffix("." + extension[1])
            splited[2] = splited[2] + "0" +"."+extension[1]
            newName = join_string(splited)
            print(newName)
            
            #os.rename( directory+file_name,directory+newName)    


def rename(finalFolders):
    
    currentFolder = os.listdir(finalFolders)
    for file_name in currentFolder:
        
        extension = file_name.split(".")
        splited = file_name.split("_")
       
       
        for x in correlacao.keys():
            if(str(x) in splited[2]):
                #splited[2]=  correlacao[x]+'.' +extension[1]
                #newName = join_string(splited)
                #print(newName)
                break;
            print(x)
            print(splited[2])


def main():
    for file in files:
        if "." in file:
            extension = file.split(".")#split the strind on .
            if "py" in extension[1]:
                continue
        finalFolder.append( directory +"\\"+ file+"\\")

    print(finalFolder)
    #for items in finalFolder:
    #    addZeroToName(items)

    for items in finalFolder:
       rename(items)
       print("fim da pasta")

##    for items in finalFolder:
##        nome = items
##        RemoveImportFiles(items, nome)



       
if __name__ == "__main__":
    main()
    
