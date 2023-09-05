from typing import Any
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from django import template

register = template.Library()


@register.simple_tag()
def update_url_query(url: str, **kwargs: Any) -> str:
    parsed_url = urlparse(url)
    query = parsed_url.query
    query_params = dict(parse_qsl(query))

    for k, v in kwargs.items():
        query_params[k] = v

    new_query = urlencode(query_params)
    return urlunparse(parsed_url._replace(query=new_query))
