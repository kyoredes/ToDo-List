from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class APIInfoView(APIView):
    def get(self, request):
        data = {
            "name": "To-do list",
            "description": "This is the main API of the to-do list project",
            # "documentation": "https://docs.example.com"
        }
        return Response(data, status=status.HTTP_200_OK)
