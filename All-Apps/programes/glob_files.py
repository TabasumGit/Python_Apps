import glob

# myfiles= glob.glob(r'D:\Python-Apps\Programmes\files\*.txt')

# for filepath in myfiles:
#     with open(filepath, 'r') as file:
#         print(file.read().upper())
#         import glob

myfiles = glob.glob(r'D:\Python-Apps\All-Apps\files\*.txt')

for file in myfiles:
    print(file)