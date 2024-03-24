graph = {}
with (open('vers.txt', 'r')) as f:
    for line in f.readlines():
        new_v = line.split()
        if len(new_v) > 1:
            graph[new_v[0]] = new_v[2:]
        else:
            graph[new_v[0]] = None


def dfs(g, v, path):
    path.append(v)
    for vi in g[v]:
        if vi not in path:
            dfs(g, vi, path)
    if not g[v]:
        print(path)
        path.remove(v)
        return True
    path.remove(v)


print(graph)
dfs(graph, 'A', [])
