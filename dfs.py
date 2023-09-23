from graph import Graph


def dfs(v: str, order: list[str], used: dict[str, bool], g: Graph):
    used[v] = True

    for vertex in g.next(v):
        if not used[vertex]:
            dfs(v=vertex, order=order, used=used, g=g)

    order.append(v)


def dfs_transpose(v: str, component: list[str], used: dict[str, bool], g_t: Graph):
    used[v] = True
    component.append(v)

    for vertex in g_t.next(v):
        if not used[vertex]:
            dfs_transpose(v=vertex, component=component, used=used, g_t=g_t)
