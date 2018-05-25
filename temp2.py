tempanswer = [3,2,4,5]
tempguess = [1,1,4,5]
result = ['-','-','-','-'] # convert using (''.join(result)) when printing

hintpeg=0


for x in range(4):
    if tempguess[x] == tempanswer[x]:
        result[hintpeg] = '1'
        tempguess[x] = '+'
        tempanswer[x] = '*'
        hintpeg += 1
        # Second run, find content matches
for x in range (4):
    if tempguess[x] in tempanswer:
        result[hintpeg] = '0'
        hintpeg += 1

print (tempguess)
print (tempanswer)
print (' '.join(result))
        
