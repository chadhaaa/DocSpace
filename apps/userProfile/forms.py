from django import forms 

from .models import userprofile 

class userProfileForm(forms.ModelForm): 
    class Meta: 
        model = userprofile
        fields = ('avatar',)