def dfs(start,goal,graph,vis=None,path=None):
    if vis is None:
        vis=set()
    if path is None:
        path=[]
    path.append(start)
    vis.add(start)
    print(start)
    if start==goal:
        return path
    for child in graph[start]:
        if child not in vis:
            if dfs(child,goal,graph,vis):
                return True
    return False
nodes=int(input("enter the number of nodes :"))
graph={}
for i in range(1,nodes+1):
    key=input("enter the key:")
    v=int(input(f"enter the value of key {key}:"))
    n=[]
    for x in range(1,v+1):
        value=input("enter the value:")
        n.append(value)
    graph[key]=n
print(f"graph is:{graph}")
start=input("enter the starting node:")
goal=input("enter the goal node:")
dfs(start,goal,graph)
