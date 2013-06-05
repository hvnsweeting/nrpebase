#!/usr/bin/env python
import os
import sys
from jinja2 import Environment, FileSystemLoader

if __name__ == "__main__":
    force = None
    if len(sys.argv) >= 4:
        dest = sys.argv[1]
        appname = sys.argv[2]
        cfg_type = sys.argv[3]
        if cfg_type not in ('nrpe', 'diamond'):
            sys.exit('cfg_type must be nrpe or diamond')
    if len(sys.argv) == 5:
        if sys.argv[4] == "-f":
            force = sys.argv[4]
    if len(sys.argv) not in (4, 5):
        print "USAGE: {0} dir_path appname TYPE [-f]".format(__file__)
        sys.exit(1)

    TEMPLATE_DIR = os.path.abspath(os.path.join(
                                   os.path.dirname(__file__), cfg_type))
    nrpe_dir = os.path.join(dest, cfg_type)
    try:
        os.mkdir(nrpe_dir)
    except OSError as e:
        if not force:
            print ("{0} dir existed, use "
                   "'{1} dir_path appname TYPE -f' to overwrite it").format(
                           cfg_type, __file__)
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
