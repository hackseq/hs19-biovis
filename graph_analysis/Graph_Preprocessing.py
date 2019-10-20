
import igraph
import tqdm
import pickle
import pandas as pd

#Note: requires roughly 70 gigs of ram to load


#######################
# LOAD GRAPH
######################
#Load graph into igraph
g = igraph.Read_Ncol("refseq93.edge.tsv",directed=FALSE)
#g = igraph.Graph.Read_Pickle('edges_undirect.objz') #pre-svaed graph


#######################
# METADATA
######################
#Add node features 
#Node data supplied by authors
df = pd.read_csv('refseq93.color',delimiter='\t')
node_gb_df = df.groupby('#node').first() #feature dataset

#taxonomic data from NCBI
taxa_df = pd.read_csv("../Data/taxa_rank.csv")

#######################
# ADD METADATA
######################
#adding node data from node_gbdf
for i in tqdm(range(g.vcount())) :
    d = df_node_gb[df_node_gb.index == g.vs[i]['name']].to_dict('recors')[0]
    for k,v in zip(d.keys(),d.values()) : g.vs[i][k] =v

# Add clusters 
cl = g.clusters()
for i, cli in enumerate(cl) :
    for n in cli :
        g.vs[n]['cluster'] =  i

#adding node data from taxa
for i in range(g.vcount()):
    d = taxa_df.loc[taxa_df['tax_id'] == g.vs[i]['tax']]
    
    if(len(d)>0):
        d = d.to_dict('recors')[0]
        for k,v in zip(d.keys(),d.values()) : g.vs[i][k] =v
    else:
        d = taxa_df.loc[0].to_dict()
        for k,v in zip(d.keys(),d.values()) : g.vs[i][k] = None


#save the graph for fast loading later!
g.Write_Picklez("edges_undirected_w_annotations.pklz")