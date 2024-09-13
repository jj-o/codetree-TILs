nodes = [Node() for _ in range(MAX_ID)]
isRoot = [False] * MAX_ID

def canMakeChild(curr, needDepth):
    if curr.id == 0:
        return 
    if curr.maxDepth <= needDepth:
        return False
    return canMakeChile(nodes[curr.parentId], needDepth+1)

if __name__ == "__main__":
    Q = int(input())
    for i in range(1,Q+1):
        query = list(map(int,input().split()))
        T = query[0]
        if T == 100:
            mId, pId, color, maxDepth = query[1:]
            if pId == -1:
                isRoot[mId] = True
            if isRoot[mId] or canMakeChild(nodes[pId], 1):
                nodes[mId].id = mId
                nodes[mId].color = color
                nodes[mId].maxDepth = maxDepth
                nodes[mId].parentId = 0 if isRoot[mId] else pId
                nodes[mId].lastUpdate = id

                if not isRoot[mId]:
                    nodes[pId].childIds.append(mId)
        elif T == 200:
            mId, color = query[1:]
            nodes[mId].color = color
            nodes[mId].lastUpdate = i
        elif T == 300:
            mId = query[1]
            print(getColor(nodes[mId])[0])
        elif T == 400:
            for i in range (1, MAX_ID):
                if isRoot[i]:
                    beauty += getBeauty(nodes[i], nodes[i].color, nodes[i].lastUpdate)[0]
                print(beauty)