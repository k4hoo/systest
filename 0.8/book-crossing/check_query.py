import predictionio
import time

import random

SEED = 3

random.seed(SEED)

def test(engine_client, num):
  for i in range(num):
    r = engine_client.send_query({
      "user": "62325",
      "items": ["1558746218", "0515132896", "3453126467", "0793827957", "1852276843", "0060938412", "1569871213", "3257203659",
"0804111359", "0972044205"]
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
