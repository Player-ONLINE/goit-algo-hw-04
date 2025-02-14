cats = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
"""

with open('cats.txt', "w") as file:
    file.write(cats)

try:
    with open('cats.txt', "r") as file:
        for line in file:
            id, name, age = line.strip().split(",")
            print(f"ID: {id}, Name: {name}, Age: {age}")
except FileNotFoundError:
    print("File not found")
