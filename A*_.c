import networkx as nwx
g=nwx.Graph()
while True:
    ch=int(input("want to insert edge? 1=yes/2=no:"))
    if ch==1:
        node1=input("node 1: ").strip().upper()
        node2=input("node 2: ").strip().upper()
        w=int(input("weight: "))
        g.add_edge(node1,node2,weight=w)
    else:
        break
print("\nlist:")
for n,nbrs in g.adj.items():
    print(n,nbrs)
start=input("start node: ").strip().upper()
goal=input("goal node: ").strip().upper()
h={goal:0}
for n in g.nodes():
    if n!=goal:
        h[n]=int(input(f"Heuristic value of {n}: "))
def get_h(u,v):
    return h[u]
path=nwx.astar_path(g,start,goal,heuristic=get_h,weight='weight')
cost=nwx.astar_path_length(g,start,goal,heuristic=get_h,weight='weight')
print("optimal path: ","->".join(path))
print("total cost: ",cost)
