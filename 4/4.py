lyrics1 = "Dance for me, dance for me, dance for me, oh, oh, oh."
lyrics1 = lyrics1.replace('.', ',')
lyrics2 = "I've never seen anybody do the things you do before."
lyrics2 = lyrics2.replace('.', ',')
lyrics3 = "They say move for me, Move for me, Move for me, Ay, Ay, Ay."
lyrics3 = lyrics3.replace('.', ',')
lyrics4 = "And when you're done."
lyrics4 = lyrics4.replace('.', ',')
lyrics5 = "I'll make you do it all again."
lyrics5 = lyrics5.replace('.', ',')

list1 = lyrics1.split(', ')
for i in range(0, len(list1)):
    list1[i] = list1[i].capitalize()
lyrics1 = ""
for i in list1:
    if i[-1] == ',':
        tempStr = i.replace(',', '.')
        lyrics1 += (tempStr + " ")
    else:
        lyrics1 += (i + ", ")
        
list2 = lyrics2.split(', ')
for i in range(0, len(list2)):
    list2[i] = list2[i].capitalize()
lyrics2 = ""
for i in list2:
    if i[-1] == ',':
        tempStr = i.replace(',', '.')
        lyrics2 += (tempStr + " ")
    else:
        lyrics2 += (i + ", ")
        
list3 = lyrics3.split(', ')
for i in range(0, len(list3)):
    list3[i] = list3[i].capitalize()
lyrics3 = ""
for i in list3:
    if i[-1] == ',':
        tempStr = i.replace(',', '.')
        lyrics3 += (tempStr + " ")
    else:
        lyrics3 += (i + ", ")
        
list4 = lyrics4.split(', ')
for i in range(0, len(list4)):
    list4[i] = list4[i].capitalize()
lyrics4 = ""
for i in list4:
    if i[-1] == ',':
        tempStr = i.replace(',', '.')
        lyrics4 += (tempStr + " ")
    else:
        lyrics4 += (i + ", ")
        
list5 = lyrics5.split(', ')
for i in range(0, len(list5)):
    list5[i] = list5[i].capitalize()
lyrics5 = ""
for i in list5:
    if i[-1] == ',':
        tempStr = i.replace(',', '.')
        lyrics5 += (tempStr + " ")
    else:
        lyrics5 += (i + ", ")
        
print(lyrics1)
print(lyrics2)
print(lyrics3)
print(lyrics4 + lyrics5)