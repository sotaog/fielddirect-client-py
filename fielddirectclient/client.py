import logging
import requests

import pyodata

from .client_error import ClientError

logger = logging.getLogger('fielddirect-client')

class Client():

    def __init__(self, userid, password, appkey, url='https://apps.fielddirect.com/DataServices/'):
        self.url = url
        self.userid = userid
        self.password = password
        self.appkey = appkey
        self.session = requests.session()
        self.authenticate()

    def authenticate(self):
        resp = self.session.post('{}/api/Account/Login'.format(self.url), json={'UserId': self.userid, 'Password': self.password, 'AppKey': self.appkey})
        if resp.status_code == 200:
            data = resp.json()
            self.session.headers.update({'Authorization': 'Basic {}'.format(data['SecurityToken'])})
            self.odata = pyodata.Client('{}/OData'.format(self.url), self.session)
        else:
            raise ClientError('Unable to authenticate to Field Direct')
