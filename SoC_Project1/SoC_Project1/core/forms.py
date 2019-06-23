from django import forms
class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept']
