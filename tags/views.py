from rest_framework import viewsets
from tags.models import Tag
from tags.serializers import TagSerializer
from todo_list.permissions import IsAdminOrReadOnly


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]
