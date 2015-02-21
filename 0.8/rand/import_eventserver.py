"""
Import sample data for similar product engine
"""

import predictionio
import argparse
import random
import time

SEED = 3

NUM_OF_USER = 100000
NUM_OF_ITEM = 100000
NUM_OF_CAT = 10
MIN_NUM_CAT_PER_ITEM = 1
MAX_NUM_CAT_PER_ITEM = 6
NUM_OF_VIEW_PER_USER = 10
RANDOM_BUY = True

def import_events(client):
  random.seed(SEED)
  count = 0
  print client.get_status()
  print "Importing data..."

  # generate 10 users, with user ids u1,u2,....,u10
  user_ids = ["u%s" % i for i in range(1, NUM_OF_USER + 1)]
  for user_id in user_ids:
    #print "Set user", user_id
    client.acreate_event(
      event="$set",
      entity_type="user",
      entity_id=user_id
    )
    count += 1

  # generate 50 items, with item ids i1,i2,....,i50
  # random assign 1 to 4 categories among c1-c6 to items
  categories = ["c%s" % i for i in range(1, NUM_OF_CAT + 1)]
  item_ids = ["i%s" % i for i in range(1, NUM_OF_ITEM + 1)]
  for item_id in item_ids:
    #print "Set item", item_id
    client.acreate_event(
      event="$set",
      entity_type="item",
      entity_id=item_id,
      properties={
        "categories" : random.sample(categories,
          random.randint(MIN_NUM_CAT_PER_ITEM, MAX_NUM_CAT_PER_ITEM))
      }
    )
    count += 1

  # each user randomly viewed 10 items
  for user_id in user_ids:
    for viewed_item in random.sample(item_ids, NUM_OF_VIEW_PER_USER):
      #print "User", user_id ,"views item", viewed_item
      client.acreate_event(
        event="view",
        entity_type="user",
        entity_id=user_id,
        target_entity_type="item",
        target_entity_id=viewed_item
      )
      count += 1
      # randomly buy some of the viewed item
      if RANDOM_BUY and random.choice([True, False]):
        client.acreate_event(
          event="buy",
          entity_type="user",
          entity_id=user_id,
          target_entity_type="item",
          target_entity_id=viewed_item
        )
        count += 1

  print "%s events are imported." % count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for similar product engine")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")

  args = parser.parse_args()
  print args

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=2,
    qsize=200)

  start_time = time.time()
  import_events(client)
  client.close()
  end_time = time.time()
  print "time: %f" % (end_time - start_time)
