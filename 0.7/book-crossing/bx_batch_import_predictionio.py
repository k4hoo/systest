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

def import_data(app_key, api_url, threads=25, req_qsize=500):

    APP_KEY = app_key
    API_URL = api_url
    THREADS = threads
    REQUEST_QSIZE = req_qsize

    client = predictionio.Client(APP_KEY, THREADS, API_URL, qsize=REQUEST_QSIZE)

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
                    client.acreate_user(uid)
    print 'Done.'

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
                itypes = ('book',)
                if re.match(id_check, iid):
                    print 'iid: "%s" contains tab or comma. Skip this item.' % iid
                else:
                    client.acreate_item(iid, itypes)
    print 'Done.'

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
                    print 'uid: "%s" or iid "%s" contains tab or comms. Skip this action.' % (uid, iid)
                else:
                    if (rating == "0"):
                        client.identify(uid)
                        client.arecord_action_on_item("view", iid)
                    else:
                        normalized_rating = int(math.ceil(float(rating)*5/10)) # convet to 1-5 scale
                        client.identify(uid)
                        client.arecord_action_on_item("rate", iid, { 'pio_rate': normalized_rating } )
    print 'Done.'

    client.close()


def main():
    parser = argparse.ArgumentParser(description="some description here..")
    parser.add_argument('--appkey', default='invalid_app_key')
    parser.add_argument('--apiurl', default="http://localhost:8000")

    args = parser.parse_args()
    print args

    import_data(
        app_key=args.appkey,
        api_url=args.apiurl)

if __name__ == '__main__':
    main()

