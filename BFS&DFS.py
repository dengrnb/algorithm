#BFS 广度优先搜索

graph = {
    "A": ["B","C"],
    "B": ["A","C","D"],
    "C": ["A","B","D","E"],
    "D": ["B","C","E","F"],
    "E": ["C","D"],
    "F": ["D"]
}
graph.keys()

###BFS 队列
queue = []
queue.append('A')
queue.append('B')
queue.append('C')
queue.pop(0)

def BFS(graph,s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while(len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)

BFS(graph,"A")
BFS(graph,"E")

###DFS 栈
stack = []
stack.append('A')
stack.append('B')
stack.append('C')
stack.pop()

def DFS(graph,s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while(len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)

DFS(graph,"A")
DFS(graph,"E")

###最短路径
def BFS(graph,s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s : None}

    while(len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent

parent = BFS(graph,"E")
for key in parent:
    print(key,parent[key])

v = 'B'
while v != None:
    print(v)
    v = parent[v]


