from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import add_stock, delete_product 
from main.views import edit_product
from main.views import get_product_json, add_product_ajax, add_stock_ajax, delete_product_ajax, edit_product_ajax
from main.views import get_product_count

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("add_stock/<int:product_id>/", add_stock, name="add_stock"),
    path("delete_product/<int:product_id>/", delete_product, name="delete_product"),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path("add_stock_ajax/<int:product_id>/", add_stock_ajax, name="add_stock_ajax"),
    path("delete_product_ajax/<int:product_id>/", delete_product_ajax, name="delete_product_ajax"),
    path('edit-product-ajax/<int:product_id>/', edit_product_ajax, name='edit_product_ajax'),
    path('get_product_count/', get_product_count, name='get_product_count'),
]