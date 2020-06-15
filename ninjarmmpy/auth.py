from requests.auth import AuthBase
from email.utils import formatdate

import base64
import hmac
import hashlib

class NinjaAuthentication(AuthBase):

    HEADER_AUTH = "Authorization"
    HEADER_DATE = "Date"
    ENCODING = "utf-8"


    def __init__(self, AccessKeyID: str, SecretAccessKey: str):
        self.AccessKeyID = AccessKeyID
        self.SecretAccessKey = SecretAccessKey
        self.timestamp = formatdate(timeval=None, localtime=False, usegmt=True)


    def __call__(self, request):
        unsigned = request.method + "\n"  # HTTP verb
        unsigned += "\n"                  # Content MD5
        unsigned += "\n"                  # Content type
        unsigned += self.timestamp + "\n" # Date
        unsigned += request.path_url      # Canonicalized resource

        encoded = base64.b64encode(unsigned.encode((self.ENCODING)))
        digest = hmac.new(self.SecretAccessKey.encode(self.ENCODING), encoded, hashlib.sha1)
        str_signature = base64.b64encode(digest.digest()).decode(self.ENCODING)
        signature = str.encode(str_signature)

        request.headers[self.HEADER_AUTH] = f'NJ {self.AccessKeyID}:{signature.decode(self.ENCODING)}'
        request.headers[self.HEADER_DATE] = self.timestamp
        return request
