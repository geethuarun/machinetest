from django import forms
from products.models import Category,Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["category_name"]
    

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["product_name","category_name","description","price"]
    
    



