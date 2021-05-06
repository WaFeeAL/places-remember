from rest_framework import serializers
from .models import MemoryModel


class MemorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user_id = serializers.IntegerField()
    location_name = serializers.CharField(max_length=150)
    location_address = serializers.CharField(max_length=255)
    location_memories = serializers.CharField(max_length=255)

    class Meta:
        model = MemoryModel

    def create(self, validated_data):
        return MemoryModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.location_name = validated_data.get('location_name', instance.location_name)
        instance.location_address = validated_data.get('location_address', instance.location_address)
        instance.location_memories = validated_data.get('location_memories', instance.location_memories)
        instance.save()
        return instance
