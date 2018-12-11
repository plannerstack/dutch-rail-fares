import networkx as nx

distances = {}

with open('kilonetnew.dat', 'r') as f:
    lines = f.readlines()
    for l in lines:
        fr,to,first,second,code = l.split(',')
        distances[fr + ':' + to] = int(second)

G=nx.Graph()

def expand(lijn):
	for j in range(1, len(lijn)):
		G.add_edge(lijn[j - 1], lijn[j], weight=distances[lijn[j - 1] + ':' + lijn[j]])

def cost(steps):
	s = 0
	for j in range(1, len(steps)):
		s += distances[steps[j - 1] + ':' + steps[j]]
	return s

lijn1 = ['odz','hglo','hgl','hglg','ddn','go','lc','zp']
expand(lijn1)

lijn2 = ['es', 'esk', 'hgl', 'bn', 'amri', 'aml', 'wdn', 'nvd', 'rat', 'hno', 'zl']
expand(lijn2)

lijn3 = ['kpn', 'zlsh', 'zl']
expand(lijn3)

lijn4 = ['aml', 'vz', 'da', 'vhp', 'mrb', 'hdb']
expand(lijn4)

lijn5 = ['zl', 'dl', 'omn', 'mrb', 'hdb', 'gbg', 'co', 'dln', 'na', 'emnz', 'emn']
expand(lijn5)

pairs = set(lijn1 + lijn2 + lijn3 + lijn4 + lijn5)

print('startplaceref,endplaceref,distance,operatorref,fareref')

for x in pairs:
	for y in pairs:
		if x != y:
			steps = nx.dijkstra_path(G, x, y, weight='weight')
			print('NL:S:%s,NL:S:%s,%d,%s,%s' % (x, y, cost(steps), 'IFF:BN', 'IFF:BN'))
