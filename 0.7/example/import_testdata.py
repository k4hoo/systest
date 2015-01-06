"""
Import simple test data for testing getting itemrec
"""
import predictionio
import argparse

MIN_VERSION = '0.5.0'
if predictionio.__version__ < MIN_VERSION:
    err = "Require PredictionIO Python SDK version >= %s" % MIN_VERSION
    raise Exception(err)

def import_testdata(app_key, api_url):
    client = predictionio.Client(app_key, 1, api_url)

    client.create_user("u1")
    client.create_user("u2")
    client.create_user("u3")

    client.create_item("grape", ("fruit",))
    client.create_item("strawberry", ("fruit",))
    client.create_item("watermelon", ("fruit",))
    client.create_item("orange", ("fruit",))

    ##
    client.identify("u1")
    client.record_action_on_item("view", "grape")
    client.record_action_on_item("view", "watermelon")
    client.record_action_on_item("view", "orange")

    client.identify("u2")
    client.record_action_on_item("view", "grape")
    client.record_action_on_item("view", "watermelon")

    client.identify("u3")
    client.record_action_on_item("view", "watermelon")

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
