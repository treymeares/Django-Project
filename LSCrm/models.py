from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    address_line_3 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=11, blank=True, null=True)
    execute_from_command_line = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    description = models.CharField(max_length=600)
    key_contacts= models.CharField(max_length=100, blank=True, null=True)


class ContactPerson(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)

class CompanyIndustry(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    industryType = models.CharField(max_length=200)
    products_interested_in = models.CharField(max_length=1000, blank=True, null=True)
    avgerage_industry_spend = models.CharField(max_length=200, blank = True, null = True)