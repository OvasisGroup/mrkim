from django.shortcuts import get_object_or_404
from website.serializers import TvetsSerializer, CategorySerializer, SubCategorySerializer, JobSerializer, ExpertTipsSerializer, WhoweareSerializer, OurmissionSerializer, WhatsetsasapartSerializer, VisionexpertiseSerializer, LegalSerializer, FaqHeadersSerializer, FaqSerializer, PremiumTitlesSerializer, PremiumSerializer, HowitworksSerializer, WhychooseSerializer, CorevaluesSerializer, HowdoesitSerializer, ContactsSerializer, CorporatereposnsibilitySerializer, ApplicationSerializer, AwardedSerializer, ChatMessageSerializer, UserProfileSerializer
from website.models import Tvets, Category, SubCategory, Job, ExpertTips, Whoweare, Ourmission, Whatsetsasapart, Visionexpertise, Legal, FaqHeaders, Faq, PremiumTitles, Premium, Howitworks, Whychoose, Corevalues, Howdoesit, Contacts, Corporatereposnsibility, Application, Awarded, ChatMessage, UserProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from cleaning.models import Category, SubCategory


class TvetsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tvets.objects.all()
    serializer_class = TvetsSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class TvetsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tvets.objects.all()
    serializer_class = TvetsSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class SubCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()   


class SubCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class ExpertTipsListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExpertTips.objects.all()
    serializer_class = ExpertTipsSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()   

class ExpertTipsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpertTips.objects.all()
    serializer_class = ExpertTipsSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class WhoWeAreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Whoweare.objects.all()
    serializer_class = WhoweareSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()   

class WhoWeAreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Whoweare.objects.all()
    serializer_class = WhoweareSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class OurMissioneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ourmission.objects.all()
    serializer_class = OurmissionSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class OurMissionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ourmission.objects.all()
    serializer_class = OurmissionSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class WhatSetsUsApartListCreateAPIView(generics.ListCreateAPIView):
    queryset = Whatsetsasapart.objects.all()
    serializer_class = WhatsetsasapartSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class WhatSetsUsApartDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Whatsetsasapart.objects.all()
    serializer_class = WhatsetsasapartSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class VisionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Visionexpertise.objects.all()
    serializer_class = VisionexpertiseSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class VisionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visionexpertise.objects.all()
    serializer_class = VisionexpertiseSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
class LegalCreateAPIView(generics.ListCreateAPIView):
    queryset = Legal.objects.all()
    serializer_class = LegalSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class LegalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Legal.objects.all()
    serializer_class = LegalSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class FaqCreateAPIView(generics.ListCreateAPIView):
    queryset = FaqHeaders.objects.all()
    serializer_class = FaqHeadersSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class FaqDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaqHeaders.objects.all()
    serializer_class = FaqHeadersSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class FaqBodyCreateAPIView(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class FaqBodyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class PremiumTitlesCreateAPIView(generics.ListCreateAPIView):
    queryset = PremiumTitles.objects.all()
    serializer_class = PremiumTitlesSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class PremiumTitlesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PremiumTitles.objects.all()
    serializer_class = PremiumTitlesSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class PremiumCreateAPIView(generics.ListCreateAPIView):
    queryset = Premium.objects.all()
    serializer_class = PremiumSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class PremiumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Premium.objects.all()
    serializer_class = PremiumSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class HowItWorksCreateAPIView(generics.ListCreateAPIView):
    queryset = Howitworks.objects.all()
    serializer_class = HowitworksSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class HowItWorksDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Howitworks.objects.all()
    serializer_class = HowitworksSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class WhyChooseCreateAPIView(generics.ListCreateAPIView):
    queryset = Whychoose.objects.all()
    serializer_class = WhychooseSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class WhyChooseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Whychoose.objects.all()
    serializer_class = WhychooseSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class CorevaluesCreateAPIView(generics.ListCreateAPIView):
    queryset = Corevalues.objects.all()
    serializer_class = CorevaluesSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class CorevaluesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Corevalues.objects.all()
    serializer_class = CorevaluesSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class HowdoesitCreateAPIView(generics.ListCreateAPIView):
    queryset = Howdoesit.objects.all()
    serializer_class = HowdoesitSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions() 

class HowdoesitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Howdoesit.objects.all()
    serializer_class = HowdoesitSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class AppplicationCreateAPIView(generics.ListCreateAPIView):
    """Allow users to apply for a job"""
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        """Set the applicant as the currently authenticated user."""
        return serializer.save(applicant=self.request.user)

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions() 

class EmployerApplicationListView(generics.ListAPIView):
    """List applications for jobs posted by the logged-in employer."""
    serializer_class = ApplicationSerializer
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions() 

    def get_queryset(self):
        return Application.objects.filter(job__recruiter=self.request.user)

class ApplicationDetailView(generics.RetrieveUpdateAPIView):
    """View or update an application (Employer can update the status)."""
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return Application.objects.filter(job__recruiter=self.request.user)
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()