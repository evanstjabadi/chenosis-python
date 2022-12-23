# MTN Chenosis API

> NB: Not affiliated with MTN's official Chenosis Platform (23 Dec 2022)

A python client for MTN's Chenosis platform: https://chenosis.io.

## Installation

`pip install chenosis`

## Usage

```python
from chenosis.client import ChenosisClient

chenosis_client = ChenosisClient(
    host="https://sandbox.api.chenosis.io", # Use live API when going to production
    client_id="xxxxxx",
    client_secret="yyyyyy"
)

# GET user's get_mobile_carrier_details
phone_number = "27123456789"
response = chenosis_client.get_mobile_carrier_details(phone_number=phone_number)
print(response)
# TODO: Put correct information
```

## Reporting Issues:
 # Copy stock library 

