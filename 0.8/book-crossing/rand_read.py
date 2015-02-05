import predictionio
import time
import csv
import re
import random

USERS_FILE = "BX-Users.csv"
ITEMS_FILE = "BX-Books.csv"
SEED = 3
random.seed(SEED)

id_check = r'.*[\t,].*'

num = 20
users = []
print 'Randomly pick 100 users...'
with open(USERS_FILE, 'r') as f:
  reader = csv.reader(f, delimiter=';')
  count = 0
  skip_firstline = True
  for line in reader:
    if (count == num):
      break

    if skip_firstline:
      skip_firstline = False
    else:
      uid = line[0]
      if re.match(id_check, uid):
        print 'uid: "%s" contains tab or comma. Skip this user.' % uid
      else:
        if (random.randint(0, 2) == 1):
          users.append(uid)
          count += 1

num = 20
items = []
print 'Randomly pick 500 items...'
with open(ITEMS_FILE, 'r') as f:
  reader = csv.reader(f, delimiter=';')
  count = 0
  skip_firstline = True
  for line in reader:
    if (count == num):
      break

    if skip_firstline:
      skip_firstline = False
    else:
      iid = line[0]
      if re.match(id_check, iid):
        print 'iid: "%s" contains tab or comma. Skip this user.' % uid
      else:
        if (random.randint(0, 2) == 1):
          items.append(iid)
          count += 1

print users
print items

def test(engine_client, n):
  for i in range(n):
    r = engine_client.send_query({
      "user": random.choice(users),
      "items": random.sample(items, 10)
    })
  return r

engine_client = predictionio.EngineClient(url="http://localhost:8000")

n = 200
before = time.time()
r = test(engine_client, n)
after = time.time()
print r
average = float(after-before)/num
print "average time per query %.5f s" % average
