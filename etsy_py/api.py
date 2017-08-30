from __future__ import unicode_literals

from requests import Session
from requests.auth import AuthBase
from six.moves.urllib import parse

from . import __version__, repo_url
from .exceptions import InvalidCredentials


class EtsyAPIKeyAuth(AuthBase):
    def __init__(self, api_key):
        super(EtsyAPIKeyAuth, self).__init__()

        if not api_key:
            raise InvalidCredentials('An Etsy API key is required.')

        self.api_key = api_key

    def __call__(self, r):
        # add the API key to the request's URL parameters
        r.prepare_url(r.url, {'api_key': self.api_key})
        return r


class EtsyAPI(Session):
    def __init__(self, **kwargs):
        super(EtsyAPI, self).__init__()

        # TODO: add support for OAUTH token based authentication via
        # a separate AuthBase handler
        self.auth = EtsyAPIKeyAuth(kwargs.get('api_key'))

        self.base_url = kwargs.get('base_url') or 'https://openapi.etsy.com/v2'
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': 'etsy_py/%s (+%s)' % (__version__, repo_url)
        }

    def request(self, method, url, *args, **kwargs):
        url_parts = parse.urlparse(url)
        if not url_parts.scheme:
            url = '/'.join([self.base_url.rstrip('/'), url.lstrip('/')])
        return super(EtsyAPI, self).request(method, url, *args, **kwargs)
