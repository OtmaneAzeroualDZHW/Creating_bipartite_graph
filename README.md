# creating_bipartite_graph
Data triplets (users, items, index of their relative weights) are structured in a bipartite hypergraph (GRAPHYP [1]) , generating an equality graph where each edge weight is equal to the sum of the marks of both neighboring nodes.

 We assume that finding a matching with maximum weight in a bipartite graph (Hungarian algorithm for solving weighted and unweighted assignment problems) is equivalent to an assignment game with weighted matchings. With a Python code we developed a simple example that can be used for other data, with "Domain" and "Subdomain" that have to be supplemented with the desired data.

Formation of object pairs in a graph has been described being solved by connected by edges [2] but we add, in GRAPHYP algorithm, that while formulating objects pairs as triplets, including an index of relative weights of objects in a pair, could be analyzed from bipartite only. This algorithm extent information extraction to new by-products of a pair like routes and community detection in pairs.   






References:

[1] Fabre, R. (2019). A searchable space with routes for querying scientific information. In Proceedings of the 8th International Workshop on Bibliometric-enhanced Information Retrieval (BIR 2019), 112-124,  http://ceur-ws.org/Vol-2345/paper10.pdf
[2] Schubert M. (2012). Paarungsprobleme und ihre ungarischen Lösungen. In: Mathematik für Informatiker. Vieweg+Teubner Verlag. https://doi.org/10.1007/978-3-8348-1995-6_19
