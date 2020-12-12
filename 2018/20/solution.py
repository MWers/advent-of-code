from __future__ import print_function
import re

data = ('^WNE$', 3)
data = ('^ENWWW(NEEE|SSE(EE|N))$', 10)
data = ('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$', 18)
data = ('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$', 23)
# data = ('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$', 31)
#
# input_file = 'input-full.txt'
# with open(input_file, 'r') as f:
#     data = (f.readline().rstrip(), -1)
#     print(data)

def traverse_graph(graph):
    for node in graph:
        if node[0] in ['at', 'literal']:
            print(node)
        elif node[0] in ['subpattern']:
            print(node[1][1][0])
        elif node[0] in ['branch']:
            print(node[1][0][0])


graph = re.sre_parse.parse(data[0])
traverse_graph(graph)
