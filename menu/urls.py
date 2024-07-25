from django.urls import path

from menu.views import MenuView

urlpatterns = [
    path('<slug:selected_menu_element_slug>/', MenuView.as_view(), name='test_menu_page'),
    path('', MenuView.as_view(), name='test_menu_page')
]
