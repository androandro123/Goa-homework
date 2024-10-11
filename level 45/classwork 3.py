def search(text,word):
    if word in text:
        return "word found"
    else:
        return "word not found"
print(search(input("text:"),input("word:")))