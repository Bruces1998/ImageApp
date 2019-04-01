from .models import Files,Images
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
#
#
#
class UserForm(UserCreationForm):
    class Meta():
        model = get_user_model()
        fields = ('username','email','password1','password2')


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'What will you call yourself on the website:'
        self.fields['email'].label = "Email Address"


class ImageForm(forms.ModelForm):
    class Meta():
        model = Images
        fields = {'image','image_by','name'}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image_by'].label = 'Reconfirm Your Username:'


class FileForm(forms.ModelForm):
    class Meta():
        model = Files
        fields = {'file','posted_by','name'}
