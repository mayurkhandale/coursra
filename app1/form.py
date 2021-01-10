from .models import StudentModal
from django import forms

class StudentForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    con_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(StudentForm, self).clean()
        password = cleaned_data.get("password")
        con_password= cleaned_data.get("con_password")

        if password !=con_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
    class Meta:
        model=StudentModal
        fields="__all__"