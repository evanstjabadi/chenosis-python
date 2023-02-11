# MTN Chenosis API

> NB: Not affiliated with MTN's official Chenosis Platform (05 Jan 2023)

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

You can open issues on the GitHub repository for library-level issues and contact Chenosis support for any issues with the API itself.

### TODO List
1. Update tests and readme examples with more response data once the chenosis sandbox/production is up and running (11 Feb 2023).
2. Use pydantic for response models.
3. Add more endpoints once POC is acceptable.
4. Add more client methods.
5. Add an async client.
