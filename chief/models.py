from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import os

def generate_file_path(instance, filename, image_category):
    
    upload_path = f"media/accounts/{image_category}-image"
    return os.path.join(upload_path, filename)

def get_therapist_idproof_file_path(instance, filename):
    return generate_file_path(instance, filename, 'therapist-idproof')

THERAPIST_REQUEST_STATUS_CHOICES = [
    ("pending", 'Pending'),
    ("approved", 'Approved'),
    ("rejected", 'Rejected'),
]

THERAPIST_GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )


PATIENT_GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )


class Therapist(models.Model):
    therapist_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    total_years_of_experience = models.IntegerField()
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    qualification = models.CharField(max_length=256, null=True, blank=True)
    id_proof = models.ImageField(upload_to=get_therapist_idproof_file_path, null=True, blank=True)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=THERAPIST_GENDER_CHOICES, null=True, blank=True)
    request_status = models.CharField(choices=THERAPIST_REQUEST_STATUS_CHOICES, null=True, blank=True)
    joined_from = models.DateTimeField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,related_name="profile")
    password = models.CharField(null=True, blank=True)

    class Meta:
        db_table = 'chief_therapist'
        verbose_name = _('Therapist')
        verbose_name_plural = _('Therapists')
        ordering = ('therapist_id',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.therapist_id:
            # Generate therapist_id if not set
            self.therapist_id = self.generate_therapist_id()
        super().save(*args, **kwargs)

    def generate_therapist_id(self):
        # Logic to generate unique therapist_id
        # For example: THST01, THST02, etc.
        # You can use a counter or any other method to generate unique IDs
        # Replace this with your actual logic
        return 'THST' + str(self.pk).zfill(2)
    
    
class Patient(models.Model):
    patient_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField()
    joined_from = models.DateTimeField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=PATIENT_GENDER_CHOICES, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(null=True, blank=True)
    last_posted_problem = models.ForeignKey('Problem', on_delete=models.SET_NULL, related_name='last_posted_for_patient', null=True, blank=True)

    class Meta:
        db_table = 'chief_patient'
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')
        ordering = ('patient_id',)

    def __str__(self):
        return self.name


class Problem(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='problem', null=True, blank=True)

    class Meta:
        db_table = 'chief_problem'
        verbose_name = _('Problem')
        verbose_name_plural = _('Problems')
        ordering = ('title',)
        
    def __str__(self):
        return f"{self.title} - {self.patient.name}"


class Solution(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, null=True, blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='solution', null=True, blank=True)
    solution = models.TextField()
    date_added = models.DateTimeField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'chief_solution'
        verbose_name = _('Solution')
        verbose_name_plural = _('Solutions')
        ordering = ('therapist',)
        
    def __str__(self):
        return self.therapist.name
