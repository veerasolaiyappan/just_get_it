from django import forms
from .models import Forms
from uploads.core.models import Document


#DataFlair #File_Upload
class UserForm(forms.ModelForm):

    class Meta:
        model = Forms

        fields = [

        'username',
        'date',
        'report',
        'lead',
        'no_of_hours',
        'today_progres',
        'todays_document',
        'concern',
        'next_plan',
        'next_plan_document',

        ]
