## hs19-biovis

General Information : http://biovis.net/2019/biovisChallenges_vis/

## Project Description

RefSeq is a massive online repository of genome sequencing data, but its size and complexity makes it prohibitive to explore such a large dataset.  A [prior publication](https://doi.org/10.1186/s13059-016-0997-x) has developed method to quickly compute the distances between genomes and has applied their method to RefSeq. The resulting distance matrix between RefSeq genomes results in a graph, that can be visualized to show the structure of RefSeq and the connections between cluster of species. However, the resulting RefSeq graph visualization is still massive and it remains difficult to explore these data.

In this project, we are exploring how such a massive dataset can be more concisely visualized and explored. Our overall project objectives are multi-faceted. First, we consider what specific questions and tasks would be relevant to biologists. Second, we consider how we should design a software system that addresses those biologist research questions and tasks. Finally, we will attempt to generate a working prototype for our proposed design.

This hack is a collaboration between HackSeq and BioVis.  Detailed project information is available online. More information is available online : http://biovis.net/2019/biovisChallenges_vis/

## Datasets

This dataset is too large to load into the repo, so please have a local copy on your own machine within this project repo. The data can be downloaded from the following location:

https://biovis.s3.amazonaws.com/biovis_contest_2019.zip


Current working dataset is on Orca : edges_undirected_annoted_v2.objz (Python Pickle Object)

Graph Stats:

Nodes : 127,465
Edges : 235,545,792
Clusters: 6,279 

## Progress

### Day 1

1) Identified two levels of the interface : Overview and Sequence Comparison

Overview : See the whole network with summarized graph topology
Tasks: Overview, Browse, Filter

Sequence Comparion : Identify linkages and paths between organisms
Tasks : Overview (subgraph), Path Identification, Comparison

2) Decided upon python and graphing/analysis/vis libraries

3) Created a final graph dataset with node annotations

TO DO:
- Continue to refine the usage scenario
- Load the data and continue implementing!






