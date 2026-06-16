print("Hello world!!!")

with file in open("data.txt"):
    
    data = file.readline()
    while(data):
        print(f"- {data}")
        data = file.readline()