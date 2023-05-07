import os

# define paths to the two directories containing the image files
dir1 = '/Users/adityagupta/Desktop/Train temp'
dir2 = '/Users/adityagupta/Desktop/Train'

# create sets of the image file names in each directory
set1 = set(os.listdir(dir1))
set2 = set(os.listdir(dir2))

# calculate the set difference between the two sets of file names
diff = set1 - set2
c=0
# print the file names that are in the first directory but not in the second
for filename in sorted(diff):
    print(filename)
    c+=1
print(c)
