print("Hello world!!!")

with file in open("data.txt"):
    
    line = file.readline()
    while(line):
        print(line)
        line = file.readline()