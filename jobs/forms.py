from django import forms

class PostJobForm(forms.Form):
    last_date = forms.DateTimeField(required = True)
    job_title = forms.CharField(max_length=50,required=True)
    category=forms.CharField(max_length=50,required=True)
    company = forms.CharField(max_length=50,required = True)
    place = forms.CharField(max_length= 50,required = True)
    experience = forms.CharField(max_length = 50,required = True)
    salary = forms.CharField(max_length = 20)

