#!/usr/bin/python
# Copyright 2016 Karwin Software Solutions LLC

"""Parse sysbench OLTP output into CSV."""

import json
import re
import sys

def parseFile(f, metric):
  for line in f:
    if ":" not in line:
      continue
    name, value = line.split(":")
    if re.match(r'^sysbench', name):
      continue
    if value.strip() == "":
      continue
    metric[name.strip()] = value.strip()

  metric["queries read"] = metric["read"] 
  metric["queries write"] = metric["write"] 
  metric["queries other"] = metric["other"]
  metric["queries total"] = metric["total"]
  del metric["read"]
  del metric["write"]
  del metric["other"]
  del metric["total"]

  r = re.compile('[ ()]+')
  metric["transactions"], metric["transactions/sec"] = r.split(metric["transactions"])[0:2]
  metric["read/write requests"], metric["read/write requests/sec"] = r.split(metric["read/write requests"])[0:2]
  metric["other operations"], metric["other operations/sec"] = r.split(metric["other operations"])[0:2]
  metric["ignored errors"], metric["ignored errors/sec"] = r.split( metric["ignored errors"])[0:2]
  metric["reconnects"], metric["reconnects/sec"] = r.split( metric["reconnects"])[0:2]

  r = re.compile('[^\d.-]+')
  metric["Target transaction rate"] = r.split(metric["Target transaction rate"])[0]
  metric["total time"] = r.split(metric["total time"])[0]
  metric["total time taken by event execution"] = r.split(metric["total time taken by event execution"])[0]
  metric["response min"] = r.split(metric["min"])[0]
  metric["response avg"] = r.split(metric["avg"])[0]
  metric["response max"] = r.split(metric["max"])[0]
  metric["response 95pct"] = r.split(metric["approx.  95 percentile"])[0]
  del metric["min"]
  del metric["avg"]
  del metric["max"]
  del metric["approx.  95 percentile"]

  metric["events avg"], metric["events stddev"] = metric["events (avg/stddev)"].split("/")
  metric["execution time avg"], metric["execution time stddev"] = metric["execution time (avg/stddev)"].split("/")
  del metric["events (avg/stddev)"]
  del metric["execution time (avg/stddev)"]

def main(args):
  args.pop(0)
  if not args:
    print >>sys.stderr, "Need at least one file in argument"
    return 1
  result = dict()
  for arg in args:
    with open(arg) as f:
      metric = {}
      parseFile(f, metric)
      for m in metric:
        if m[0] in result:
          result[m[0]][arg] = m[1]
        else:
          result[m[0]] = {arg: m[1]}

  json.dump(result, sys.stdout, indent=2)

if __name__ == "__main__":
  sys.exit(main(sys.argv))
