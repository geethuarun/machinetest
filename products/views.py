from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from products.models import Category,Product
from products.forms import CategoryForm,ProductForm
from django.views.generic import View,CreateView,ListView,DetailView,UpdateView,DeleteView


class CategoryView(CreateView):
    template_name="categoryadd.html"
    form_class=CategoryForm
    # context_object_name="categories"
    # model=Category
    success_url=reverse_lazy("add-category")
    # def get(self,request,args,*kwargs):
    #     form=CategoryForm()
    #     return render(request,"category.html",{"form":form})
    
    # def post(self,request,args,*kwargs):
    #     form=CategoryForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("product-add")

class CategoryListView(ListView):
    template_name="categorylist.html"
    context_object_name="categories"
    model=Category
        

        

class ProductAddView(CreateView):
    template_name="productadd.html"
    model=Product
    form_class=ProductForm
    success_url=reverse_lazy("product-add")
    # def get(self,request,args,*kwargs):
    #     form=ProductForm()
    #     return render(request,"product.html",{"form":form})
    
    # def post(self,request,args,*kwargs):
    #     form=ProductForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("product-list")


class ProductList(ListView):
    template_name="productlist.html"
    context_object_name="products"
    model=Product

class ProductDetail(DetailView):
    template_name="productdetail.html" 
    context_object_name="product" 
    model=Product

class ProductChangeView(UpdateView):
    template_name="productchange.html"
    model=Product
    form_class=ProductForm
    success_url=reverse_lazy("product-list")

def Product_remove(request,args,*kwargs):
    id-kwargs.get("pk")
    Product.objects.filter().delete()
    return redirect("product-list")