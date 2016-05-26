from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from callout.models import User, Beacon, Workspace, Status, Subscription
from callout.serializers import UserSerializer, UserListSerializer, BeaconSerializer, WorkspaceGetSerializer, WorkspacePostSerializer, StatusSerializer, SubscriptionListGetSerializer, SubscriptionGetSerializer, SubscriptionPostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BeaconList(generics.ListCreateAPIView):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer


class BeaconDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer


class WorkspaceList(APIView):

    def get(self, request, format=None):
        workspaces = Workspace.objects.all()
        serializer = WorkspaceGetSerializer(workspaces, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkspacePostSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class WorkspaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceGetSerializer


class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class SubscriptionList(APIView):

    def get(self, request, format=None):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionListGetSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubscriptionPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionDetail(APIView):

    def get_object(self, pk):
        try:
            return Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subscription = self.get_object(pk)
        serializer = SubscriptionGetSerializer(subscription)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subscription = self.get_object(pk)
        serializer = SubscriptionPostSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subscription = self.get_object(pk)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)