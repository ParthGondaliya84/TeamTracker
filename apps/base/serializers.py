from rest_framework import serializers

class BaseSerialzers(serializers.ModelSerializer):
    user =serializers.StringRelatedField(read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)
    updated_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        abstract = True
        read_only_fields = ["created_by", "updated_by", "created_at", "updated_at",
                            "is_active", "is_delete"]