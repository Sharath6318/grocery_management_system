from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone


from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView


from grocerymanagement.serializers import UserSerializer, GrocerySerializer
from grocerymanagement.models import GroceryItem


class RegisterView(CreateAPIView):

    serializer_class = UserSerializer

class GroceryListCreateView(CreateAPIView, ListAPIView):

    serializer_class = GrocerySerializer

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
    
    def get_queryset(self):
        return GroceryItem.objects.filter(owner = self.request.user)
    
class GroceryRetriveUpdateDeleteView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    
    serializer_class = GrocerySerializer

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = GroceryItem.objects.all()

class GrocerySummaryView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        cur_data = timezone.now()

        cur_month = cur_data.month

        cur_year = cur_data.year

        qs = GroceryItem.objects.filter(
            owner = request.user,
            created_at__month = cur_month,
            created_at__year = cur_year
        )

        total_grocery_expense = qs.aggregate(total_expense = Sum('price'))

        category_wise_expense = qs.values("category").annotate(total_expense = Sum('price'))

        context = {
            "total_grocery_expense" : total_grocery_expense,
            "category_wise_expense" : category_wise_expense
        }

        return Response(data = context)






