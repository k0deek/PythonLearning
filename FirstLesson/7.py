text = input()
newtext = ''
for i in range(len(text)):
    if text[i] == 'o':
        newtext = newtext + 'a'
    elif text[i] == 'T':
        newtext = newtext + 'R'
    else:
        newtext = newtext + text[i]
print(newtext)
