from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

now = timezone.now()
def home(request):
   return render(request, 'REprop/home.html',
                 {'REprop': home})

# Customer_List
@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'REprop/customer_list.html',
                 {'customers': customer})

#customer_Edit
@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'REprop/customer_list.html',
                         {'customers': customer})
   else:
        # edit
       form = CustomerForm(instance=customer)
   return render(request, 'REprop/customer_edit.html', {'form': form})


# customer_delete
@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('REprop:customer_list')

# property_list
@login_required
def property_list(request):
    propertys = Property.objects.filter(created_date__lte=timezone.now())
    return render(request, 'REprop/property_list.html',
                 {'propertys': propertys})

# property_edit
@login_required
def property_edit(request, pk):
   property = get_object_or_404(Property, pk=pk)
   if request.method == "POST":
       # update
       form = PropertyForm(request.POST, instance=property)
       if form.is_valid():
           property = form.save(commit=False)
           property.updated_date = timezone.now()
           property.save()
           propertys = Property.objects.filter(created_date__lte=timezone.now())
           return render(request, 'REprop/property_list.html',
                         {'propertys': propertys})
   else:
        # edit
       form = PropertyForm(instance=property)
   return render(request, 'REprop/property_edit.html', {'form': form})

# property_delete
@login_required
def property_delete(request, pk):
   property = get_object_or_404(Property, pk=pk)
   property.delete()
   return redirect('REprop:property_list')

@login_required
def property_summary(request, pk):
    customers = get_object_or_404(Customer, pk=pk)
    customers = Customer.objects.filter(created_date__lte=timezone.now())
    propertys = Property.objects.filter(pk=pk)
    return render(request, 'REprop/property_summary.html', {'customers': customers,
                                                    'propertys': propertys,})
