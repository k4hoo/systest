"""
Import simple test data for testing getting itemrec with dedup
"""
import predictionio
import argparse
import datetime
import time

MIN_VERSION = '0.5.0'
if predictionio.__version__ < MIN_VERSION:
    err = "Require PredictionIO Python SDK version >= %s" % MIN_VERSION
    raise Exception(err)

def datetime_to_ms(dt):
    return int(time.mktime(dt.timetuple()) * 1000 + dt.microsecond / 1000)

def import_testdata(app_key, api_url):
    client = predictionio.Client(app_key, 1, api_url)

    client.create_user("u0")
    client.create_user("u1")
    client.create_user("u2")
    client.create_user("u3")

    current_time = datetime.datetime.now()
    current_time_p1day = current_time + datetime.timedelta(1)

    """
    client.create_item("i0", ("ta",), {"pio_startT": 12345667, "pio_endT": datetime_to_ms(current_time_p1day), "custom1": "i0c1"})
    client.create_item("i1", ("ta", "tb"), {"pio_startT": 12345677, "pio_endT": datetime_to_ms(current_time_p1day), "custom1": "i1c1", "custom2": "i1c2"})
    client.create_item("i2", ("ta",), {"pio_startT": 12345687, "pio_endT": datetime_to_ms(current_time), "custom2": "i2c2"})
    client.create_item("i3", ("ta", "tb"), {"pio_startT": 12345697 })
    """

    client.create_item("i0", ("ta",), {"pio_startT": 12345667, "attr1": "g1", "attr2": "x1"})
    client.create_item("i1", ("ta", "tb"), {"pio_startT": 12345677, "attr1": "g1", "attr2": "x2"})
    client.create_item("i2", ("ta",), {"pio_startT": 12345687, "attr1": "g2", "attr2" : "x3"})
    client.create_item("i3", ("ta", "tb"), {"pio_startT": 12345697, "attr1": "g3", "attr2": "x2" })
    client.create_item("i4", ("ta", "tb"), {"pio_startT": 12345697, "attr1": "g1", "attr2": "x1" })
    client.create_item("i5", ("ta", "tb"), {"pio_startT": 12345697, "attr1": "g3", "attr2": "x3" })
    client.create_item("i6", ("ta", "tb"), {"pio_startT": 12345697, "attr1": "g2", "attr2": "x1" })
    client.create_item("i7", ("ta", "tb"), {"pio_startT": 12345697, "attr1": "g3", "attr2": "x2" })

    ##
    client.identify("u0")
    client.record_action_on_item("rate", "i0", { "pio_rate": 2 })
    client.record_action_on_item("rate", "i1", { "pio_rate": 3 })
    client.record_action_on_item("rate", "i2", { "pio_rate": 4 })
    client.record_action_on_item("conversion", "i2")
    client.record_action_on_item("conversion", "i6")
    client.record_action_on_item("rate", "i7", { "pio_rate": 5 })

    client.identify("u1")
    client.record_action_on_item("rate", "i2", { "pio_rate": 4 })
    client.record_action_on_item("rate", "i3", { "pio_rate": 1 })
    client.record_action_on_item("rate", "i6", { "pio_rate": 2 })
    client.record_action_on_item("conversion", "i3")
    client.record_action_on_item("conversion", "i7")

    client.identify("u2")
    client.record_action_on_item("rate", "i1", { "pio_rate": 2 })
    client.record_action_on_item("rate", "i2", { "pio_rate": 1 })
    client.record_action_on_item("rate", "i3", { "pio_rate": 3 })
    client.record_action_on_item("rate", "i6", { "pio_rate": 1 })
    client.record_action_on_item("conversion", "i4")
    client.record_action_on_item("conversion", "i5")

    client.identify("u3")
    client.record_action_on_item("rate", "i0", { "pio_rate": 5 })
    client.record_action_on_item("rate", "i1", { "pio_rate": 3 })
    client.record_action_on_item("rate", "i3", { "pio_rate": 2 })
    client.record_action_on_item("conversion", "i0")
    client.record_action_on_item("conversion", "i5")
    client.record_action_on_item("conversion", "i7")

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
