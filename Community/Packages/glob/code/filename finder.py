from glob import glob

#define the path variable
path="../data/"

#open a list with all file names in that directory that have the following extension
textfiles = glob(path + "*.txt")
print(textfiles)

#open a list with all file names in that directory and all sub directories that have the following extension
textfiles = glob(path + '**/*.txt',recursive=True)
print(textfiles)

