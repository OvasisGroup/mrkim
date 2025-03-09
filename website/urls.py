from django.urls import path
from . import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path, re_path


schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version="v1",
        description="API documentation",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # Change as needed
)


urlpatterns = [
    path('tvets/', views.TvetsListCreateAPIView.as_view(), name='tvets_list'),
    path('tvets/<int:pk>/', views.TvetsDetailAPIView.as_view(), name='tvets_detail'),
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category_detail'),
    path('subcategories/', views.SubCategoryListCreateAPIView.as_view, name='subcategory_list'),
    path('subcategories/<int:pk>/', views.SubCategoryDetailAPIView.as_view(), name='subcategory_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jobs/', views.JobListCreateAPIView.as_view(), name='jobs_list'),
    path('jobs/<int:pk>/', views.JobDetailAPIView.as_view(), name='jobs_detail'),
    path('experttips/', views.ExpertTipsListCreateAPIView.as_view(), name='experttips_list'),
    path('experttips/<int:pk>/', views.ExpertTipsDetailAPIView.as_view(), name='experttips_detail'),
    path('whoweare/', views.WhoWeAreListCreateAPIView.as_view(), name='whoweare_list'),
    path('whoweare/<int:pk>/', views.WhoWeAreDetailAPIView.as_view(), name='whoweare_detail'),
    path('ourmission/', views.OurMissioneListCreateAPIView.as_view(), name='ourmission_list'),
    path('ourmission/<int:pk>/', views.OurMissionDetailAPIView.as_view(), name='ourmission_detail'),
    path('whatsetsusapart', views.WhatSetsUsApartListCreateAPIView.as_view(), name='whatsetsusapart_list'),
    path('whatsetsusapart/<int:pk>/', views.WhatSetsUsApartDetailAPIView.as_view(), name='whatsetsusapart_detail'),
    path('vision', views.VisionListCreateAPIView.as_view(), name='visionexpertise_list'),
    path('vision/<int:pk>/', views.VisionDetailAPIView.as_view(), name='visionexpertise_detail'),
    path('legal', views.LegalCreateAPIView.as_view(), name='legal_list'),
    path('legal/<int:pk>/', views.LegalDetailAPIView.as_view(), name='legal_detail'),
    path('faqheaders', views.FaqCreateAPIView.as_view(), name='faq'),
    path('faqheaders/<int:pk>/', views.FaqDetailAPIView.as_view(), name='faq_detail'),
    path('faq', views.FaqBodyCreateAPIView.as_view(), name='MainFaq'),
    path('faq/<int:pk>/', views.FaqBodyDetailAPIView.as_view(), name='MainFaqDetail'),
    path('premium_headers', views.PremiumTitlesCreateAPIView.as_view(), name='Premium Header'),
    path('premium_headers/<int:pk>/', views.PremiumTitlesDetailAPIView.as_view(), name='Premium Header Detail'),
    path('premium', views.PremiumCreateAPIView.as_view(), name='Premium'),
    path('premium/<int:pk>/', views.PremiumDetailAPIView.as_view(), name='Premium Detail'),
    path('howitworks', views.HowItWorksCreateAPIView.as_view(), name='howitworks_list'),
    path('howitworks/<int:pk>/', views.HowItWorksDetailAPIView.as_view(), name='howitworks_detail'),
    path('whychooseus', views.WhyChooseCreateAPIView.as_view(), name='whychooseus_list'),
    path('whychooseus/<int:pk>/', views.WhyChooseDetailAPIView.as_view(), name='whychooseus_detail'),
    path('core-values', views.CorevaluesCreateAPIView.as_view(), name='core values'),
    path('core-values/<int:pk>/', views.CorevaluesDetailAPIView.as_view(), name='core values'),
    path('howdoesit', views.HowdoesitCreateAPIView.as_view(), name='how does it'),
    path('howdoesit/<int:pk>/', views.HowdoesitDetailAPIView.as_view(), name='how does it'),
    path('profile', views.UserProfileAPIView.as_view(), name='profile'),
    path('Application', views.AppplicationCreateAPIView.as_view(), name='Application'),
    path('EmployerApplication', views.EmployerApplicationListView.as_view(), name='EmployerApplication'),
    path('Application/<int:pk>/', views.ApplicationDetailView.as_view(), name='Application'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='swagger-json'),
]