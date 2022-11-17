from django.urls import path, reverse_lazy
from django.views.generic import CreateView, DeleteView

from awards.models import Category, Nomination
from awards.views import CategoryList, CategoryDetail, NominationsList, NominationDetail

app_name = 'awards'

urlpatterns = [
    path('category-list/', CategoryList.as_view(), name='categories'),
    path('category-detail/<pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('nominations-list/', NominationsList.as_view(), name='nominations'),
    path('nomination-detail/<pk>/', NominationDetail.as_view(), name='nomination-detail'),
    path('category/create/',
         CreateView.as_view(
             model=Category,
             fields='__all__',
             success_url=reverse_lazy('awards:categories'),
             template_name='awards/generic_update.html'
         ),
         name='category-create'),
    path('category/<pk>/delete/',
         DeleteView.as_view(
             model=Category,

             success_url=reverse_lazy('awards:categories'),
             template_name='awards/generic_delete.html'
         ),
         name='category-delete'),
    path('nomination/create/',
         CreateView.as_view(
             model=Nomination,
             fields='__all__',
             success_url=reverse_lazy('awards:categories'),
             template_name='awards/generic_update.html'
         ),
         name='nomination-create'),

]
