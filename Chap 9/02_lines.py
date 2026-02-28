with open('myfile.txt', 'w') as f:
    f.write("hey wasi your amazing.i am so happy to meet you")
f = open('myfile.txt', 'r')
lines = f.readlines()
print(lines,type(lines))

f.close()