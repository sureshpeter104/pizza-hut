from django import forms
from .models import pizza

# class pizzaForm(forms.Form):
#   topping1=forms.CharField(label="toppping1",max_length=100,widget=forms.PasswordInput)
#   topping2=forms.CharField(label="toppping2",max_length=100,widget=forms.Textarea)
#   size=forms.ChoiceField(label="size",choices=[('small','small'),
#                                                ('medium','medium'),
#                                                ('large','large')])
  
class pizzaForm(forms.ModelForm):
  class Meta: #about details about models
    model= pizza
    fields=['topping1','topping2','size']
    # labels={'topping1':'T1'}
    # Widgets={'topping2':forms.PasswordInput}

class multiplepizzaform(forms.Form): #django from class
  number=forms.IntegerField(min_value=2,max_value=10) 
     