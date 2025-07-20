from django import forms

class QRcodeForm(forms.Form):
    name=forms.CharField(max_length=30,
                         label="Name",
                         widget=forms.TextInput(attrs={
                             'class':'form-control',
                             'placeholder':'Enter Name'
                         })
                         )
    url=forms.URLField(max_length=200,
                       label="Url",
                       widget=forms.URLInput(attrs={
                           'class':'form-control',
                           'placeholder':'Enter the Url'
                       })
                       )