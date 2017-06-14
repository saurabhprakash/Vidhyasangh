from rest_framework import views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import  EmployeeSerializer, CategorySerializer, GetCategorySerializer
from .models import Employee, Category
from django.http import JsonResponse

from datetime import datetime, date
# Create your views here.


class CategoryView(views.APIView):

    permission_classes = [AllowAny, ]

    def post(self, request, format=None):
        '''
        Register
        ---
        parameters:
            - name: employee_id
              required: True
              type: number
            - name: first_name
              required: True
              type: string
            - name: last_name
              required: True
              type: string
            - name: password
              required: True
              type: string
        '''
        serializer = CategorySerializer(data=request.data)
     #   print (serializer.initial_data)
        if not serializer.is_valid():
            res = {
                'code': 2,
            }
            for key, val in serializer.errors.items():
                res['message'] = key + ": " + val[0]
            return JsonResponse(res)

        serializer.save()
        res = {
            'code': 0,
            'message': 'Category Registration Successful'
        }
        return JsonResponse(res)



class GetAllCategories(APIView):
    """
    Get all Categories 
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches all Categories .
        """
       	categories  = Category.objects.filter(is_deleted=False)
       	serializer = GetCategorySerializer(categories, many=True)
       	res = {
            'error': 0,
            'detail': '',
            'response': serializer.data
        }
       	return Response(data=res, status=status.HTTP_200_OK)
       	


    


class RegisterView(views.APIView):

    permission_classes = [AllowAny, ]

    def post(self, request, format=None):
        '''
        Register
        ---
        parameters:
            - name: employee_id
              required: True
              type: number
            - name: first_name
              required: True
              type: string
            - name: last_name
              required: True
              type: string
            - name: password
              required: True
              type: string
        '''
        serializer = EmployeeSerializer(data=request.data)
     #   print (serializer.initial_data)
        if not serializer.is_valid():
            res = {
                'code': 2,
            }
            for key, val in serializer.errors.items():
                res['message'] = key + ": " + val[0]
            return JsonResponse(res)

        serializer.save()
        res = {
            'code': 0,
            'message': 'Employee Registration Successful'
        }
        return JsonResponse(res)

    def put(self, request, format=None):
        '''
        Register
        ---
        parameters:
            - name: employee_id
              required: True
              type: number
        '''
        try:
            emp = Employee.objects.get(employee_id=request.data.get('employee_id'))
        except:
            res = {
                'code': 1,
                'message': 'No Employee exist for entered Employee ID',
            }
            return JsonResponse(res)

        emp.is_admin = True
        emp.save()
        res = {
            'code': 0,
            'message': 'Changed to Admin'
        }
        return JsonResponse(res)
