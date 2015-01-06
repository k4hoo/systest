"""
Import Book-crossing data set data into PredictionIO
"""
import predictionio
import Queue
import csv
import re
import math
import argparse

USERS_FILE = "BX-Users.csv"
ITEMS_FILE = "BX-Books.csv"
FOLLOW_ACTIONS_FILE = "BX-Book-Ratings.csv"

def import_events(client):
  count = 0
  print client.get_status()
  print "Importing data..."

  id_check = r'.*[\t,].*'

  print 'Importing users...'
  with open(USERS_FILE, 'r') as f:
    reader = csv.reader(f, delimiter=';')
    firstline = True
    for line in reader:
      if firstline:
        firstline = False
      else:
        uid = line[0]
        if re.match(id_check, uid):
          print 'uid: "%s" contains tab or comma. Skip this user.' % uid
        else:
          client.acreate_event(
            event="$set",
            entity_type="user",
            entity_id=uid
          )
          count += 1

  # startup_id,name,url,incubator,markets
  print 'Importing items...'
  with open(ITEMS_FILE, 'r') as f:
    reader = csv.reader(f, delimiter=';')
    firstline = True
    for line in reader:
      if firstline:
        firstline = False
      else:
        iid = line[0]
        itypes = ["book"]
        if re.match(id_check, iid):
          print 'iid: "%s" contains tab or comma. Skip this item.' % iid
        else:
          client.acreate_event(
            event="$set",
            entity_type="item",
            entity_id=iid,
            properties={
              "categories": itypes
            }
          )
          count += 1

  print 'Importing actions...'
  with open(FOLLOW_ACTIONS_FILE, 'r') as f:
    reader = csv.reader(f, delimiter=';')
    firstline = True
    for line in reader:
      if firstline:
        firstline = False
      else:
        uid = line[0]
        iid = line[1]
        rating = line[2] # expressed on a scale from 1-10
        if re.match(id_check, uid) or re.match(id_check, iid):
          print 'uid: "%s" or iid "%s" contains tab or comms." \
            " Skip this action.' % (uid, iid)
        else:
          client.acreate_event(
            event="view",
            entity_type="user",
            entity_id=uid,
            target_entity_type="item",
            target_entity_id=iid
          )
          count += 1

  client.close()


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="some description here..")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")

  args = parser.parse_args()
  print args

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=50,
    qsize=500)
  import_events(client)
