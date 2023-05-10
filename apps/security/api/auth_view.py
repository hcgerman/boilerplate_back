from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.security.serializers.user_serializer import UserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_session(request, *args, **kwargs):
    user = request.user
    serializer = UserSerializer(instance=user)
    return Response({"user": serializer.data})
