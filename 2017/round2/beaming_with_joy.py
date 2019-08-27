#!/usr/bin/env python

'''
Given a formula in conjunctive normal form (2-CNF), finds a way to assign
True/False values to all variables to satisfy all clauses, or reports there
is no solution.
https://en.wikipedia.org/wiki/2-satisfiability
'''


''' Format:
        - each clause is a pair of literals
        - each literal in the form (name, is_neg)
          where name is an arbitrary identifier,
          and is_neg is true if the literal is negated
'''
'''
formula = [(('x', False), ('y', False)),
           (('y', True), ('y', True)),
           (('a', False), ('b', False)),
           (('a', True), ('c', True)),
           (('c', False), ('b', True))]
'''


def dfs_transposed(v, graph, order, vis):
    vis[v] = True

    for u in graph[v]:
        if not vis[u]:
            dfs_transposed(u, graph, order, vis)

    order.append(v)


def dfs(v, current_comp, vertex_scc, graph, vis):
    vis[v] = True
    vertex_scc[v] = current_comp

    for u in graph[v]:
        if not vis[u]:
            dfs(u, current_comp, vertex_scc, graph, vis)


def add_edge(graph, vertex_from, vertex_to):
    if vertex_from not in graph:
        graph[vertex_from] = []

    graph[vertex_from].append(vertex_to)


def scc(graph):
    ''' Computes the strongly connected components of a graph '''
    order = []
    vis = {vertex: False for vertex in graph}

    graph_transposed = {vertex: [] for vertex in graph}

    for (v, neighbours) in graph.items():
        for u in neighbours:
            add_edge(graph_transposed, u, v)

    for v in graph:
        if not vis[v]:
            dfs_transposed(v, graph_transposed, order, vis)

    vis = {vertex: False for vertex in graph}
    vertex_scc = {}

    current_comp = 0
    for v in reversed(order):
        if not vis[v]:
            # Each dfs will visit exactly one component
            dfs(v, current_comp, vertex_scc, graph, vis)
            current_comp += 1

    return vertex_scc


def build_graph(formula):
    ''' Builds the implication graph from the formula '''
    graph = {}

    for clause in formula:
        for (lit, _) in clause:
            for neg in [False, True]:
                graph[(lit, neg)] = []

    for ((a_lit, a_neg), (b_lit, b_neg)) in formula:
        add_edge(graph, (a_lit, a_neg), (b_lit, not b_neg))
        add_edge(graph, (b_lit, b_neg), (a_lit, not a_neg))

    return graph


def solve_sat(formula):
    graph = build_graph(formula)
    vertex_scc = scc(graph)

    for (var, _) in graph:
        if vertex_scc[(var, False)] == vertex_scc[(var, True)]:
            return None  # The formula is contradictory

    comp_repr = {}  # An arbitrary representant from each component

    for vertex in graph:
        if not vertex_scc[vertex] in comp_repr:
            comp_repr[vertex_scc[vertex]] = vertex

    comp_value = {}  # True/False value for each strongly connected component
    components = sorted(vertex_scc.values())

    for comp in components:
        if comp not in comp_value:
            comp_value[comp] = False

            (lit, neg) = comp_repr[comp]
            comp_value[vertex_scc[(lit, not neg)]] = True

    value = {var: comp_value[vertex_scc[(var, False)]] for (var, _) in graph}

    return value


def solve(r, c, house):
    empty_cells = []
    for i_row, row in enumerate(house):
        for i_col, cell in enumerate(row):
            if cell == '.':
                empty_cells.append((i_row, i_col))
    # True:vertical / False:horizontal
    # [(2, 2, True)]
    possible_beam_shooters_for_each_empty_cell = []
    for empty_cell in empty_cells:
        possible_beam_shooters = ()
        # 0:up / 1:down / 2:right / 3:left
        for direction in range(4):
            i_row = empty_cell[0]
            i_col = empty_cell[1]
            i_row_stop, i_col_stop, direction_stop = go_until_colliding_beam_shooter(
                i_row, i_col, direction)
            # This means vertical
            if direction_stop == 0 or direction_stop == 1:
                if go_until_colliding_beam_shooter(i_row_stop, i_col_stop, 0)[2] == -1 and go_until_colliding_beam_shooter(i_row_stop, i_col_stop, 1)[2] == -1:
                    possible_beam_shooters = possible_beam_shooters + (
                        ((i_row_stop, i_col_stop), not True),)
            # This means horizontal
            elif direction_stop == 2 or direction_stop == 3:
                if go_until_colliding_beam_shooter(i_row_stop, i_col_stop, 2)[2] == -1 and go_until_colliding_beam_shooter(i_row_stop, i_col_stop, 3)[2] == -1:
                    possible_beam_shooters = possible_beam_shooters + (
                        ((i_row_stop, i_col_stop), not False),)
        if len(possible_beam_shooters) == 1:
            possible_beam_shooters = possible_beam_shooters * 2
        elif len(possible_beam_shooters) == 0:
            return None
        possible_beam_shooters_for_each_empty_cell.append(
            possible_beam_shooters)
    sat_ans = solve_sat(possible_beam_shooters_for_each_empty_cell)
    shooter_cells = []
    for i_row, row in enumerate(house):
        for i_col, cell in enumerate(row):
            if cell == '-' or cell == '|':
                shooter_cells.append((i_row, i_col))
    if sat_ans is None:
        return None
    sat_ans_keys = sat_ans.keys()
    for shooter_cell in shooter_cells:
        if shooter_cell not in sat_ans_keys:
            r = shooter_cell[0]
            c = shooter_cell[1]
            if go_until_colliding_beam_shooter(r, c, 0)[2] == -1 and go_until_colliding_beam_shooter(r, c, 1)[2] == -1:
                sat_ans[(r, c)] = True
            elif go_until_colliding_beam_shooter(r, c, 2)[2] == -1 and go_until_colliding_beam_shooter(r, c, 3)[2] == -1:
                sat_ans[(r, c)] = False
            else:
                return None
    for k, v in sat_ans.items():
        house[k[0]][k[1]] = '|' if v else '-'
    return house


def go_until_colliding_beam_shooter(i_row, i_col, direction):
    while True:
        if direction == 0:
            i_row -= 1
        elif direction == 1:
            i_row += 1
        elif direction == 2:
            i_col += 1
        elif direction == 3:
            i_col -= 1
        else:
            raise Exception()
        if i_row < 0 or i_row >= r or i_col < 0 or i_col >= c:
            break
        cell = house[i_row][i_col]
        if cell == '/':
            if direction == 0:
                direction = 2
            elif direction == 1:
                direction = 3
            elif direction == 2:
                direction = 0
            elif direction == 3:
                direction = 1
            else:
                raise Exception()
        elif cell == '\\':
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1
            elif direction == 3:
                direction = 0
            else:
                raise Exception()
        elif cell == '#':
            break
        elif cell == '-' or cell == '|':
            return i_row, i_col, direction
    return -1, -1, -1


def rotate_successfully(possible_beam_shooters_for_each_empty_cell):
    return []


if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        r, c = map(int, input().split())
        house = []
        for _ in range(r):
            house.append([c for c in input()])
        ans = solve(r, c, house)
        print("Case #%d: %s" %
              (i + 1, "IMPOSSIBLE" if ans is None else "POSSIBLE"))
        if ans is not None:
            for row in ans:
                print("".join(row))
