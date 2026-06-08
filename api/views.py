from rest_framework.response import Response
from rest_framework.decorators import api_view

from members.models import Member
from .serializers import MemberSerializer


@api_view(['GET'])
def member_list(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)

    return Response(serializer.data)
