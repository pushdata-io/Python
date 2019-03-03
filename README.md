# Pushdata Python client library

## Installation

`pip install pushdata`

## Usage

### No authentication

```python
import pushdata

# Send a data point to a time series
pushdata.send(4711, email="myemail@example.com", tsname="mytimeseries")

# Retrieve data from a time series
tsdata = pushdata.recv(

```