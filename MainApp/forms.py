from django import forms

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(label='Choose a CSV file', required=True)
    timeframe = forms.IntegerField(label='Timeframe (minutes)', initial=1, required=True)
