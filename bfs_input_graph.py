from collections import deque
def bfs(start,goal,graph,visited=None):
    visited=set()
    queue=deque([[start]])
    while queue:
        print("queue",queue)
        print("visited",visited)
        path=queue.popleft()
        print("path",path)
        node=path[-1]
        print("node",node)
        if node==goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path=path+[neighbor]
                print(new_path)
                queue.append(new_path)
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
print(f"graph is:{graph3}")
start=input("enter the starting node:")
goal=input("enter the goal node:")
bfs(start,goal,graph)
