numRow=3
numCol=3
games=[[0 for x in range(numCol)] for x in range(numRow)]
for i in range(numRow):
    line=input().split(' ')
    row=[]
    for j in range(numRow):
        row.append(float(line[j]))
    games[i]=row
# 1.1 2.5 1.7
# 1.2 3.1 1.6
# 4.1 1.2 1.1

record=[]
for game in games:
    maxP=0
    for j in range(numCol):
        if game[maxP] < game[j]:
            maxP=j
    record.append((maxP,game[maxP]))
string=''
summ=1.0
num_char={0:'W',
          1:'T',
          2:'L'}
for i in record:
    string+=num_char[i[0]]+' '
    summ*=i[1]
summ=(summ*0.65-1)*2
summ=str(round(summ,2))
print(string+summ)
