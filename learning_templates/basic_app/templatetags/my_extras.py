from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    value.replace(arg,'')

#register.filter('cut',cut)