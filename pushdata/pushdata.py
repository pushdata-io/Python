
import datetime
import requests
import json

class Client:
    def __init__(self, email="", apikey="", tsname=""):
        if email == "" and apikey == "":
            raise ValueError("pushdata::Client(): You must supply either email or apikey when creating a Client instance")
        self.email = email
        self.apikey = apikey
        self.tsname = tsname
    def send(self, value, time=datetime.datetime.now(), tsname=""):
        if tsname == "":
            tsname = self.tsname
        if tsname == "":
            raise ValueError("pushdata::Client(): send(): You must supply a timeseries name")
        url = 'https://pushdata.io/api/timeseries?'
        if self.apikey != "":
            url += ('apikey=' + self.apikey)
        elif self.email != "":
            url += ('email=' + self.email)
        payload = {
            'name': tsname,
            'points': [ { 'time': self._rfc3339(time), 'value': value } ]
        }
        return requests.post(url, data = json.dumps(payload))
    def recv(self, tsname="", fromtime=datetime.datetime.utcfromtimestamp(0),
        totime=datetime.datetime.now(), offset=0, limit=0):
        if tsname == "":
            tsname = self.tsname
        if tsname == "":
            raise ValueError("pushdata::Client(): recv(): You must supply a timeseries name")
        url = 'https://pushdata.io/api/timeseries?'
        if self.apikey != "":
            url += ('apikey=' + self.apikey)
        elif self.email != "":
            url += ('email=' + self.email)
        url += ('&tsname=' + tsname)
        url += ('&from=' + self._rfc3339(fromtime))
        url += ('&to=' + self._rfc3339(totime))
        url += ("&offset=%d" % offset)
        url += ("&limit=%d" % limit)
        return requests.get(url)
    def _rfc3339(self, t):
        return t.isoformat("T") + "Z"

