from django.forms import ValidationError
from django.forms.fields import  RegexField
import re

class NIPhoneNumberField(RegexField):
    """
    Nicaraguan phone number field.
    NOTE: Nicaragua will add another digit from April 1st 2009.
    """
    default_error_messages = {
        'invalid': u'Phone numbers must be in the format  XXXX-XXXX or XXXXXXXX.',
    }

    def __init__(self, *args, **kwargs):
        super(NIPhoneNumberField, self).__init__(r'^[ 0-9\-]+$',
                max_length = None, min_length = None, *args, **kwargs)

    def clean(self, value):
        """
        Validates the input and returns a string with only numbers.
        Returns an empty string for empty values
        """

        if value in EMPTY_VALUES:
            return u''

        v = super(NIPhoneNumberField, self).clean(value)
        v= v.replace('-', '')
        v = v.replace(' ', '')
        if (len(v) == 8):
            return v
        raise ValidationError(self.default_error_messages['invalid'])
