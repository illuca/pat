# 已知中序和先序, 求层次
class Node:
    def __init__(self, data=None, level=None):
        self.level = level
        self.data = data


def dfs(root, start, end, level):
    global res
    if start > end:
        return
    i = start
    while i < end and inLst[i] != postLst[root]:
        i += 1
    res.append(Node(postLst[root], level))
    dfs(root-1-end+i, start, i-1, level+1)
    dfs(root-1, i+1, end, level+1)


n = int(input())

postLst = list(map(int, input().split()))
inLst = list(map(int, input().split()))

res = []
length = len(inLst)
dfs(-1, 0, length-1, 0)
res.sort(key=lambda x: x.level)
print(' '.join(list(map(str, [node.data for node in res]))))
