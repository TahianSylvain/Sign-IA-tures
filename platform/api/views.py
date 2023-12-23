import os
from api.main import main
from main.models import FilesAdmin
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.response import Response


class LandingViewSet(APIView):
    def get(self, request, *args, **kwargs):
        data = {}
        if request.user.username:
            query = FilesAdmin.objects.filter(
                owner=request.user)            
            for q in query:
                data["static_url"] = q.adminupload.name
                data['owner'] = q.owner.username
        return Response(data)
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_user = User.objects.get(
                email = request.data['email'],
                username=request.data['username'],
            )
            ## Create / GeneratePDF
            main(text=new_user.username)
            new_pdf = FilesAdmin.objects.create(
                owner = new_user, 
                adminupload = os.path.join(
                    settings.BASE_DIR, 
                    f"./static/{new_user.username}_output.pdf" )
            )
            return Response(serializer.data)
        return Response(serializer.errors)
    
