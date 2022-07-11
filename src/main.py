import os
import sys
from argparse import ArgumentParser
from importlib import import_module

if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')
    
if os.path.exists('libs.zip'):
    sys.path.insert(0, 'libs.zip')
else:
    sys.path.insert(0, './libs')

env = os.environ.get('ENVIRON')
src_dir = os.environ.get('SRC_DIR')
tgt_dir = os.environ.get('TGT_DIR')

  
parser = ArgumentParser()
parser.add_argument('--job', type=str, required=True)
parser.add_argument('--job-args', nargs='*')
args = parser.parse_args()

job_module = import_module('jobs.%s' % args.job)

result = job_module.handler(env, args.job, src_dir, tgt_dir)
print(f'Result is = {result}')
    