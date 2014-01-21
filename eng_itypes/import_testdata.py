"""
Import simple test data for testing getting itemrec
"""
import predictionio

APP_KEY = "Y5SZlskydmF4f02ro3fqmBYVA3fb3wpJ26LSwWIEMXzJhXXPvbKvPLka5DpFlkoc"
API_URL = "http://localhost:8000"

MIN_VERSION = '0.5.0'
if predictionio.__version__ < MIN_VERSION:
    err = "Require PredictionIO Python SDK version >= %s" % MIN_VERSION
    raise Exception(err)

if __name__ == "__main__":
    client = predictionio.Client(APP_KEY, 1, API_URL)

    client.create_user("u0")
    client.create_user("u1")
    client.create_user("u2")
    client.create_user("u3")

    client.create_item("ia0", ("ta",), {"custom1": "i0c1"})
    client.create_item("ia1", ("ta",), {"custom1": "i1c1", "custom2": "i1c2"})
    client.create_item("ia2", ("ta",), {"custom2": "i2c2"})
    client.create_item("ia3", ("ta",))

    client.create_item("ib0", ("tb",), {"custom1": "i0c1"})
    client.create_item("ib1", ("tb",), {"custom1": "i1c1", "custom2": "i1c2"})
    client.create_item("ib2", ("tb",), {"custom2": "i2c2"})
    client.create_item("ib3", ("tb",))

    ## 
    client.identify("u0")
    client.record_action_on_item("rate", "ia0", { "pio_rate": 2 })
    client.record_action_on_item("rate", "ia1", { "pio_rate": 3 })
    client.record_action_on_item("rate", "ia2", { "pio_rate": 4 })
    
    client.identify("u1")
    client.record_action_on_item("rate", "ia2", { "pio_rate": 4 })
    client.record_action_on_item("rate", "ia3", { "pio_rate": 1 })

    client.identify("u2")
    client.record_action_on_item("rate", "ia1", { "pio_rate": 2 })
    client.record_action_on_item("rate", "ia2", { "pio_rate": 1 })
    client.record_action_on_item("rate", "ia3", { "pio_rate": 3 })

    client.identify("u3")
    client.record_action_on_item("rate", "ia0", { "pio_rate": 5 })
    client.record_action_on_item("rate", "ia1", { "pio_rate": 3 })
    client.record_action_on_item("rate", "ia3", { "pio_rate": 2 })

    ##
    client.identify("u0")
    client.record_action_on_item("rate", "ib0", { "pio_rate": 2 })
    client.record_action_on_item("rate", "ib1", { "pio_rate": 3 })
    client.record_action_on_item("rate", "ib2", { "pio_rate": 4 })
    
    client.identify("u1")
    client.record_action_on_item("rate", "ib2", { "pio_rate": 4 })
    client.record_action_on_item("rate", "ib3", { "pio_rate": 1 })

    client.identify("u2")
    client.record_action_on_item("rate", "ib1", { "pio_rate": 2 })
    client.record_action_on_item("rate", "ib2", { "pio_rate": 1 })
    client.record_action_on_item("rate", "ib3", { "pio_rate": 3 })

    client.identify("u3")
    client.record_action_on_item("rate", "ib0", { "pio_rate": 5 })
    client.record_action_on_item("rate", "ib1", { "pio_rate": 3 })
    client.record_action_on_item("rate", "ib3", { "pio_rate": 2 })

    client.close()
    




