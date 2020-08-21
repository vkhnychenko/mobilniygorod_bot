from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import ManualCategory, ManualItem


class ManualItemSerializer(ModelSerializer):
    # products = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = ManualItem
        fields = ("id", "image", "description")


class ManualCategorySerializer(ModelSerializer):
    items = ManualItemSerializer(many=True)

    class Meta:
        model = ManualCategory
        fields = ("id", "items", "name")