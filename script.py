from operator import le
from posixpath import split

log = open('review.txt') #abrir o arquivo

read = log.readlines() #colocando em uma list

linhas = []
time = []

for x in read:
    item = x
    for y in ['\n', '\t', '/', '.', '-', '(', ')']:
        item = item.replace(y, "")
        item = item.replace(",", " ")
    linhas.append(item)

log.close()
i=0


for linha in linhas:
    
    if i<(len(linhas)-2):
     i=i+1
     
    if 'RXKEY' in linha:
        
        if 'LINKP' in linhas[i]:
            print("")
        else:
            time.append(linha)
            time.append(linhas[i])

print(time)

            
    