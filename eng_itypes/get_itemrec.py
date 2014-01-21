import predictionio
import time

APP_KEY = "Y5SZlskydmF4f02ro3fqmBYVA3fb3wpJ26LSwWIEMXzJhXXPvbKvPLka5DpFlkoc" # replace this with your AppKey
API_URL = "http://localhost:8000" # PredictoinIO Server

if __name__ == "__main__":
    client = predictionio.Client(APP_KEY, 1, API_URL)

    itemrec = client.get_itemrec("u0", 10, "t1")
    print itemrec

    client.close()