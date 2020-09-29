import os
import zipfile
import tempfile
import argparse
import logging
import shutil
import sys


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG, filename=u'log.log')

parser = argparse.ArgumentParser()
parser.add_argument('-n', dest="name", help="zip name", type=str)
args = parser.parse_args()

goal = "__init__.py"


try:
    with zipfile.ZipFile(args.name, 'r') as zf:
        tmpdir = tempfile.mkdtemp()
        zf.extractall(tmpdir)
        logging.debug(f'temp was created: {tmpdir}')
        logging.debug(f'{args.name} extracted in {tmpdir}')
except Exception as err:
    logging.error(err)
    sys.exit(1)

for dirpath, dirnames, files in os.walk(tmpdir):
    if goal not in files and goal not in dirnames:
        shutil.rmtree(dirpath)
        logging.info(f"removed catalog {dirpath}")

with zipfile.ZipFile(args.name.replace(".zip", "_new.zip"), "w") as zf:
    for dirpath, dirnames, files in os.walk(tmpdir):
        for filename in files:
            filepath = os.path.join(dirpath, filename)
            path = filepath.replace(tmpdir, "", 1)
            zf.write(filepath, path)
logging.debug(f"{args.name}_new.zip was created")
logging.debug(f"{tmpdir} was removed")
