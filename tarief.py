distances = {}

print('startplaceref,endplaceref,distance,operatorref,fareref')

with open('kilonetnew.dat', 'r') as f:
	lines = f.readlines()
	for l in lines:
		fr,to,first,second,code = l.split(',')
		distances[fr + ':' + to] = int(second)

def expand(lijn, operator, fareref):
    for i in range(0, len(lijn)):
        s = 0
        for j in range(i + 1, len(lijn)):
            pair1 = (lijn[i], lijn[j],)
            s += distances[lijn[j - 1] + ':' + lijn[j]]
            print('NL:S:%s,NL:S:%s,%d,%s,%s' % (pair1[0], pair1[1], s, operator, fareref))

lijn = ['odz','hglo','hgl','hglg','ddn','go','lc','zp']
expand(lijn, 'IFF:BN', 'IFF:BN')
expand(lijn[::-1], 'IFF:BN', 'IFF:BN')

lijn = ['es', 'esk', 'hgl', 'bn', 'amri', 'aml', 'wdn', 'nvd', 'rat', 'hno', 'zl']
expand(lijn, 'IFF:BN', 'IFF:BN')
expand(lijn[::-1], 'IFF:BN', 'IFF:BN')

lijn = ['kpn', 'zlsh', 'zl']
expand(lijn, 'IFF:BN', 'IFF:BN')
expand(lijn[::-1], 'IFF:BN', 'IFF:BN')

lijn = ['aml', 'vz', 'da', 'vhp', 'mrb', 'hdb']
expand(lijn, 'IFF:BN', 'IFF:BN')
expand(lijn[::-1], 'IFF:BN', 'IFF:BN')

lijn = ['zl', 'dl', 'omn', 'mrb', 'hdb', 'gbg', 'co', 'dln', 'na', 'emnz', 'emn']
expand(lijn, 'IFF:BN', 'IFF:BN')
expand(lijn[::-1], 'IFF:BN', 'IFF:BN')

lijn = ['gd', 'wadt', 'wad', 'wadn', 'bsks', 'bsk', 'apn']
expand(lijn, 'IFF:RNET', 'IFF:RNET')
expand(lijn[::-1], 'IFF:RNET', 'IFF:RNET')

lijn = ['gdm', 'bsd', 'ldm', 'akl', 'gr', 'bhdv', 'gnd', 'hbzm', 'sdt', 'sdtb', 'ddrs', 'ddr']
expand(lijn, 'IFF:RNET', 'IFF:RNET')
expand(lijn[::-1], 'IFF:RNET', 'IFF:RNET')



