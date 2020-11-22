from django import template


register = template.Library()

@register.filter('cut')
def cutText(text,word):
    """ This function will cuts the word from the given text"""
    return text.replace(word,'')