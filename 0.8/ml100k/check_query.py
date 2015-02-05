import predictionio
import time

import random

SEED = 3

random.seed(SEED)

def test(engine_client, num):
  for i in range(num):
    r = engine_client.send_query({
      "user": "1",
      "items": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    })
  return r

engine_client = predictionio.EngineClient(url="http://localhost:8000")

num = 200
before = time.time()
r = test(engine_client, num)
after = time.time()
print r
average = float(after-before)/num
print "average time per query %.5f s" % average
