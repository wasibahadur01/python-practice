with open('poem.txt') as f:
    poem = f.read()
    if 'moments' in poem and 'parrots' in poem:
    
        print('The poem mentions the moments and parrots.')
    else:
        print('The poem does not mention both the moments and parrots.')

