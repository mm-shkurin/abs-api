from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Auto
from .serializers import AutoSerializer

class AutoListView(APIView):
    def get(self, request, *args, **kwargs):
        category_id = request.query_params.get('category', None)
        if category_id:
            autos = Auto.objects.filter(categories__id=category_id) # Исправлено categories__id
        else:
            autos = Auto.objects.all()

        sort_by_category = request.query_params.get('ordering', None)
        if sort_by_category == 'category':
            autos = autos.order_by('categories__name') # Исправлено categories__name
        elif sort_by_category == '-category':
            autos = autos.order_by('-categories__name') # Исправлено categories__name

        serializer = AutoSerializer(autos, many=True)
        return Response({'posts': serializer.data})

class AutoDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            auto = Auto.objects.get(pk=pk)
        except Auto.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AutoSerializer(auto)
        return Response({'post': serializer.data})
