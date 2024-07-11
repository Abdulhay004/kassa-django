from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from users.models import *
from django.contrib import messages


class Userprofilform(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','nomi','tg','tel',)

    def __init__(self,*args,**kwargs):
        super(Userprofilform,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
class NewIshchiForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(), required=True)
    last_name = forms.CharField(widget=forms.TextInput(), required=True)
    tel = forms.CharField(widget=forms.TextInput(), required=True)

    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name','tel','tg',)
    
    def __init__(self, *args, **kwargs):
        super(NewIshchiForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
           
            
class QarzForm(forms.ModelForm):

    class Meta:
        model = Qarz
        fields = ('summa',)
        
    def __init__(self, *args, **kwargs):
        super(QarzForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'