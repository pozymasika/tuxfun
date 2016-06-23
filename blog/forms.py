from django import forms

class PostImageForm(forms.Form):
    image = forms.FileField(label='Select a Post Image')
