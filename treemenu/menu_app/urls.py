from django.urls import path
from . import views

app_name = 'menu_app'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('contacts/', views.contacts_page, name='contacts'),

    path('products/', views.products_page, name='products'),
    path('products/categories/', views.categories_page, name='categories'),

    path('products/categories/electronics/', views.electronics_category_page, name='electronics'),
    path('products/categories/electronics/laptops/', views.laptops_page, name='laptops'),
    path('products/categories/electronics/laptops/gaming/', views.gaming_laptops_page, name='gaming_laptops'),
    path('products/categories/electronics/laptops/work/', views.work_laptops_page, name='work_laptops'),
    path('products/categories/electronics/smartphones/', views.smartphones_page, name='smartphones'),

    path('products/categories/apparel/', views.apparel_category_page, name='apparel'),

    path('products/popular/', views.popular_products_page, name='popular_products'),

    path('blog/', views.blog_page, name='blog'),
    path('blog/latest/', views.blog_latest_page, name='blog_latest'),
    path('blog/archive/', views.blog_archive_page, name='blog_archive'),
    path('blog/archive/2023/', views.blog_archive_2023_page, name='blog_archive_2023'),
    path('blog/archive/2024/', views.blog_archive_2024_page, name='blog_archive_2024'),
    path('faq/', views.faq_page, name='faq'),
    path('help/', views.help_page, name='help_page'),
]
