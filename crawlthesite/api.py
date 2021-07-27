import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SanctionsListSerializer
from .getresults import getresultsaftersearch

results = None

class SearchList(APIView):
    def get(self, request):
        if results is not None:
            return Response(json.dumps(results))
        return Response(json.dumps([{}]))

    def post(self, request):
        serializer = SanctionsListSerializer(data=request.data)
        if serializer.is_valid():
            global results
            results = getresultsaftersearch(request.data)
            return Response(json.dumps(results), status.HTTP_201_CREATED, content_type='text/json')
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

