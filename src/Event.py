sample = "hey you here are some words much more words than that i need this to be fairly long and this can be arbitrarily long and it will still work even if it makes the linter upset"
text = sample.split()
show = ""
i = 0
# while i < 6:
#     show += text[i] + " "
#     i += 1
# print(show)
i = 0
sentence = ''

for word in text:
    if i<6:
        sentence += word + " "
        i += 1
    else:
        print(sentence)
        sentence=word + " "
        i=0

print(sentence)