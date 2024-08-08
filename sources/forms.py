from django import forms
from .models import SourceConn

class SourceConnForm(forms.ModelForm):
    class Meta:
        model = SourceConn
        fields = '__all__'  # Use all fields from the model