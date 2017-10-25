from rest_framework import serializers

from authentication.serializers import AccountSerializer
from tricounts.models import Tricount


class TricountSerializer(serializers.ModelSerializer):
    creator = AccountSerializer(read_only=True, required=True)

    class Meta:
        model = Tricount



class PaymentSerializer(serializers.ModelSerializer):
    creator = AccountSerializer(read_only=True, required=True)
