from django import forms
from .models import Video
from users.models import CustomUser


class VideoEditForm(forms.ModelForm):
    class Meta:
        model  = Video
        fields = ["title", "description", "dt",]

class IconForm(forms.ModelForm):
    class Meta:
        model  = CustomUser
        fields = ["usericon",]
