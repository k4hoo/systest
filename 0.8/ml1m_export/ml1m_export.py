"""
Export ML-1m data set data to PredictionIO Event API JSON file for batch import
"""
import predictionio
import csv
import re
import math
import argparse
from sets import Set

ITEMS_FILE = "ml-1m/movies.dat"
RATING_FILE = "ml-1m/ratings.dat"

def export_events(exporter):
  all_users = Set()

  count = 0
  print "Exporting data..."

  id_check = r'.*[\t,].*'

  # startup_id,name,url,incubator,markets
  print 'Exporting items...'
  with open(ITEMS_FILE, 'r') as f:
    #reader = csv.reader(f, delimiter='::')
    reader = csv.reader((line.replace('::', ':') for line in f), delimiter=':')
    firstline = False
    for line in reader:
      if firstline:
        firstline = False
      else:
        #print line
        iid = line[0]
        name = line[1]
        categories = line[2].split("|")
        if re.match(id_check, iid):
          print 'iid: "%s" contains tab or comma. Skip this item.' % iid
        else:
          try:
            exporter.create_event(
              event="$set",
              entity_type="item",
              entity_id=iid,
              properties={
                "name": name,
                "categories": categories
              }
            )
            count += 1
          except:
            print 'cannot create event for this %s' % line

  print 'Exporting actions...'
  with open(RATING_FILE, 'r') as f:
    #reader = csv.reader(f, delimiter='::')
    reader = csv.reader((line.replace('::', ':') for line in f), delimiter=':')
    firstline = False
    for line in reader:
      if firstline:
        firstline = False
      else:
        #print line
        uid = line[0]
        all_users.add(uid)
        iid = line[1]
        rating = line[2]
        if re.match(id_check, uid) or re.match(id_check, iid):
          print 'uid: "%s" or iid "%s" contains tab or comms." \
            " Skip this action.' % (uid, iid)
        else:
          exporter.create_event(
            event="rate",
            entity_type="user",
            entity_id=uid,
            target_entity_type="item",
            target_entity_id=iid,
            properties={
              "rating" : float(rating)
            }
          )
          count += 1

  print 'Exporting users...'
  for uid in all_users:
    if re.match(id_check, uid):
      print 'uid: "%s" contains tab or comma. Skip this user.' % uid
    else:
      exporter.create_event(
        event="$set",
        entity_type="user",
        entity_id=uid
      )
      count += 1

  print "%s events are exported." % count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="some description here..")
  parser.add_argument('--file_name', default='invald_file_name')

  args = parser.parse_args()
  print args

  exporter = predictionio.FileExporter(
    file_name=args.file_name)
  export_events(exporter)
  exporter.close()
