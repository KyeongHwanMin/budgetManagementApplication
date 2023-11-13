from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.serializers import SignupSerializer


class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("회원가입 되었습니다.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors. status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)