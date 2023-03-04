from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404

from .forms import EditItemForm, NewItemForm
from .models import Items, Category

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('Category', 0)
    categories = Category.objects.all()
    items = Items.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(Category_id = category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
     
    return render(request, 'items/items.html', {'items': items,'query': query, 'categories': categories, 'category_id' : int(category_id),})

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(Category=item.Category, is_sold=False).exclude(pk=pk)[0:3]


    return render(request, 'items/detail.html', {'item': item, "related_items": related_items,})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, 'items/form.html', {'form': form, 'title': 'New item',})


@login_required
def edit(request, pk):
    item = get_object_or_404(Items, pk=pk, created_by = request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'items/form.html', {'form': form, 'title': 'Edit item',})


@login_required
def delete(request, pk):
    item = get_object_or_404(Items, pk=pk, created_by = request.user)
    item.delete()
    
    return redirect('dashboard:index')
    