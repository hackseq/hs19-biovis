
#Add features 
df = pd.read_csv('refseq93.color',delimiter='\t')
node_gb = df.groupby('#node').first()
 g = igraph.Graph.Read_Pickle('edges_undirect.objz')

for i in tqdm(range(g.vcount())) :
    d = df_node_gb[df_node_gb.index == g.vs[i]['name']].to_dict('recors')[0]
    for k,v in zip(d.keys(),d.values()) : g.vs[i][k] =v

# Add clusters 
cl = g.clusters()
for i, cli in enumerate(cl) :
    for n in cli :
        g.vs[n]['cluster'] =  i
