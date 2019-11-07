from django import forms

class IncidentDetailsSelectionForm(forms.Form):

	IncidentNumberField = forms.CharField(required=False,  label='', widget=forms.TextInput(attrs={'placeholder': 'Incident Number'}) )
	IncidentDescription = forms.CharField(required=False,  label='', widget=forms.TextInput(attrs={'placeholder': 'Incident Description'}) )
