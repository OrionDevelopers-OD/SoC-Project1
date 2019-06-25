from django import forms
class DepartmentForm(forms.Form):
    docfile = forms.FileField(
        department = 'abc'
    )
