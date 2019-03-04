# Pushdata Python client library

## Installation

`pip install pushdata-io`

## Usage

```python
import pushdata

# 1. Initialize with no authentication
# Initialize with our account email and time series name we want to use
pd = pushdata.Client(email="myemail@example.com", tsname="mytimeseries")

# 2. ...or initialize with authentication (for account with security=on)
pd = pushdata.Client(apikey="thd8JT73LsB8jah0F4d9", tsname="mytimeseries")

# Send a data point to the time series
pd.send(4711)

# Send to another time series by overriding tsname
pd.send(4711, tsname="myothertimeseries")

# Retrieve all data from the time series
tsdata = pd.recv()

# Retrieve data timestamped during the last week
import datetime
one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
tsdata = pd.recv(fromtime=one_week_ago)

# Retrieve data for one 24-hour period, one week ago
import datetime
one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
one_week_ago_plus_24h = one_week_ago + datetime.timedelta(days=1)
tsdata = pd.recv(fromtime=one_week_ago, totime=one_week_ago_plus_24h)

# Print time series data
print("Timeseries name: " + tsdata["name"])
print("First point recorded at   : " + tsdata["first"])    # timestamp of first point in time series
print("Last point recorded at    : " + tsdata["last"])     # timestamp of last point in time series
print("Total number of points    : " + tsdata["total"])    # total number of points in timeseries
print("Number of points returned : " + tsdata["returned"]) # number of points returned in this call
print("---- Points ----")
for point in tsdata["points"]:
    print("Time=%s value=%f" % (point["time"], point["value"]))

#
# tsdata (returned from pd.recv()) is a dictionary that looks like this:
#  {
#     "name": "mytimeseries",
#     "first": datetime.datetime,
#     "last": datetime.datetime,
#     "total": 482,
#     "returned: 482,
#     "offset": 0,
#     "limit": 10000,
#     "points": [
#        {
#           "time": datetime.datetime,
#           "value": 4711.0
#        },
#        ...
#     ]
#  }
#
```

