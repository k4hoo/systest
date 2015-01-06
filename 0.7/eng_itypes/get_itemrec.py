import predictionio
import time
import argparse

def get_itemrec(app_key, api_url, eng_name):
    client = predictionio.Client(app_key, 1, api_url)

    uids = ["u0", "u1", "u2", "u3"]
    print eng_name
    for u in uids:
        try:
            itemrec = client.get_itemrec(u, 10, eng_name)
            print itemrec
        except Exception as e:
            print e
            pass

    client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="some description here..")
    parser.add_argument('--appkey', default='invalid_app_key')
    parser.add_argument('--apiurl', default="http://localhost:8000")
    parser.add_argument('--engine', default="invalid_engine_name")

    args = parser.parse_args()
    print args

    get_itemrec(
        app_key=args.appkey,
        api_url=args.apiurl,
        eng_name=args.engine)
    

