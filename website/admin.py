from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Tvets, Category, SubCategory, Job, ExpertTips, Whoweare, Ourmission, Whatsetsasapart, Visionexpertise, Legal, FaqHeaders, Faq, PremiumTitles, Premium, Howitworks, Whychoose, Corevalues, Howdoesit, Contacts, Corporatereposnsibility, Awarded, Application, ChatMessage, UserProfile

class TvetsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Tvets, ImportExportModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'header_image', 'image')
    search_fields = ('name',)

admin.site.register(Category, ImportExportModelAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)

admin.site.register(SubCategory, ImportExportModelAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'amount', 'is_active')
    search_fields = ('title', 'company', 'location', 'job_type', 'amount')
    list_filter = ('is_active',)

admin.site.register(Job, JobAdmin)

class ExpertTipsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title', 'body')

admin.site.register(ExpertTips, ExpertTipsAdmin)

class WhoweareAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title', 'body')

admin.site.register(Whoweare, WhoweareAdmin)

class OurmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title', 'body')

admin.site.register(Ourmission, OurmissionAdmin)

class WhatsetsasapartAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title', 'body')

admin.site.register(Whatsetsasapart, WhatsetsasapartAdmin)

class VisionexpertiseAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title', 'body')

admin.site.register(Visionexpertise, VisionexpertiseAdmin)

class LegalAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title', 'body')

admin.site.register(Legal, LegalAdmin)

class FaqHeadersAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(FaqHeaders, ImportExportModelAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ('headers', 'title', 'body')
    search_fields = ('title', 'body')

admin.site.register(Faq, ImportExportModelAdmin)

class PremiumTitlesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(PremiumTitles, PremiumTitlesAdmin)

class PremiumAdmin(admin.ModelAdmin):
    list_display = ('maintitle', 'premium_headers', 'image', 'body')
    search_fields = ('maintitle', 'body')

admin.site.register(Premium, PremiumAdmin)

class HowitworksAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body')
    search_fields = ('title', 'body')

admin.site.register(Howitworks, HowitworksAdmin)

class WhychooseAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body')
    search_fields = ('title', 'body')

admin.site.register(Whychoose, WhychooseAdmin)

class CorevaluesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body')
    search_fields = ('title', 'body')

admin.site.register(Corevalues, CorevaluesAdmin)

class HowdoesitAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title', 'body')

admin.site.register(Howdoesit, HowdoesitAdmin)

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'message')
    search_fields = ('name', 'telephone', 'message')

admin.site.register(Contacts, ContactsAdmin)

class CorporatereposnsibilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body')
    search_fields = ('title', 'body')

admin.site.register(Corporatereposnsibility, CorporatereposnsibilityAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'status', 'applied_at')
    search_fields = ('applicant', 'job', 'status', 'applied_at')

admin.site.register(Application, ApplicationAdmin)

class AwardedAdmin(admin.ModelAdmin):
    list_display = ('application', 'awarded_at', 'is_completed')
    search_fields = ('application', 'awarded_at', 'is_completed')

admin.site.register(Awarded, AwardedAdmin)

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'is_read', 'seen_at')  # Show seen_at
    list_filter = ('is_read', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'message')
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp', 'seen_at')  # ✅ seen_at is now properly referenced

admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Chat Admin"
admin.site.index_title = "Manage Chat Messages"

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_role', 'location', 'phone_number')
    search_fields = ('user__username', 'job_role', 'location')
    ordering = ('-created_at',)
