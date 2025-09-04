from rest_framework import serializers, validators

from api.models import ApiUser, Warehouse, Product, Category, Basket


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)
    cat = serializers.SlugRelatedField('name', read_only=True)


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
    #user = serializers.PrimaryKeyRelatedField(many=True, queryset=ApiUser.objects.all())

    class Meta:
        model = Warehouse
        #fields = ['name', 'user']
        fields = '__all__'
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    #warehouse = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Product
        #fields = ('name', 'quantity', 'warehouse', )
        fields = '__all__'
        extra_kwargs = {"id": {"read_only": True}}


class BasketSerializer(serializers.Serializer):

    product = serializers.PrimaryKeyRelatedField(many=True, queryset=Basket.objects.all())
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=Basket.objects.all())
    quantity = serializers.IntegerField(null=True)
    # class Meta:
    #     model = Basket
    #     #fields = ('product', 'quantity', 'user', )
    #     fields = '__all__'
    #     extra_kwargs = {"id": {'read_only': True}}
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        if self.user.cat == 2:
            product = ()




