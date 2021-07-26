"""e_com URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from product_app.views import CategoryList, SubCategoryList, ProductListFromCategory, ProductListFromSubCategory,\
    ProductCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_all_categories/', CategoryList.as_view()),
    url(r'^get_all_products_for_category/(?P<pk>[0-9].*)/$', ProductListFromCategory.as_view()),
    url(r'^get_all_products_for_sub_category/(?P<pk>[0-9].*)/$', ProductListFromSubCategory.as_view()),
    url(r'^add_product_under_sub_category', ProductCreateView.as_view()),
]
