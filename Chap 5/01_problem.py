words={
    'adaba':'hello',
    'baba':'world',
    'caca':'python',
    'kalal':'banana',
}
rev_words={v:k for k,v in words.items()}
word=input("Enter a word: ")

print(rev_words.get(word,'word not found'))