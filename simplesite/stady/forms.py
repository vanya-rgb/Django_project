from django.forms import ModelForm
from .models import Ss

class SsForm(ModelForm):
    class Meta:
        model = Ss
        fields = ('title', 'content')