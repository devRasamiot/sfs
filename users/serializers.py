from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    # def validate_phone_number(self, phone_number):
        # MOBILE_REGEX = re.compile('^(?:\+?88)?01[15-9]\d{8}$')
        # if MOBILE_REGEX.match(phone_number):
            # return phone_number
        # else:
            # raise serializers.ValidationError('No. not matching')
# 
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
