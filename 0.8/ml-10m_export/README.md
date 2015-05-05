# Use SDK to export data to json file for batch import

## get data set

```
$ wget http://files.grouplens.org/datasets/movielens/ml-10m.zip
```

## create json file

```
$ python ml-10m_export.py --file_name ml-10m-event.json
```

## batch import

```
$ pio import --appid <YOUR_APP_ID> --input ml-10m-event.json
```
