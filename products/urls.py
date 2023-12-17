from django.urls import path
from products.views import CategoryView,ProductAddView,ProductList,ProductDetail,ProductChangeView,\
    Product_remove,CategoryListView

urlpatterns=[
    path("add",CategoryView.as_view(),name="add-category"),
    path("product/add",ProductAddView.as_view(),name="product-add"),
    path("product/list",ProductList.as_view(),name="product-list"),
    path("product/<int:pk>/detail",ProductDetail.as_view(),name="product-detail"),
    path("product/<int:pk>/change",ProductChangeView.as_view(),name="product-change"),
    path("product/<int:pk>/remove",Product_remove),
    path("list",CategoryListView.as_view(),name="list-category")

]