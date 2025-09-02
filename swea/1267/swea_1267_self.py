def dfs(node_info, node, visited, result):
    visited[node] = True

    for next_node in node_info[node]:
        if not visited[next_node]:
            dfs(node_info, next_node, visited, result)
    result.append(node)


def solve():
    for tc in range(1, 11):
        node_num, edge_num = map(int, input().split())
        edge_list = list(map(int, input().split()))

        node_info = {i: [] for i in range(1, node_num + 1)}

        for idx in range(0, edge_num * 2, 2):
            node = edge_list[idx]
            edge = edge_list[idx + 1]
            node_info[node].append(edge)
        # print(node_info)

        in_degree = {i: 0 for i in range(1, node_num + 1)}
        for node in node_info:
            for item in node_info[node]:
                in_degree[item] += 1
        # print(in_degree)

        visited = {i: False for i in range(1, node_num + 1)}
        result = []

        for node, value in in_degree.items():
            if value == 0:
                dfs(node_info, node, visited, result)

        result = reversed(result)
        print(f"#{tc} {' '.join(map(str, result))}")
    return


solve()
