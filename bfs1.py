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
                
graph2={'A':['B','C'],'B':['A','D'],'C':['A','D'],'D':['B','C']}
result=bfs('A','D',graph2)
print("\n")
print("Shortest Path:", result)
