from django import forms
from models import Robot

class RobotForm(forms.ModelForm):  

    Thumb = forms.FileField(required=True)
    Image = forms.FileField(required=True)
    TinyMCE = forms.CharField(widget=forms.Textarea(attrs={'selector': 'textarea'}))
    Kit = forms.FileField(required=False)
    Software = forms.FileField(required=False)

    class Meta:
        model = Robot
        fields = ('Name', 'Date', 'Thumb', 'Image', 'TinyMCE', 'Kit', 'Software')

class EditForm(forms.ModelForm):  

    Thumb = forms.FileField(required=True)
    Image = forms.FileField(required=True)
    TinyMCE = forms.CharField(widget=forms.Textarea(attrs={'selector': 'textarea'}))
    Kit = forms.FileField(required=False)
    Software = forms.FileField(required=False)

    class Meta:
        model = Robot
        fields = ('Name', 'Date', 'Thumb', 'Image', 'TinyMCE', 'Kit', 'Software')

