import os, shutil
#Defining the directory i want to sort
path = "C:/Users/DANIEL/Videos/HOLLYWOOD/"

#os.listdr(path) actually returns the list of items in the path, i will assign the list to a variable
listOfThingsToSort = os.listdir(path)
print(listOfThingsToSort)

#folders to create
FolderCreate = ['mkv format', 'Mp4 format', 'Srt format']

#looping thru the path to check whether we have already created a folder for it
for everything in range(3):
    #if statement to check whether we have created a folder with the names in the FolderCreate variale
    if not os.path.exists(path + FolderCreate[everything]):
        #the below makes a new folder 
        os.makedirs(path + FolderCreate[everything])
        print(f'{FolderCreate[everything]} has been created')
    else:
        #this lets us know that the folder has been previously created
        print(f'{FolderCreate[everything]} has already been created')

NoOffilesMoved = 0

#looping through the list of files in the indicated folder
for files in listOfThingsToSort:
    
    #if statement to check whether we have the indicated file already in the created folder, if not we move it
    if ".mkv" in files and not os.path.exists(path + 'mkv format/' + files):
        #we use the below to move the indicated file from where it is to the created folder
        shutil.move(path + files, path + "mkv format/" + files)
        print(f'{files} has been moved to {path + "mkv format/"}')
        NoOffilesMoved += 1

    elif ".mp4" in files and not os.path.exists(path + "Mp4 format/" + files):
        shutil.move(path + files, path + 'Mp4 format/' + files)
        print(f'{files} has been moved to {path + "Mp4 format/"}')
        NoOffilesMoved += 1

    elif ".srt" in files and not os.path.exists(path + "Srt format/" + files):
        shutil.move(path + files, path + 'Srt format/' + files)
        print(f'{files} has been moved to {path + "Srt format/"}')
        NoOffilesMoved += 1
    else:
        print(f"The {files} was not moved because there is no file to move or an Error")
    
print(f'The number of files moved is: {NoOffilesMoved} file(s)')


'''Some of the bugs I encountered:
- Mp4 files was not moving because i made mistake of writing .Mp4 instead of .mp4
- .mkv started adding gibberish to the names of the files in moved to the moved, i don't know why 
but it resolved itself'''