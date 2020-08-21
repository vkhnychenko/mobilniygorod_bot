from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ManualCategoryView, ManualItemView
router = DefaultRouter()
router.register('category', ManualCategoryView)

app_name = "api"

urlpatterns = [
    path('items/', ManualItemView.as_view()),
]
urlpatterns += router.urls