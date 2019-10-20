import pandas as pd

c = pd.read_csv('refseq93.color',delimiter='\t')
d = pd.read_csv('refseq.genomes.k21s1000.tsv',delimiter='\t')


m = c.merge(d,how='inner',left_on='asm',right_on='ID')


c.groupby('#node').first().shape
m.groupby('#node').first().shape
