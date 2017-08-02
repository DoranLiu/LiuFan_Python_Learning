# coding: utf-8

'''
为了避免重复而对graph.py进行必要的重构之后的代码
不再有bfs()和dfs()两个函数，我们将代码重构为使用单个traverse()函数。
traverse() 函数实际上是一个模板函数。它接受一个参数action，该参数是一个“知道”如何延伸路径的函数。
根据要使用的算法，我们可以传递extend_bfs_path()或extend_dfs_path()作为目标动作。
'''
def traverse(graph, start, end, action):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                return (True, path)
            # 两个顶点不相连，则跳过
            if current not in graph:
                continue
        visited = action(visited, graph[current])
    return (False, path)


def extend_bfs_path(visited, current):
    return visited + current


def extend_dfs_path(visited, current):
    return current + visited


def main():
    graph = {
        'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
        'Mannheim': ['Karlsruhe'],
        'Karlsruhe': ['Augsburg'],
        'Augsburg': ['Munchen'],
        'Wurzburg': ['Erfurt', 'Nurnberg'],
        'Nurnberg': ['Stuttgart', 'Munchen'],
        'Kassel': ['Munchen'],
        'Erfurt': [],
        'Stuttgart': [],
        'Munchen': []
    }

    bfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', extend_bfs_path)
    dfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', extend_dfs_path)
    print('bfs Frankfurt-Nurnberg: {}'.format(bfs_path[1] if bfs_path[0] else 'Not found'))
    print('dfs Frankfurt-Nurnberg: {}'.format(dfs_path[1] if dfs_path[0] else 'Not found'))

    bfs_nopath = traverse(graph, 'Wurzburg', 'Kassel', extend_bfs_path)
    print('bfs Wurzburg-Kassel: {}'.format(bfs_nopath[1] if bfs_nopath[0] else 'Not found'))
    dfs_nopath = traverse(graph, 'Wurzburg', 'Kassel', extend_dfs_path)
    print('dfs Wurzburg-Kassel: {}'.format(dfs_nopath[1] if dfs_nopath[0] else 'Not found'))

if __name__ == '__main__':
    main()
