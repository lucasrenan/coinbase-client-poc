# Get currencies list from Coinbase

This app is a POC for pulling data from Coinbase API. Currently, it supports only `/v2/currencies` [endpoint](https://developers.coinbase.com/api/v2#get-currencies), but support for other endpoints can be added later if needed.

The app was developed and tested using Python 3.8.1 on Linux Alpine 3.11.

## Running with Docker

We strongly encourage the use of `make` and `docker` for running the app.

### Building the Docker image

`make build`

### Running

`make run`

### Running tests

`make test`

## Running without Docker

If you don't want to run it with Docker, you can:

```
pip install -r requirements.txt
python main.py
```

### Running tests

```
pytest
```

## Logs

Logs can be found inside the `logs` folder e.g `logs/development.log`
