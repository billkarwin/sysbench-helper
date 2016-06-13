#!/usr/bin/python
# Copyright 2016 Karwin Software Solutions LLC

"""Generate rows of sysbench test data in CSV format."""

import random
import csv
import sys

def main(args):
  args.pop(0)
  if not args:
    print >>sys.stderr, "Usage: create-data.py <rows> <partition>"
    return 1
  rows = int(args.pop(0))
  partition = int(args.pop(0))
  outputfile = args.pop(0)
  if outputfile:
    outfd = open(outputfile, "w")
  else:
    outfd = sys.stdout

  csvout = csv.writer(outfd)
  random.seed(8675309+partition)
  for i in xrange(rows * (partition-1) + 1, rows * partition):
    k = int(random.uniform(0, 1000000))
    c = set()
    while len(c) < 10:
      c.add('%011d' % random.randint(0, 99999999999))
    cstr = '-'.join(c)
    pad = set()
    while len(pad) < 1000:
      pad.add('%011d' % random.randint(0, 99999999999))
    padstr = '-'.join(pad)
    csvout.writerow([i,k,cstr,padstr])
    
if __name__ == "__main__":
  sys.exit(main(sys.argv))
