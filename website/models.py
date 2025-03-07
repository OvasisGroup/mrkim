from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError

User = get_user_model()

class Tvets(models.Model):
    name= models.CharField(max_length=150)
    class Meta:
        verbose_name_plural = "Tvets"
    
    def __str__(self):
        return self.name

class Category(models.Model):
    header_image = models.ImageField(null=True, blank=True, upload_to='categories')
    image = models.ImageField(null=True, blank=True, upload_to='ategories')
    name= models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Main Categories"
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name

class ExpertTips(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/blog/')

    class Meta:
        verbose_name_plural = "Expert Tips"
    
    def __str__(self):
        return self.title

class Whoweare(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Who We Are"
    
    def __str__(self):
        return self.title
    
class Ourmission(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Our Mission"
    
    def __str__(self):
        return self.title

class Whatsetsasapart(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')

    class Meta:
        verbose_name_plural = "What Sets As Apart"
    
    def __str__(self):
        return self.title
    
class Visionexpertise(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Your Vision, Our Expertise"
    
    def __str__(self):
        return self.title

class Legal(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Legal"
    
    def __str__(self):
        return self.title

class FaqHeaders(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Faq Headers"
    
    def __str__(self):
        return self.title

class Faq(models.Model):
    headers = models.ForeignKey(FaqHeaders, related_name='faqheaders', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Faqs"
    
    def __str__(self):
        return self.title
    
class PremiumTitles(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='premium')
    name= models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Premium Categories"
    
    def __str__(self):
        return self.name

class Premium(models.Model):
    maintitle = models.CharField(max_length=250, default="premium header")
    premium_headers = models.ForeignKey(PremiumTitles, related_name='premiumheaders', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='premium')
    body = RichTextField()

    class Meta:
        verbose_name_plural = "Premium Services"
    
    def __str__(self):
        return self.maintitle

class Howitworks(models.Model):
    title = models.CharField(max_length=250, default="premium header")
    image = models.ImageField(null=True, blank=True, upload_to='premium')
    body = RichTextField()

    class Meta:
        verbose_name_plural = "How it Works"
    
    def __str__(self):
        return self.title

class Whychoose(models.Model):
    title = models.CharField(max_length=250, default="premium header")
    image = models.ImageField(null=True, blank=True, upload_to='premium')
    body = RichTextField()

    class Meta:
        verbose_name_plural = "Why Choose Us"
    
    def __str__(self):
        return self.title

class Corevalues(models.Model):
    title = models.CharField(max_length=250, default="premium header")
    image = models.ImageField(null=True, blank=True, upload_to='premium')
    body = RichTextField()

    class Meta:
        verbose_name_plural = "Core Values"
    
    def __str__(self):
        return self.title

class Howdoesit(models.Model):
    title = models.CharField(max_length=250, default="premium header")
    body = RichTextField()

    class Meta:
        verbose_name_plural = "How does it work"
    
    def __str__(self):
        return self.title

class Contacts(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, default="Name")
    telephone = models.CharField(max_length=250, null=False, blank=False)
    message = models.TextField(max_length=500, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return self.name

class Corporatereposnsibility(models.Model):
    title = models.CharField(max_length=250, default="premium header")
    image = models.ImageField(null=True, blank=True, upload_to='premium')
    body = RichTextField()

    class Meta:
        verbose_name_plural = "Corporate Responsibility"
    
    def __str__(self):
        return self.title

CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)

class Job(models.Model):
    recruiter = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField(default="Default")
    category = models.ManyToManyField(SubCategory, blank=True, related_name='jobs')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    job_type = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time'
    )
    link = models.URLField(null=True, blank=True)
    telephone = PhoneNumberField(default='+254700000000')
    slug = AutoSlugField(populate_from='title', unique_with='company', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)  # Controls job visibility
    deadline = models.DateTimeField(null=True, blank=True)  # Application deadline

    class Meta:
        indexes = [
            models.Index(fields=['date_posted']),
            models.Index(fields=['title']),
        ]
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def clean(self):
        """ Validate deadline to ensure it's not in the past. """
        if self.deadline and self.deadline < timezone.now():
            raise ValidationError("Deadline cannot be in the past.")

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        super().save(*args, **kwargs)


class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    applicant = models.ForeignKey(
        User, related_name='applications', on_delete=models.CASCADE
    )
    job = models.ForeignKey(
        'Job', related_name='applications', on_delete=models.CASCADE
    )
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Pending'
    )
    applied_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('applicant', 'job')  # Prevent duplicate applications
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['applied_at']),
        ]
        ordering = ['-applied_at']

    def __str__(self):
        return f"{self.applicant} - {self.job.title} ({self.status})"

class Awarded(models.Model):
    application = models.OneToOneField(
        Application, related_name='awarded', on_delete=models.CASCADE
    )
    awarded_at = models.DateTimeField(default=timezone.now)
    contract_details = models.TextField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_completed = models.BooleanField(default=False)  # Track job completion

    class Meta:
        ordering = ['-awarded_at']

    def __str__(self):
        return f"Awarded: {self.application.applicant} - {self.application.job.title}"

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatMessage(models.Model):
    application = models.ForeignKey(
        'Application', related_name='messages', on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        User, related_name='sent_messages', on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User, related_name='received_messages', on_delete=models.CASCADE
    )
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)  # Track if the message is read
    seen_at = models.DateTimeField(null=True, blank=True)  # ✅ FIXED: Ensure seen_at is correctly defined
    attachments = models.JSONField(default=dict, blank=True)  # Store images/files

    class Meta:
        ordering = ['-timestamp']

    def mark_as_read(self):
        """Mark message as read and set seen_at timestamp."""
        if not self.is_read:
            self.is_read = True
            self.seen_at = timezone.now()
            self.save()

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.timestamp}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    job_role = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"