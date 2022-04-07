from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Destination

class DestinationModelForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = [
            'name',
            'description',
            'rating',
            'region',
            'location',
            'image',
            'tags',
        ]

# This form is broken, using previous on because it works now
# class DestinationRawForm(forms.Form):
#     name = forms.CharField()
#     description = forms.CharField(widget=CKEditorWidget())
#     rating = forms.IntegerField()
#     region = forms.CharField()
#     location = forms.CharField()