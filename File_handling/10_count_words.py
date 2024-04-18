f=open("myfile1.txt",mode='r')

data=f.read()
words=data.split()
print("words are:",words)
count=len(words)
print("num of words in file:",count)

