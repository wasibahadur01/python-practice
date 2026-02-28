# Open the file in read mode
with open("file.txt", "r") as f:
    content = f.read()

# Replace all occurrences of "Donkey" with "#####"
content = content.replace("Donkey", "#####")

# Write the updated content back to the same file
with open("file.txt", "w") as f:
    f.write(content)
