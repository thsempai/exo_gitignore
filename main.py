print("Hello, world!")

with file in open("data.txt"):
    
    data = file.readline()
    while(data):
        print(data)
        data = file.readline()