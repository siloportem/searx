from sys import version_info

if version_info[0] == 2:
    from urllib import quote, quote_plus, unquote, urlencode
    from urlparse import urljoin, urlparse
else:
    from urllib.parse import quote, quote_plus, unquote, urlencode, urljoin, urlparse


__export__ = (quote,
              quote_plus,
              unquote,
              urlencode,
              urljoin,
              urlparse)
