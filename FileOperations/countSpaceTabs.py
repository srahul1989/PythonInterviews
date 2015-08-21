__author__ = 'watson'

path = "/home/watson/Documents/PythonInterviews/FileOperations/"

fh = open(path+"sample.txt")
spaces = 0
tabs = 0
print "before counting : ", spaces
print "before counting : ", tabs
#print "enumerate(fh) : ", enumerate(fh)
for i, line in enumerate(fh):
    spaces += line.count(' ')
    tabs += line.count('\t')

print "after counting : ", spaces
print "after counting : ", tabs
