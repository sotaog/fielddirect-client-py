# Field Direct API Client Python

A python client for accessing the (Field Direct API)[https://apps.fielddirect.com/DataServices/]. This is bascially a wrapper around (pyodata)[https://pyodata.readthedocs.io/en/latest/index.html] to make handle the unique authentication in Field Direct.

# Installation

`pip install -U fielddirect-client-py`

# Usage

```python
import Client from fielddirectclient

client = Client(userid, password, appkey)
service = client.odata

lmrs = service.entity_sets.DocLiquidMeterReadings.get_entities().execute()
for lmr in lmrs:
    print(lmr.MeterPtID)
```
See the (pyodata documentation)[https://pyodata.readthedocs.io/en/latest/index.html] for more information on how to use.
