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
    fields = [i] * 34
    fields[1] = int(random.uniform(0, rows))
    fields[2] = int(random.uniform(0, rows))
    fields[3] = int(random.uniform(0, rows))
    for j in xrange(4,34):
      c = set()
      while len(c) < 20:
        c.add('%011d' % random.randint(0, 99999999999))
      fields[j] = '-'.join(c)
    csvout.writerow(fields)
    
if __name__ == "__main__":
  sys.exit(main(sys.argv))
