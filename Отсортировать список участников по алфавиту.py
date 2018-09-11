inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'r', encoding='utf8')
lines = inFile.readlines()
lines.sort()
for i in lines:
    print(*i.spilit()[:2] + i.spilit[:3], end=' ')
    print()
inFile.close()
outFile.close()
