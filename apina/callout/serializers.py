from rest_framework import serializers
from callout.models import User, Beacon, Workspace, Status, Subscription


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email_address', 'first_name', 'last_name', 'subscriptions')


class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        fields = ('id', 'major', 'minor', 'uuid')


class WorkspaceSerializer(serializers.ModelSerializer):
    attendees = serializers.SerializerMethodField()
    admins = serializers.SerializerMethodField()
    beacons = serializers.SerializerMethodField()

    class Meta:
        model = Workspace
        fields = ('id', 'date_starting', 'date_ending', 'name', 'creator', 'beacons', 'attendees', 'admins')

    def get_attendees(self, workspace):
        attendees = User.objects.filter(subscriptions__workspace=workspace, subscriptions__role=1)
        serializer = UserSerializer(instance=attendees, many=True)
        return serializer.data

    def get_admins(self, workspace):
        admins = User.objects.filter(subscriptions__workspace=workspace, subscriptions__role=2)
        serializer = UserSerializer(instance=admins, many=True)
        return serializer.data

    def get_beacons(self, workspace):
        beacons = workspace.beacons
        serializer = BeaconSerializer(instance=beacons, many=True)
        return serializer.data


class SubscriptionListGetSerializer(serializers.ModelSerializer):
    currentstatus = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = '__all__'
        depth = 1

    def get_currentstatus(self, subscription):
        currentstatus = Status.objects.filter(subscription=subscription).order_by('-date_created')[0]
        serializer = StatusSerializer(instance=currentstatus, many=False)
        return serializer.data


class SubscriptionGetSerializer(serializers.ModelSerializer):
    statushistory = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = '__all__'
        depth = 1

    def get_statushistory(self, subscription):
        statushistory = Status.objects.filter(subscription=subscription).order_by('-date_created')
        serializer = StatusSerializer(instance=statushistory, many=True)
        return serializer.data


class SubscriptionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'role', 'feedback', 'user', 'workspace')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
