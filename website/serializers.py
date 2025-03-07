from rest_framework import serializers
from .models import User, Tvets, Category, SubCategory, Job, ExpertTips, Whoweare, Ourmission, Whatsetsasapart, Visionexpertise, Legal, FaqHeaders, Faq, PremiumTitles, Premium, Howitworks, Whychoose, Corevalues, Howdoesit, Contacts, Corporatereposnsibility, Application, Awarded, ChatMessage, UserProfile
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'location', 'is_employer', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_employer': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
            'is_active': {'read_only': True},
        }
    
    def validate_phone_number(self, value):
        """Validate phone number format."""
        # Option 1: Using Regex (Basic Validation)
        phone_regex = re.compile(r'^\+?1?\d{9,15}$')  # Supports international formats
        if not phone_regex.match(value):
            raise serializers.ValidationError("Invalid phone number format. Use +254711782435.")

        return value
        
class TvetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tvets
        fields = ('id', 'name')

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'category')

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'header_image', 'image', 'name', 'description', 'subcategories')

class JobSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=SubCategory.objects.all()  # ✅ Properly handles ManyToManyField
    )
    
    recruiter = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),  # ✅ Allows recruiter selection
        required=False  # Optional if it will be set automatically
    )

    class Meta:
        model = Job
        fields = ('id', 'recruiter', 'title', 'company', 'location', 'description', 
                  'category', 'amount', 'job_type', 'link', 'telephone', 
                  'slug', 'date_posted', 'is_active', 'deadline')

    def create(self, validated_data):
        """Automatically assign recruiter from request.user if not provided."""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['recruiter'] = request.user
        return super().create(validated_data)


class ExpertTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertTips
        fields = ('id', 'title', 'body', 'created_on', 'last_modified', 'image')

class WhoweareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whoweare
        fields = ('id', 'title', 'body', 'created_on')

class OurmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ourmission
        fields = ('__all__')

class WhatsetsasapartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whatsetsasapart
        fields = ('__all__')

class VisionexpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visionexpertise
        fields = ('__all__')

class LegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legal
        fields = ('__all__')

class FaqHeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqHeaders
        fields = ('__all__')

class FaqSerializer(serializers.ModelSerializer):
    headers = FaqHeadersSerializer(read_only=True)
    class Meta:
        model = Faq
        fields = ('__all__')

class PremiumTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumTitles
        fields = ('__all__')

class PremiumSerializer(serializers.ModelSerializer):
    titles = PremiumTitlesSerializer(read_only=True)
    class Meta:
        model = Premium
        fields = ('__all__')

class HowitworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Howitworks
        fields = ('__all__')

class WhychooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whychoose
        fields = ('__all__')

class CorevaluesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corevalues
        fields = ('__all__')

class HowdoesitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Howdoesit
        fields = ('__all__')

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('__all__')

class CorporatereposnsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporatereposnsibility 
        fields = ('__all__')

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('__all__')

class AwardedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awarded
        fields = ('__all__')

class ChatMessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)
    receiver_name = serializers.CharField(source='receiver.username', read_only=True)

    class Meta:
        model = ChatMessage
        fields = ('__all__')
        read_only_fields = ('timestamp', 'is_read')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('__all__')