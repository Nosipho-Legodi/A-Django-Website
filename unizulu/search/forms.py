from pyexpat import model
from django.forms import ModelForm 
from .models import degree
from django.contrib.auth.models import User

class degreeForm(ModelForm):
    class Meta:
        model = degree
        fields = '__all__'
        
        
class loginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password']