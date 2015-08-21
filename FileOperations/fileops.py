__author__ = 'rahul telgote'

path = "/home/watson/Documents/PythonInterviews/FileOperations/"
fh = open(path+"sample.txt", "rb")
print "fh.tell : ", fh.tell()
# print fh
# print "fh.mode : ", fh.mode
# print "fh.name : ", fh.name
# print "fh.softspace : ", fh.softspace
# print fh.read()
# print fh.readline()
# print "fh.readlines : ", fh.readlines()

#
# writing into files
fw = open(path+"file1.txt", 'w')
fw.write('powerpork\n')
fw.write('indraprasth\n')
fw.write('mishti\n rahul \n telgote')

#
#copying file1.txt to file2.txt
fr = open(path+'file1.txt', 'r')
s = fr.read()
#fr.close()
fw2 = open(path+"file2.txt", 'w+')
#fw2.write("this is the content of the file2.txt file")
print "before copying the files: ", fw2.read()

## after copying the files
fw2.write(s)
print "after copying the files: ", fw2.read()
