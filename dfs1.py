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

graph1={'A':['B','E'],'B':['F','C','A'],'C':['B','G','D'],'D':['C','H'],
       'E':['A','F','I'],'F':['B','G','E'],'G':['F','C','H'],
       'H':['G','J','D'],'I':['E','J'],'J':['H','I']}
dfs('A','J',graph1)
