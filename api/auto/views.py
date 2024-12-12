from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Auto,Image,Category
from .serializers import AutoSerializer, RegisterSerializer,CategorySerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
class CategoryViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
class AutoAPIList(generics.ListCreateAPIView):
    """
    Список автомобилей доступен всем (GET),
    создание записи (POST) только для авторизованных пользователей.
    """
    serializer_class = AutoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = Auto.objects.all()
        category_id = self.request.query_params.get('categories')
        if category_id:
            queryset = queryset.filter(categories__id=category_id)
        return queryset

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]  # GET доступен всем
        if self.request.method == 'POST':
            return [IsAuthenticated()]  # POST доступен только авторизованным
        return super().get_permissions()

class RegisterView(APIView):
    """
    Класс для регистрации нового пользователя
    """
    permission_classes = [AllowAny]  # Разрешаем доступ всем пользователям

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AutoAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsAdminOrReadOnly,)
class AutoDetailView(APIView):
    """
    Представление для отображения деталей автомобиля (GET).
    Доступно всем пользователям.
    """
    permission_classes = [AllowAny]  # Разрешаем доступ всем пользователям

    def get(self, request, pk, *args, **kwargs):
        try:
            auto = Auto.objects.get(pk=pk)  # Поиск объекта по первичному ключу
        except Auto.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AutoSerializer(auto)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class AutoAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = (IsOwnerOrReadOnly,)