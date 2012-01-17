""" Widgets for mongonaut forms"""

from django import forms

from mongoengine.base import ObjectIdField
from mongoengine.fields import DateTimeField
from mongoengine.fields import ListField
from mongoengine.fields import ReferenceField


def get_widget(field, disabled=False):
    """ TODO: Make this do something besides just character fields """
    attrs={}
    attrs['class'] = 'span6 xlarge'
    if disabled or \
            isinstance(field, ObjectIdField) or \
            isinstance(field, ListField) or \
            isinstance(field, ReferenceField) or \
            isinstance(field, DateTimeField):
        attrs['class'] += ' disabled'
        attrs['readonly'] = 'readonly'
    
    if hasattr(field, "max_length") and not field.max_length:
        return forms.Textarea(attrs=attrs)


    return forms.TextInput(attrs=attrs)