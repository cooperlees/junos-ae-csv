#!/usr/bin/python

#######################################
# Cooper Lees <me@cooperlees.com>
# Convert a CSV to EX/QFbric Vlan Syntax
# Last Updated: 20120820
#######################################

import re, sys

aeConf = 'set interfaces $AEINT$ description "$DESC$"\n\
set interfaces $AEINT$ mtu 9192\n\
set interfaces $AEINT$ aggregated-ether-options lacp active\n\
set interfaces $AEINT$ unit 0 family ethernet-switching port-mode trunk\n\
set interfaces $AEINT$ unit 0 family ethernet-switching vlan members [ BRD_MGT $OTHERVLANS$ ]'

phyConf = "set interfaces $PHY$ ether-options 802.3ad $AEINT$"

aeReg = re.compile("\$AEINT\$")
descReg = re.compile("\$DESC\$")
vlanReg = re.compile("\$OTHERVLANS\$")
phyReg = re.compile("\$PHY\$")


def printConf(data):
    INTS = data[3].split("|")

    # re.sub(pattern, repl, string, count=0, flags=0)
    ae = aeReg.sub(data[0], aeConf)
    ae = descReg.sub(data[1], ae)
    ae = vlanReg.sub(data[2], ae)
    print ae
    for aInt in INTS:
        tempInt = phyReg.sub(aInt, phyConf)
        tempInt = aeReg.sub(data[0], tempInt)
        print tempInt

    print ""
    return True


csvf = open(sys.argv[1], "r")
for line in csvf:
    if line[0][0:] == "#":
        continue
    line = line.strip()
    data = line.split(",")
    # 	print data #DEBUG
    printConf(data)

csvf.close()
