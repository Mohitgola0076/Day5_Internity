'''
Python too supports file handling and allows users to handle files i.e.,
to read and write files, along with many other file handling options, to operate on files.
Data handling is the process of ensuring that research data is stored, 
archived or disposed off in a safe and secure manner during and after the conclusion of a research project.
Proper planning for data handling can also result in efficient and economical storage, retrieval, and disposal of data.
'''


#  Python print() to File Example : 

def main():
     f= open("guru99.txt","w+")
     #f=open("guru99.txt","a+")
     for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
     f.close()   
     #Open the file back and read the contents
     #f=open("guru99.txt", "r")
     #   if f.mode == 'r': 
     #     contents =f.read()
     #     print contents
     #or, readlines reads the individual line into a list
     #fl =f.readlines()
     #for x in fl:
     #print x
if __name__== "__main__":
  main()


# Python code to illustrate read() mode

file = open("file.text", "r") 
print (file.read())


# Python code to create a file

file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


# Python code to illustrate append() mode

file = open('geek.txt','a')
file.write("This will add this line")
file.close()

# Python code to illustrate with()

with open("file.txt") as file:
	data = file.read()
# do something with data


# Python code to illustrate split() function

with open("file.text", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)

