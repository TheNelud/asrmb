from django.template.defaultfilters import floatformat
from django.template import Library

register = Library()

def formatted_float(value):
    value = floatformat(value, arg=3)
    return str(value).replace(',','.')


register.filter('formatted_float', formatted_float)



# {% load floattags %}
# |formatted_float