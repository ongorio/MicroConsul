from clients.services import ClientsService

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from clients.serializers import ClientSerializer, ClientCreateSerializer

class ClientsApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            clients = ClientsService.get_clients()
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ClientCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            client_data = serializer.validated_data
            client = ClientsService.create_client(client_data)
            output_serializer = ClientSerializer(client)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ClientApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        try:
            client = ClientsService.get_client_by_id(id)
            
            if client is None:
                return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

            serializer = ClientSerializer(client)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
