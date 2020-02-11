import httpretty
import pytest
import json

import coinbase

@httpretty.activate
def test_successful_get_currencies():
    resp_body = {
        "data": [
            {
                "id": "AED",
                "name": "United Arab Emirates Dirham",
                "min_size": "0.01000000"
            },
            {
                "id": "AFN",
                "name": "Afghan Afghani",
                "min_size": "0.01000000"
            }
        ]
    }

    httpretty.register_uri(
        httpretty.GET,
        "https://api.coinbase.com/v2/currencies",
        body=json.dumps(resp_body),
        status=200
    )

    c = coinbase.Client()
    resp = c.get_currencies()

    assert httpretty.has_request()
    assert resp_body == resp.json()

@httpretty.activate
def test_successful_get_currencies_with_custom_url():
    resp_body = {
        "data": [
            {
                "id": "AED",
                "name": "United Arab Emirates Dirham",
                "min_size": "0.01000000"
            },
            {
                "id": "AFN",
                "name": "Afghan Afghani",
                "min_size": "0.01000000"
            }
        ]
    }

    httpretty.register_uri(
        httpretty.GET,
        "http://localhost/v2/currencies",
        body=json.dumps(resp_body),
        status=200
    )

    c = coinbase.Client(base_url="http://localhost")
    resp = c.get_currencies()

    assert httpretty.has_request()
    assert resp_body == resp.json()

@httpretty.activate
def test_unsuccessful_get_currencies_http_bad_request():
    httpretty.register_uri(
        httpretty.GET,
        "http://error.url/v2/currencies",
        status=500
    )

    with pytest.raises(coinbase.HTTPBadResponse) as http_bad_response:
        c = coinbase.Client(base_url="http://error.url")
        c.get_currencies()

    assert "HTTP BadResponse, code: 500" in str(http_bad_response)

@httpretty.activate
def test_unsuccessful_get_currencies_bad_request():
    # limitation for HTTPretty callbacks https://github.com/gabrielfalcao/HTTPretty/issues/334
    def exception_callback(request, uri, headers):
        raise requests.ConnectionError()

    httpretty.register_uri(
        httpretty.GET,
        "http://time.out/v2/currencies",
        body=exception_callback,
        status=200
    )

    with pytest.raises(coinbase.BadResponse) as bad_response:
        c = coinbase.Client(base_url="http://time.out")
        c.get_currencies()

    assert "Connection aborted." in str(bad_response)
