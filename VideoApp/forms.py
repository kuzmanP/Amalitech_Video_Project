from django import forms
from .models import Video, UserProfile

from django import forms
from .models import Video

from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            if not file.content_type.startswith('video/'):
                raise forms.ValidationError('File is not a video.')
            if file.size > 52428800:  # 50MB limit
                raise forms.ValidationError('File size exceeds 50MB.')
            return file
        else:
            raise forms.ValidationError('No file selected.')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'email', 'verified']