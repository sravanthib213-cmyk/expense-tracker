from django.shortcuts import render, redirect
from .models import Expense

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        Expense.objects.create(title=title, amount=amount, category=category)
        return redirect('/')
    
    expenses = Expense.objects.all()
    total = sum(e.amount for e in expenses)
    return render(request, 'index.html', {'expenses': expenses, 'total': total})

def delete_expense(request, id):
    Expense.objects.get(id=id).delete()
    return redirect('/')