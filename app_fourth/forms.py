from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'email', 'password']
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True),
        }

        # Statement No 7 and 8 both purpose are same, we can use any one of them.
        # and if we did not want to use one or more then one fields then we can use below command:
        # exclude = ['required_field_name']
