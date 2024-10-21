from rest_framework import serializers
from .models import Question,Choice


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Question
        fields =['id','question_text','pub_date','owner']

    def validate_question_text(self,value):
        if 'spam' in value.lower():
            raise serializers.validationError('No sapm allowed in question text')
        return value


# serializer.model
class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    q_choice =serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all() ,source='question',write_only=True
    )
    class Meta:
        model =Choice
        fields = ['id','choice_text','votes','question' ,'q_choice']
           
#serializer.serializer

class QuestionSerializer(serializers.ModelSerializer):
    choices= ChoiceSerializer(many=True,read_only=True, source='choice_text')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model=Question
        fields =['id','question_text','pub_date','choices','owner']