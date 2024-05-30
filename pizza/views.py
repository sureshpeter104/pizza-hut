from django.shortcuts import render
from .forms import pizzaForm,multiplepizzaform
from django.forms import formset_factory
from .models import pizza

# Create your views here.
def homepage(request): #function based view
  return render(request,'pizza/home.html')
def order(request):
  multiple_pizza_form=multiplepizzaform #empty form
  created_pizza_pk = None
  if request.method=='POST':
    filled_form=pizzaForm(request.POST)
    if filled_form.is_valid():
      note='your order for %s %s %s pizza was placed!!'%(filled_form.cleaned_data['topping1'],
                                                         filled_form.cleaned_data['topping2'],
                                                         filled_form.cleaned_data['size'])
      filled_form.save()
      created_pizza = filled_form.save()
      created_pizza_pk = created_pizza.id 
      new_form=pizzaForm()  #empty form
    
    else:
      note='somthing went wrong'
      new_form=filled_form  #empty form
    
    return render(request,'pizza/order.html',{'pizzaform':new_form,'note':note,'multiplepizzaform':multiple_pizza_form,'created_pizza_pk':created_pizza_pk})    
  else:
    form=pizzaForm() #object of class #empty form
    return render(request,'pizza/order.html',{'pizzaform':form,'multiple_pizza_form':multiple_pizza_form,'created_pizza_pk':created_pizza_pk})
def pizzas(request):
    number_of_pizzas = 2
    if request.method == 'GET':
        filled_form = multiplepizzaform(request.GET)
        if filled_form.is_valid():
            number_of_pizzas = filled_form.cleaned_data['number']
            print(number_of_pizzas)
    PizzasFormSet = formset_factory(pizzaForm, extra=number_of_pizzas)  # formset class...
    if request.method == 'POST':
        filled_formset = PizzasFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            note='your order placed successfully,have a good dinner...!!!'
        else:
            note= 'sorry Something Went Wrong tryagain'
        return render(request, 'pizza/pizzas.html', {'note':note})
    form_set = PizzasFormSet() #Empty form_set
    return render(request,'pizza/pizzas.html',{'form_set':form_set})
def edit(request,pk):
    pizza_object = pizza.objects.get(pk=pk)  #model class
    filled_form =pizzaForm(instance=pizza_object)   #form object
    if request.method=='POST':
      edited_form=pizzaForm(request.POST,instance=pizza_object)
      if edited_form.is_valid():
        edited_form.save()
        note='order was updated successfully'
      else:
        note='sorry please try again'  
      return render(request,'pizza/edit.html',{'form':edited_form,'pk':pk,'note':note})
  
    return render(request,'pizza/edit.html',{'form':filled_form,'pk':pk})

  