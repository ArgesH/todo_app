from django.urls import path
from ideas import views

urlpatterns = [
    path('create_idea/<int:id>', views.create_idea(), name="create-idea"),
]
