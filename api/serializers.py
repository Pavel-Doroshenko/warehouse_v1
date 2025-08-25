from rest_framework import serializers, validators

from api.models import ApiUser, Warehouse, Product, Category


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)
    cat_id = serializers.CharField( write_only=True)

    def update(self, instance, validated_data):
        if email := validated_data.get("email"):
            instance.email = email
            instance.save(update_fields=["email"])

        if password := validated_data.get("password"):
            instance.set_password(password)
            instance.save(update_fields=["password"])
        return instance

    def create(self, validated_data):
        user = ApiUser.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            cat_id=validated_data["cat_id"],
        )

        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}