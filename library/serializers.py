# from rest_framework import serializers
# from .models import Person

# class PeopleSerializer(serializers.Models.serializers):

#     class Meta:
#         model = Person
#         fileds = '__all__'
        

from rest_framework import serializers
from .models import Person  # Assuming 'Person' is your model

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'  # or list specific fields, e.g., ['name', 'age']


    def validate(self, data):

        iChars = "!@#$%^&*()+=-[]\\\';,./{}|\":<>?"
        if any (c in iChars for c in data['name']):
            raise serializers.ValidationError('name cannot contain special chars')

        if data['age'] < 18:
            raise serializers.ValidationError('age should be greator than 18')
        return data