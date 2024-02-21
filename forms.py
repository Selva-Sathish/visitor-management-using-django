from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['visitor_name', 'mobile_number', 'place', 'company_name', 'designation', 'person_to_meet', 'purpose', 'photo_path']
