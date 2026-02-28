import os
print('cwd:', os.getcwd())
with open('poem.txt') as f:              # same filename as in your workspace
    poem = f.read()
print('read', len(poem), 'characters')
print(poem)