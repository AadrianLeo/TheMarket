from django import forms

from .models import Items

INPUT_CLASSES = 'w-full py-6 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['Category','name', 'description', 'price', 'image']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['description'].widget.attrs['class'] = 'form-control'
    #     self.fields['price'].widget.attrs['class'] = 'form-control'
    #     self.fields['image'].widget.attrs['class'] = 'form-control'

        widgets = {
            'Category': forms.Select(attrs = {
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs = {
                'class': INPUT_CLASSES,
            }),
            'price': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            'image': forms.FileInput(attrs = {
                'class': INPUT_CLASSES,
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'description', 'price', 'image', 'is_sold']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['description'].widget.attrs['class'] = 'form-control'
    #     self.fields['price'].widget.attrs['class'] = 'form-control'
    #     self.fields['image'].widget.attrs['class'] = 'form-control'

        widgets = {
            'name': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs = {
                'class': INPUT_CLASSES,
            }),
            'price': forms.TextInput(attrs = {
                'class': INPUT_CLASSES,
            }),
            'image': forms.FileInput(attrs = {
                'class': INPUT_CLASSES,
            }),
        }