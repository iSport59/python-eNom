'''Wrapper for eNom API'''

import urllib2, urllib, xmltodict, json

class eNom(object):
    uid = ''
    pw = ''
    base_url = ''
    command = ''

    def __init__(self, username, password, base_url='https://resellertest.enom.com/interface.asp?'):
        self.uid = username
        self.pw = password
        self.base_url = base_url


    def __getattr__(self, name, **kwargs):
        def _call(**kwargs):
            q = {
                'command': name,
                'uid': self.__dict__['uid'],
                'pw': self.__dict__['pw'],
                'responsetype': 'XML'
            }
            query = urllib.urlencode(dict(q.items() + kwargs.items()))

            response = urllib2.urlopen(self.base_url + query)
            d = xmltodict.parse(''.join( r.strip() for r in response.readlines()))
            j = json.loads(json.dumps(d))
            return j['interface-response']
        return _call
