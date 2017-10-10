from rest_framework import serializers
from .models import User, Show, Ratings, Plan, Director, Runtime, Genre, Payment, Budget, Reviews

class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = "__all__"



class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"



class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = "__all__"



class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"



class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"



class RuntimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runtime
        fields = "__all__"



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"



class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = "__all__"



class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"
