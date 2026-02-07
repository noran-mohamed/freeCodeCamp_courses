def adjacency_list_to_matrix(adj_list):
    tot_nodes = len(adj_list)
    res = [[0 for _ in range(tot_nodes)] for _ in range(tot_nodes)]
    
    for i in adj_list.keys():
        for j in adj_list[i]:
            res[i][j] = 1
    print(res)
    return res
    


adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})
