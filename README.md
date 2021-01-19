# creating_bipartite_graph
Data triplets (users, items, index of their relative weights) are structured in a bipartite hypergraph (GRAPHYP Fabre 2019[1]) , generating an equality graph where each edge weight is equal to the sum of the marks of both neighboring nodes.

 We assume that finding a matching with maximum weight in a bipartite graph (Hungarian algorithm for solving weighted and unweighted assignment problems) is equivalent to an assignment game with weighted matchings. With a Python code we developed a simple example that can be used for other data, with "Domain" and "Subdomain" that have to be supplemented with the desired data.

Formation of object pairs in a graph has been described being solved by connected by edges (Schubert, 2012) but we add, in GRAPHYP algorithm, that while formulating objects pairs as triplets, including an index of relative weights of objects in a pair, could be analyzed from bipartite only. This algorithm extent information extraction to new by-products of a pair like routes and community detection in pairs.   
