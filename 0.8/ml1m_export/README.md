# Use SDK to export data to json file for batch import

## get data set

```
$ wget http://files.grouplens.org/datasets/movielens/ml-1m.zip
```

## create json file

```
$ python ml1m_export.py --file_name ml1m-event.json
```

## batch import

```
$ pio import --appid <YOUR_APP_ID> --input ml1m-event.json
```
