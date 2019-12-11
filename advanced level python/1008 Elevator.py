import numpy as np
total=0
lst=np.array(list(map(int, input().split())))
lst=np.delete(lst,0)
for i in range(lstLen):
    if i == 0:
        diff=lst[i]
    else:
        diff=lst[i]-lst[i-1]
    if diff < 0:
        total=total+abs(diff)*4+5
    else:
        total=total+diff*6+5
print(total)
