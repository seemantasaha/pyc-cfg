from utils import buildCFG

cfgs = buildCFG('structure_test.c')

for cfg in cfgs:
    print "\n[+] Function: ", cfg[0]
    print cfg[1].printer()