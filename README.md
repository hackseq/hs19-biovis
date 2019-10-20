## hs19-biovis

General Information : http://biovis.net/2019/biovisChallenges_vis/

## Team Members
|Member|Github|
|------|-------|
|Ana Crisan | amcrisan|
| Etienne Meunier | Etienne-Meunier |
| Federico Arribas | Svendsen |
| Javier Castillo-Arnemann | yavyx|


## Project Description

RefSeq is a massive online repository of genome sequencing data, but its size and complexity makes it prohibitive to explore such a large dataset.  A [prior publication](https://doi.org/10.1186/s13059-016-0997-x) has developed method to quickly compute the distances between genomes and has applied their method to RefSeq. The resulting distance matrix between RefSeq genomes results in a graph, that can be visualized to show the structure of RefSeq and the connections between cluster of species. However, the resulting RefSeq graph visualization is still massive and it remains difficult to explore these data.

In this project, we are exploring how such a massive dataset can be more concisely visualized and explored. Our overall project objectives are multi-faceted. First, we consider what specific questions and tasks would be relevant to biologists. Second, we consider how we should design a software system that addresses those biologist research questions and tasks. Finally, we will attempt to generate a working prototype for our proposed design.

This hack is a collaboration between HackSeq and BioVis.  Detailed project information is available online. More information is available online : http://biovis.net/2019/biovisChallenges_vis/

## Datasets

This dataset is too large to load into the repo, so please have a local copy on your own machine within this project repo. The data can be downloaded from the following location:

https://biovis.s3.amazonaws.com/biovis_contest_2019.zip


Current working dataset is on Orca : edges_undirected_annoted_v3.objz (Python Pickle Object)

**Graph Stats:**

Nodes : 127,465

Edges : 235,545,792

Clusters: 6,279 

*This graph also contains:*

- 4 Kingdoms  (Eukaryota, Bacteria, Archaea,  Viruses)

- 40 Phyla

- 1,763 Genuses

**Cluster stats:**

*Nodes per cluster*

- Min size: 2, Max size : 12,348

- Median size : 3, Average Size : 24

*Genus per cluster*

- Min size: 2, Max size : 21

- Median size : 1, Average Size : 1

*Phyla per cluster*

- Min size: 1, Max size : 5

- Median size : 1, Average Size : 1


## Dependencies
Python v 3.7
Packages:
- dash
- igraph
- pandas
- networkx
- mash
- collections

Requires about 70 GIGS of RAM to load the dataset into RAM.

## Analysis Code
We deliver a set of scripts to load, annotate, and analyze this massive graph. We also contribute a preliminary user interface for getting an overview of the graph, browsing its contents, and filtering desired nodes. 

### Graph Analysis Scripts
A series of python scripts. Here is an overview of the files:

- **Graph_Preprocessing.py** : loading and annotation graph 

- **graph_converter.py** : set of scripts to convert between igraph, gml, and cytospace

- **database_analysis.py** : analysis of the MASH refseq database, in order to extract weights

- **add_weights_to_graph.py** : add weights to the graph edges (this is an example on a small subgraph)

### Dashboard
We also produce a preliminary dashboard using Dash. 

- **dash_app.py** : preliminary dashboard application


## Results

- Biological stakeholder usage scenario and tasks for such a big network :
    - *Usage Scenario* : A biologist wishing the explore high level structure of large but unknown genomic network(in this case RefSeq), potentially seeking interesting and unexpected connects to probe in detail.
    - Highlight level network view. Tasks: Overview, browse, filter
    - Low level node view. Task: Filter, Comparison, 

- Exploring how to visualization and represent a massive and densely connected graph

- Identify cluster structure within the graph. 

- Derive additional information for the graph : edges weights of genomic similarity (not just 0 or 1) and taxonomic information

- Derived summary statistics for graph overall and also its clusters.

- Attempt to identify and display biologically relevant parts of the graph


## Ongoing Work
This set of code sets can be used to tackle this massive graph and we contribute additional information to help others get going with their graph analysis and to with this graph in particular.







