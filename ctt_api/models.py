from django.db import models

# ctt_dummy database table
class CaseTT(models.Model):
    CTT_ID = models.AutoField(primary_key=True)
    Case_Description = models.CharField(max_length=255)
    IMSI = models.BigIntegerField()
    MSISDN = models.BigIntegerField()
    CTT_Created_Date = models.DateTimeField()

    class Meta:
        db_table = 'case_tt'
        managed = False  # Table already exists in ctt_dummy database


# datacollector_dummy database table
class MSISDNIMSI(models.Model):
    MSISDN = models.BigIntegerField()
    IMSI = models.BigIntegerField()

    class Meta:
        db_table = 'msisdn_imsi'
        managed = False  # Table already exists in datacollector_dummy database
        constraints = [
            models.UniqueConstraint(fields=['MSISDN', 'IMSI'], name='unique_msisdn_imsi')
        ]
