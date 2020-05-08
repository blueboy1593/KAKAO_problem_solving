import sys
sys.setrecursionlimit(10**6)

class IjinTree:
    def __init__(self,dataList):
        self.data=max(dataList,key=lambda x :x[1])
        leftarr =list(filter(lambda x :x[0] < self.data[0] , dataList))
        rightarr = list(filter(lambda x :x[0] > self.data[0] , dataList))
        if leftarr != []:
            self.left=IjinTree(leftarr)
        else :
            self.left=None
        if rightarr != []:
            self.right=IjinTree(rightarr)
        else :
            self.right=None

def fix_node(node,postList,preList):
    postList.append(node.data)
    if node.left is not None:
        fix_node(node.left,postList,preList)
    if node.right is not None:
        fix_node(node.right,postList,preList)
    preList.append(node.data)

def solution(nodeinfo):
    answer = []
    root = IjinTree(nodeinfo)
    postList = []
    preList = []
    fix_node(root,postList,preList)
    answer.append(list(map(lambda x: nodeinfo.index(x)+1 ,postList)))
    answer.append(list(map(lambda x: nodeinfo.index(x)+1 ,preList)))
    return answer
