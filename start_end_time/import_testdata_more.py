"""
Import simple test data for testing getting itemrec
"""
import predictionio
import argparse
import datetime
import time
import random

MIN_VERSION = '0.5.0'
if predictionio.__version__ < MIN_VERSION:
    err = "Require PredictionIO Python SDK version >= %s" % MIN_VERSION
    raise Exception(err)

def datetime_to_ms(dt):
    return int(time.mktime(dt.timetuple()) * 1000 + dt.microsecond / 1000)

def import_testdata(app_key, api_url):
    client = predictionio.Client(app_key, 1, api_url)


    uids = ["u%s" % i for i in range(0, 10)]
    for uid in uids:
        client.create_user(uid)

    current_time = datetime.datetime.now()
    current_time_m2 = datetime_to_ms(current_time - datetime.timedelta(hours=2))
    current_time_m1 = datetime_to_ms(current_time - datetime.timedelta(hours=1))
    current_time_p1 = datetime_to_ms(current_time + datetime.timedelta(hours=1))
    current_time_p2 = datetime_to_ms(current_time + datetime.timedelta(hours=2))

    a_iids = ["ia%s" % i for i in range(0,10)]
    for iid in a_iids:
        client.create_item(iid, ("ta",), {"pio_startT": current_time_m2, "pio_endT": current_time_m1})
    
    b_iids = ["ib%s" % i for i in range(0,10)]
    for iid in b_iids:
        client.create_item(iid, ("ta",), {"pio_startT": current_time_m1, "pio_endT": current_time_p1})

    c_iids = ["ic%s" % i for i in range(0,10)]
    for iid in c_iids:
        client.create_item(iid, ("ta",), {"pio_startT": current_time_p1, "pio_endT": current_time_p2})

    # each user view half of the group
    for uid in uids:
        client.identify(uid)
        for iid in random.sample(a_iids, len(a_iids)/2):
            client.record_action_on_item("view", iid)

        for iid in random.sample(b_iids, len(b_iids)/2):
            client.record_action_on_item("view", iid)

        for iid in random.sample(c_iids, len(c_iids)/2):
            client.record_action_on_item("view", iid)

    client.close()
    
def main():
    parser = argparse.ArgumentParser(description="some description here..")
    parser.add_argument('--appkey', default='invalid_app_key')
    parser.add_argument('--apiurl', default="http://localhost:8000")

    args = parser.parse_args()
    print args

    import_testdata(
        app_key=args.appkey,
        api_url=args.apiurl)

if __name__ == '__main__':
    main()





