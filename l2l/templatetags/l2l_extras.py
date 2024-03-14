from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='l2l_dt')
def l2l_dt(value):
    if not value or isinstance(value, int) or isinstance(value, float) or isinstance(value, bool):
        return ''
  
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError('Invalid date string')