Junos AE CSV to Conf

Cooper Ry Lees
<me@cooperlees.com>

In a lot of large deployments these days you need to generate a lot of ae interfaces. This can take some time.

This script was made just to generate that conf for you, genreally designed for EX/QFabric but would also work for SRX (anything that does ethernet-switching).

CSV Format:
	#Interface,Description,vlan-ids,physical-ints|physical-int2|..|physical-intX

USAGE:
	junos-aecsv-to-conf.py CSV_FILE
	e.g.
		junos-aecsv-to-conf.py ae.csv
