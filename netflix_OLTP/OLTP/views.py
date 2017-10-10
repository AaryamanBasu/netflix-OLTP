from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from .serializers import (UserSerializer, ShowSerializer, RatingsSerializer, PlanSerializer, DirectorSerializer, RuntimeSerializer, GenreSerializer, PaymentSerializer, BudgetSerializer, ReviewsSerializer)
from .models import User, Show, Ratings, Plan, Director, Runtime, Genre, Payment, Budget, Reviews

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ShowViewSet(ModelViewSet):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()



class RatingsViewSet(ModelViewSet):
    serializer_class = RatingsSerializer
    queryset = Ratings.objects.all()



class PlanViewSet(ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()



class DirectorViewSet(ModelViewSet):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()



class RuntimeViewSet(ModelViewSet):
    serializer_class = RuntimeSerializer
    queryset = Runtime.objects.all()



class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()



class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()



class BudgetViewSet(ModelViewSet):
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()



class ReviewsViewSet(ModelViewSet):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()
