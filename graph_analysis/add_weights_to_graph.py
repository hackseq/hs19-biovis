import igraph
import pandas as pd
from tqdm import tqdm
 #%% Load GRAP Name
g = igraph.Graph.Read_Pickle('../graphs/smaller_subgraph.pklz')
#g.add_vertex()
#g.add_vertex()
#g.add_vertex()

#%%.
m = g.get_adjacency()

#%% Extract indexes
index_asm_dist = []
f = open('../distances_k21s1000.tsv')
n_lines = int(f.readline().strip())
for i in tqdm(range(n_lines)):
    l = f.readline().split('\t')
    index_asm_dist.append(l[0])

index_asm_graph = [x['asm'] for x in g.vs]

#%%
print('Common asm : {} / {}'.format(len(list(set(index_asm_graph).intersection(index_asm_dist))),len(index_asm_graph)))

#%%
f = open('../distances_k21s1000.tsv')
n_lines = int(f.readline().strip())

for i in tqdm(range(n_lines)):
    line = f.readline().split('\t')
    name = line[0]
    l = list(map(lambda x : float(x.strip()),line[1:]))
    if name in index_asm_graph :
        idx_1 = index_asm_graph.index(name)
        for i, v in enumerate(l) :
            if index_asm_dist[i] in index_asm_graph :
                idx_2 = index_asm_graph.index(index_asm_dist[i])
                if m[idx_1,idx_2] == 1:
                    m[idx_1, idx_2] = v
                    m[idx_2, idx_1] = v

#%%
g2 = g.Weighted_Adjacency(matrix=list(m),attr='weight')
g2.write_pickle('small_weighted.obj')
