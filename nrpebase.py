#!/usr/bin/env python
import os
import sys
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))

if __name__ == "__main__":
	force = None
	if len(sys.argv) >= 3:
		dest = sys.argv[1]
		appname = sys.argv[2]
	if len(sys.argv) == 4:
		if sys.argv[3] == "-f":
			force = sys.argv[3]
	if len(sys.argv) not in (3, 4):
		print "USAGE: nrpebase dir_path appname [-f]'"
		sys.exit(1)

	nrpe_dir = os.path.join(dest, 'nrpe')
	try:
		os.mkdir(nrpe_dir)
	except OSError as e:
		if not force:
			print ("NRPE dir existed, use "
				   "'nrpebase dir_path appname -f' to overwrite it")
			sys.exit(1)
		else:
			pass
	env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
	for fn in os.listdir(TEMPLATE_DIR):
		template1 = env.get_template(fn)
		rendered = template1.render(app=appname)
		with open(os.path.join(nrpe_dir, fn), 'wt') as f:
			f.writelines(rendered)
	print "Done"
