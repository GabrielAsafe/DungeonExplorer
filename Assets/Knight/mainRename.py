"""
Supostamente ele muda os nomes das imagens 

"""
import os


#get current directory
directory = os.getcwd()
#get the folders
files = os.listdir(directory)
finalFolder=[]
correlacao = {
        "dir60":"dir0",
        "dir70":"dir1",
        "dir80":"dir2",
        "dir10":"dir3",
        "dir20":"dir4",
        "dir30":"dir5",
        "dir40":"dir6",
        "dir50":"dir7"
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
               
            


def addZeroToName(finalFolders,name):
        currentFolder = os.listdir(finalFolders)
        for file_name in currentFolder:
            extension = file_name.split(".")#split the strind on .
            splited = file_name.split("_")#split the strind on _

            if "dir" in splited[2]:
                splited[2] = splited[2].removesuffix("." + extension[1])
                splited[2] = splited[2] + "0" +"."+extension[1]
                newName = join_string(splited)
                #print(newName)
                #print(name+"\\"+file_name,name+"\\"+newName)
                os.rename(name+"\\"+file_name,name+"\\"+newName)  


def rename(finalFolders,name):
    
    currentFolder = os.listdir(finalFolders)
    for file_name in currentFolder:
        
        extension = file_name.split(".")
        splited = file_name.split("_")
       
       
        for x in correlacao.keys():
            if x in str(splited[2]):
                splited[2]= correlacao[x]+'.' +extension[1]
                newName = join_string(splited)
                print(newName)
                #print(directory+file_name,directory+newName)
                os.rename(name+"\\"+file_name,name+"\\"+newName)  
                break;
        




def main():
    for file in files:
        if "." in file:
            extension = file.split(".")#split the strind on .
            if "py" in extension[1]:
                continue
        finalFolder.append( directory +"\\"+ file+"\\")

   
    for items in finalFolder:
        name = items
        #addZeroToName(items,name)

    for items in finalFolder:
        name = items
        rename(items,name)
       
##    for items in finalFolder:
##        nome = items
##        RemoveImportFiles(items, nome)



       
if __name__ == "__main__":
    main()
    
