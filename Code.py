from collections import defaultdict
graph=defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)
def find_path(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath=find_path(graph,node,end,path)
            if newpath:
                return newpath
    return None
def gcd(a,b):
    if b==0:
        return a
    if b>a:
        return gcd(b,a)
    return gcd(b,a%b)

N=int(input())
for i in range(0,N-1):
    u,v=map(int,input().split())
    addEdge(graph,u,v)
value=list(map(int,input().split()))
Q=int(input())
for i in range(0,Q):
    query=input().split()
    if query[0] =='F':
        u=int(query[1])
        v=int(query[2])
        path=find_path(graph,u,v)
        if path!=None:
            
            result=value[path[0]]
            length=len(path)
            for i in range(1,length) :
                result=gcd(result,value[path[i]])
            print(result)
            
    if query[0] =='C':
        u=int(query[1])
        v=int(query[2])
        path=find_path(graph,u,v)
        if path!=None:
            inc=int(query[3])
            for i in path:
                value[i]=value[i]+inc
        