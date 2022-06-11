"""Base64 python file.."""

# Standard Library
# -*- coding: utf-8 -*-
import base64

# Django
from django import template
from django.contrib.staticfiles.finders import find

register = template.Library()


def get_file_data(file_path):
    """Get data of a file."""
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
        return data


@register.simple_tag
def to_base64(path):
    """Convert to base64."""
    file_path = find(path)
    ext = file_path.split('.')[-1]
    file_str = base64.b64encode(get_file_data(file_path)).decode()
    return f'data:image/{ext};base64,{file_str}'
