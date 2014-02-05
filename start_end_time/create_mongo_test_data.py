import pymongo
from pymongo import MongoClient
import datetime

def ms_to_datetime(ms):
    """
    Convert ms in integer to datetime.datetime
    """
    # fromtimestamp() takes seconds
    dt = datetime.datetime.fromtimestamp(ms/1000).replace(microsecond=ms%1000*1000)
    return dt

def create_test_data():
    client = MongoClient("localhost", 27017)
    db = client['test']
    coll = db['items']

    obj1 = {
        '_id': '1_i1',
        'itypes' : ['t1', 't2'],
        'appid' : 1,
        'starttime' : ms_to_datetime(12345679001),
        'endtime' : ms_to_datetime(12345679101),
        'ct': ms_to_datetime(987654321001),
        'attr1': 'apple'
    }
    coll.save(obj1)

    obj2 = {
        '_id': '1_i2',
        'itypes' : ['t1', 't2'],
        'appid' : 1,
        'starttime' : ms_to_datetime(12345679002),
        'ct': ms_to_datetime(987654321002),
        'attr1': 'orange'
    }
    coll.save(obj2)

    obj3 = {
        '_id': '1_i3',
        'itypes' : ['t1', 't2'],
        'appid' : 1,
        'starttime' : ms_to_datetime(12345679003),
        'endtime' : ms_to_datetime(12345679103),
        'ct': ms_to_datetime(987654321003),
        'attr2': 'cat'
    }
    coll.save(obj3)

    obj4 = {
        '_id': '1_i4',
        'itypes' : ['t1', 't2'],
        'appid' : 1,
        'starttime' : ms_to_datetime(12345679004),
        'ct': ms_to_datetime(987654321004),
        'attr2': 'dog',
        'attr1': 'apple2'
    }
    coll.save(obj4)

    obj5 = {
        '_id': '1_i5',
        'itypes' : ['t1', 't2'],
        'appid' : 1,
        'starttime' : ms_to_datetime(12345679005),
        'endtime' : ms_to_datetime(12345679105),
        'ct': ms_to_datetime(987654321005)
    }
    coll.save(obj5)

    obj5 = {
        '_id': '1_i6',
        'itypes' : ['t1', 't2'],
        'appid' : 1,
        'starttime' : ms_to_datetime(12345679006),
        'ct': ms_to_datetime(987654321006)
    }
    coll.save(obj5)

if __name__ == '__main__':
    create_test_data()
