from rest_framework import serializers

class SiNoField(serializers.CharField):
    def to_internal_value(self, data):
        if isinstance(data, bool):
            return 'S' if data else 'N'
        elif isinstance(data, str):
            return 'S' if data.lower() == 'si' else 'N'
        else:
            raise serializers.ValidationError('Invalid value for SiNoField')

    def to_representation(self, value):
        if value is None:
            return None
        return value.upper() == 'S'

class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    status = serializers.CharField()
    moneda = serializers.CharField()
    f_id = serializers.CharField()

class ClientCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    sujeto_ieps = SiNoField()
    diferir_cfdi_cobros = serializers.BooleanField()
    limite_credito = serializers.DecimalField(max_digits=10, decimal_places=2)
    moneda_id = serializers.IntegerField()
    cond_pago_id = serializers.IntegerField()
