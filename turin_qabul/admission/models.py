from django.db import models

from admission.choices import GenderChoices


class Admission(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(choices=GenderChoices.choices, max_length=10, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    country_of_birth = models.ForeignKey(
        'admission.Country', 
        on_delete=models.PROTECT, 
        related_name='birth_country_admissions',
        null=False, 
        blank=False
    )

    nationality = models.ForeignKey(
        'admission.Country', 
        on_delete=models.PROTECT, 
        related_name='nationality_admissions',
        null=False, 
        blank=False
    )
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    school_name = models.CharField(max_length=100, null=False, blank=False)
    english_certificate = models.CharField(
        max_length=50,
        choices=[
            ('IELTS', 'IELTS'),
            ('TOEFL', 'TOEFL'),
            ('CEFR', 'CEFR'),
            ('Other', 'Other'),
        ],
        blank=True,
        null=True,
    )
    english_certificate_score = models.CharField(max_length=30, blank=True, null=True)
    sat_score = models.CharField(max_length=10, blank=True, null=True)
    program = models.ForeignKey('admission.Program', on_delete=models.PROTECT, null=False, blank=False)
    # File fields
    passport = models.FileField(upload_to='documents/passports/')
    language_certificate = models.FileField(upload_to='documents/language_certificates/')
    sat_certificate = models.FileField(upload_to='documents/sat_certificates/', blank=True, null=True)
    photo = models.FileField(upload_to='documents/photos/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Admission'
        verbose_name_plural = 'Admissions'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


class Country(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
    


class Program(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

    def __str__(self):
        return self.name