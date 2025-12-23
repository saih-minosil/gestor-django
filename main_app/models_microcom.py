# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from main_app.functions import generate_uuid
from utm import conversion

# CVs (options)

class CvActiontype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_actiontype'

    def __str__(self):
        return(f"{self.name}")    


class CvAggregationstatistic(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_aggregationstatistic'

    def __str__(self):
        return(f"{self.name}")     


class CvAnnotationtype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_annotationtype'

    def __str__(self):
        return(f"{self.name}")        


class CvCensorcode(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_censorcode'


class CvDataqualitytype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_dataqualitytype'


class CvDatasettype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_datasettype'


class CvDirectivetype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_directivetype'


class CvElevationdatum(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_elevationdatum'


class CvEquipmenttype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_equipmenttype'


class CvMedium(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_medium'

    def __str__(self):
        return self.name    


class CvMethodtype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_methodtype'


class CvOrganizationtype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_organizationtype'


class CvPropertydatatype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_propertydatatype'


class CvQualitycode(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_qualitycode'


class CvRelationshiptype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_relationshiptype'


class CvResulttype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_resulttype'


class CvSamplingfeaturegeotype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_samplingfeaturegeotype'


class CvSamplingfeaturetype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_samplingfeaturetype'


class CvSitetype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_sitetype'


class CvSpatialoffsettype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_spatialoffsettype'


class CvSpeciation(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_speciation'


class CvSpecimentype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_specimentype'


class CvStatus(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_status'


class CvTaxonomicclassifiertype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_taxonomicclassifiertype'


class CvUnitstype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_unitstype'


class CvVariablename(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_variablename'

    def __str__(self):
        return f"{self.name}"    


class CvVariabletype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_variabletype'

    def __str__(self):
        return f"{self.name}"    

class Taxonomicclassifiers(models.Model):
    taxonomicclassifierid = models.AutoField(db_column='TaxonomicClassifierID', primary_key=True)  # Field name made lowercase.
    taxonomicclassifiertypecv = models.ForeignKey(CvTaxonomicclassifiertype, models.DO_NOTHING, db_column='TaxonomicClassifierTypeCV')  # Field name made lowercase.
    taxonomicclassifiername = models.CharField(db_column='TaxonomicClassifierName', max_length=255)  # Field name made lowercase.
    taxonomicclassifiercommonname = models.CharField(db_column='TaxonomicClassifierCommonName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxonomicclassifierdescription = models.CharField(db_column='TaxonomicClassifierDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    parenttaxonomicclassifierid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentTaxonomicClassifierID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxonomicclassifiers'

class Processinglevels(models.Model):
    processinglevelid = models.AutoField(db_column='ProcessingLevelID', primary_key=True)  # Field name made lowercase.
    processinglevelcode = models.CharField(db_column='ProcessingLevelCode', unique=True, max_length=50)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    explanation = models.CharField(db_column='Explanation', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'processinglevels'

class Citations(models.Model):
    citationid = models.AutoField(db_column='CitationID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=255)  # Field name made lowercase.
    publicationyear = models.IntegerField(db_column='PublicationYear')  # Field name made lowercase.
    citationlink = models.CharField(db_column='CitationLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citations'

class Organizations(models.Model):
    organizationid = models.AutoField(db_column='OrganizationID', primary_key=True)  # Field name made lowercase.
    organizationtypecv = models.ForeignKey(CvOrganizationtype, models.DO_NOTHING, db_column='OrganizationTypeCV')  # Field name made lowercase.
    organizationcode = models.CharField(db_column='OrganizationCode', unique=True, max_length=50)  # Field name made lowercase.
    organizationname = models.CharField(db_column='OrganizationName', max_length=255)  # Field name made lowercase.
    organizationdescription = models.CharField(db_column='OrganizationDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    organizationlink = models.CharField(db_column='OrganizationLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parentorganizationid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentOrganizationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organizations'


class Methods(models.Model):
    methodid = models.AutoField(db_column='MethodID', primary_key=True)  # Field name made lowercase.
    methodtypecv = models.ForeignKey(CvMethodtype, models.DO_NOTHING, db_column='MethodTypeCV')  # Field name made lowercase.
    methodcode = models.CharField(db_column='MethodCode', unique=True, max_length=50)  # Field name made lowercase.
    methodname = models.CharField(db_column='MethodName', max_length=255)  # Field name made lowercase.
    methoddescription = models.CharField(db_column='MethodDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    methodlink = models.CharField(db_column='MethodLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='OrganizationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methods'

    def __str__(self):
        return(f"{self.methodid}:{self.methodname}")    

class People(models.Model):
    personid = models.AutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    personfirstname = models.CharField(db_column='PersonFirstName', max_length=255)  # Field name made lowercase.
    personmiddlename = models.CharField(db_column='PersonMiddleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personlastname = models.CharField(db_column='PersonLastName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'people'




class Actions(models.Model):
    actionid = models.AutoField(db_column='ActionID', primary_key=True)  # Field name made lowercase.
    actiontypecv = models.ForeignKey('CvActiontype', models.PROTECT, db_column='ActionTypeCV',default=CvActiontype.objects.get(term='observation'))  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.PROTECT, db_column='MethodID',default=Methods.objects.get(methodid=7))  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime',default=datetime.now)  # Field name made lowercase.
    begindatetimeutcoffset = models.IntegerField(db_column='BeginDateTimeUTCOffset',default=0)  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    enddatetimeutcoffset = models.IntegerField(db_column='EndDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.
    actiondescription = models.CharField(db_column='ActionDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    actionfilelink = models.CharField(db_column='ActionFileLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actions'
        verbose_name="Acción"
        verbose_name_plural="Acciones" 

    def __str__(self):
        featureactions=Featureactions.objects.filter(actionid=self.actionid)
        if featureactions:
            results=Results.objects.filter(featureactionid=featureactions[0].featureactionid)
            if results:
                tags=Resultannotations.objects.filter(resultid=results[0].resultid)
                for tag in tags:
                    anno=Annotations.objects.filter(annotationid=tag.annotationid_id)[0]
                    if anno.annotationcode=='Tag':
                        return f"{anno.annotationtext}"
        return f"{self.actionid}"
        #return(f"{self.actionid}")    


class Annotations(models.Model):
    annotationid = models.AutoField(db_column='AnnotationID', primary_key=True)  # Field name made lowercase.
    annotationtypecv = models.ForeignKey('CvAnnotationtype', models.PROTECT, db_column='AnnotationTypeCV',default='Result annotation')  # Field name made lowercase.
    annotationcode = models.CharField(db_column='AnnotationCode', max_length=50, blank=True, null=True, default='Tag')  # Field name made lowercase.
    annotationtext = models.CharField(db_column='AnnotationText', max_length=500)  # Field name made lowercase.
    annotationdatetime = models.DateTimeField(db_column='AnnotationDateTime', blank=True, null=True)  # Field name made lowercase.
    annotationutcoffset = models.IntegerField(db_column='AnnotationUTCOffset', blank=True, null=True)  # Field name made lowercase.
    annotationlink = models.CharField(db_column='AnnotationLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    annotatorid = models.ForeignKey('People', models.DO_NOTHING, db_column='AnnotatorID', blank=True, null=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', models.DO_NOTHING, db_column='CitationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'annotations'
        verbose_name="Anotación"
        verbose_name_plural="Anotaciones"


    def __str__ (self):
        return(f"{self.annotationcode}:{self.annotationtext}")   

    def set_tag(self,tag):
        self.annotationtext=tag
        self.annotationcode="Tag"
        self.save()    


class Derivationequations(models.Model):
    derivationequationid = models.AutoField(db_column='DerivationEquationID', primary_key=True)  # Field name made lowercase.
    derivationequation = models.TextField(db_column='DerivationEquation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'derivationequations'
        verbose_name="Ecuación"
        verbose_name_plural="Ecuaciones"


    def __str__(self):
        return(f"{self.derivationequation}")    


class Featureactions(models.Model):
    featureactionid = models.AutoField(db_column='FeatureActionID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.CASCADE, db_column='SamplingFeatureID')  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, models.CASCADE, db_column='ActionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'featureactions'
        verbose_name="Relación acción-estación"
        verbose_name_plural="Relaciones acción-estación"


    def __str__(self):
        result=Results.objects.filter(featureactionid=self.featureactionid)
        if(result):
            tags=Resultannotations.objects.filter(resultid=result[0].resultid)
            for tag in tags:
                anno=Annotations.objects.filter(annotationid=tag.annotationid_id)[0]
                if anno.annotationcode=='Tag':
                    return f"{self.featureactionid}:{anno.annotationtext}"
        return f"{self.featureactionid}"
        #return ""

        #return f"{self.featureactionid}:{self.samplingfeatureid}:{self.actionid}"    

    def from_gestor(self,obj):
        self.samplingfeatureid=Samplingfeatures.objects.get(samplingfeaturecode=obj.ls_remota.lr_estacion.le_codigo_txt)
        if not hasattr(self, 'actionid'): 
            self.actionid=Actions()     
            self.actionid.save()       
        self.save()


class Variables(models.Model):
    variableid = models.AutoField(db_column='VariableID', primary_key=True)  # Field name made lowercase.
    variabletypecv = models.ForeignKey(CvVariabletype, models.PROTECT, db_column='VariableTypeCV')  # Field name made lowercase.
    variablecode = models.CharField(db_column='VariableCode', unique=True, max_length=50)  # Field name made lowercase.
    variablenamecv = models.ForeignKey(CvVariablename, models.PROTECT, db_column='VariableNameCV')  # Field name made lowercase.
    variabledefinition = models.CharField(db_column='VariableDefinition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    speciationcv = models.ForeignKey(CvSpeciation, models.PROTECT, db_column='SpeciationCV', blank=True, null=True)  # Field name made lowercase.
    nodatavalue = models.FloatField(db_column='NoDataValue',default=-9999)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variables'
        verbose_name='Variable'
        verbose_name_plural='Variables'

    def __str__(self):
        return f"{self.variabledefinition}"



class Relatedresults(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.CASCADE, db_column='ResultID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.PROTECT, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedresultid = models.ForeignKey('Results', models.PROTECT, db_column='RelatedResultID', related_name='relatedresults_relatedresultid_set')  # Field name made lowercase.
    versioncode = models.CharField(db_column='VersionCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    relatedresultsequencenumber = models.IntegerField(db_column='RelatedResultSequenceNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedresults'
        verbose_name="Relación entre resultados"
        verbose_name_plural="Relaciones entre resultados"


class Resultannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.CASCADE, db_column='ResultID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.CASCADE, db_column='AnnotationID')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime',default=datetime.now)  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime',default=datetime.now)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultannotations'
        verbose_name = 'Anotación sobre señal'
        verbose_name_plural = 'Anotaciones sobre señales'

    def __str__(self):
        return f"{self.annotationid}"

    def from_annotation(self,annotation,resultid):
        self.annotationid=annotation
        self.resultid=resultid
        self.begindatetime =datetime.now()  # Field name made lowercase.
        self.enddatetime = datetime.now()  # Field name made lowercase.
        self.save()         


class Resultderivationequations(models.Model):
    resultid = models.OneToOneField('Results', models.CASCADE, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    derivationequationid = models.ForeignKey(Derivationequations, models.PROTECT, db_column='DerivationEquationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultderivationequations'

    def __str__(self):
        return f"{self.derivationequationid}"     


class Units(models.Model):
    unitsid = models.AutoField(db_column='UnitsID', primary_key=True)  # Field name made lowercase.
    unitstypecv = models.ForeignKey(CvUnitstype, models.DO_NOTHING, db_column='UnitsTypeCV')  # Field name made lowercase.
    unitsabbreviation = models.CharField(db_column='UnitsAbbreviation', max_length=50)  # Field name made lowercase.
    unitsname = models.CharField(db_column='UnitsName', max_length=255)  # Field name made lowercase.
    unitslink = models.CharField(db_column='UnitsLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'units'
        verbose_name= 'Unidad'
        verbose_name_plural= 'Unidades'
    
    def __str__(self):
        return f"{self.unitsname}"



class Results(models.Model):
    resultid = models.BigAutoField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    resultuuid = models.CharField(db_column='ResultUUID', max_length=36,default=generate_uuid)  # Field name made lowercase.
    featureactionid = models.ForeignKey('Featureactions', models.CASCADE, db_column='FeatureActionID',verbose_name="Acción")  # Field name made lowercase.
    resulttypecv = models.ForeignKey('CvResulttype', models.PROTECT, db_column='ResultTypeCV',default='Time series coverage',verbose_name="Tipo de resultado")  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.PROTECT, db_column='VariableID',verbose_name="Tipo de señal",default=Variables.objects.get(variableid=1))  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', models.PROTECT, db_column='UnitsID',verbose_name="Unidades",default=Units.objects.get(unitsid=1))  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('Taxonomicclassifiers', models.DO_NOTHING, db_column='TaxonomicClassifierID', blank=True, null=True)  # Field name made lowercase.
    processinglevelid = models.ForeignKey('Processinglevels', models.DO_NOTHING, db_column='ProcessingLevelID',default=1)  # Field name made lowercase.
    resultdatetime = models.DateTimeField(db_column='ResultDateTime', blank=True, null=True)  # Field name made lowercase.
    resultdatetimeutcoffset = models.BigIntegerField(db_column='ResultDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.
    validdatetime = models.DateTimeField(db_column='ValidDateTime', blank=True, null=True)  # Field name made lowercase.
    validdatetimeutcoffset = models.BigIntegerField(db_column='ValidDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.
    statuscv = models.ForeignKey('CvStatus', models.DO_NOTHING, db_column='StatusCV', blank=True, null=True)  # Field name made lowercase.
    sampledmediumcv = models.ForeignKey('CvMedium', models.DO_NOTHING, db_column='SampledMediumCV',default='Liquid aqueous')  # Field name made lowercase.
    valuecount = models.IntegerField(db_column='ValueCount',default=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'results'
        verbose_name="Señal microcoom"
        verbose_name_plural="Señales microcoom"
        ordering=['resultid']

    def __str__(self):
        tags=Resultannotations.objects.filter(resultid=self.resultid)#[0].annotationid#
        for tag in tags:
            anno=Annotations.objects.filter(annotationid=tag.annotationid_id)[0]
            if anno.annotationcode=='Tag':
                return f"{anno.annotationtext}"
        return f"{self.resultid}"

    def delete(self, using=None, keep_parents=False):
        featureactions=Featureactions.objects.filter(featureactionid=self.featureactionid.featureactionid)
        if featureactions:
            actions=Actions.objects.filter(actionid=featureactions[0].actionid_id)#.featureactionid)
            if actions:
                print(f"borrando {actions}")
                actions.delete()                
            featureactions.delete()
        super().delete()

    def from_gestor(self,obj):
        feature_action=models_microcom.Featureactions()
        feature_action.from_gestor(obj)
        feature_action.save()
        if obj.ls_naturaleza==1:
            natur="a"
        else:
            natur="d"
        if obj.ls_origen=="CALCULO":
            orig="c"
        else:       
            orig="i"
        tipo_senal=obj.ls_tipo_senal.lower()    
        variableid=Variables.objects.filter(variablecode=f"{orig}{natur}{tipo_senal}")   
        if(variableid): 
            self.variableid=variableid[0]
        else:
            self.variableid=Variables.objects.get(variableid=1)
        self.unitsid=obj.unitsid
        self.save() 
            
    def add_anno(self,anno_code,anno_txt):
        result_annotations = models_microcom.Resultannotations.objects.filter(resultid=self.resultid)
        for ra in result_annotations:
            anno=models_microcom.Annotations.objects.filter(annotationcode=ra.annotationid_id)
            if anno:
                if anno.annotationcode==anno_code:
                    anno.annotationtext=anno_txt
                    anno.save()
                    return anno
        #Si no existe el tag
        anno=models_microcom.Annotations()
        anno.annotationcode=anno_code
        anno.annotationtext=anno_txt
        anno.save()
        ra=models_microcom.Resultannotations()
        ra.resultid=self.resultid
        ra.annotationid=anno.annotationid
        ra.save()
        
    def get_anno(self,anno_code):
        result_annotations = models_microcom.Resultannotations.objects.filter(resultid=self.resultid)
        for ra in result_annotations:
            anno=models_microcom.Annotations.objects.filter(annotationcode=ra.annotationid_id)
            if anno:
                if anno.annotationcode==anno_code:
                    return anno    
        return None  



# USADO PARA "ESTACIONES" EN CONJUNTO CON "SITES"
class Samplingfeatures(models.Model):
    samplingfeatureid = models.AutoField(db_column='SamplingFeatureID', primary_key=True,verbose_name="ID")  # Field name made lowercase.
    samplingfeatureuuid = models.CharField(db_column='SamplingFeatureUUID', max_length=36,default=generate_uuid)  # Field name made lowercase.
    samplingfeaturetypecv = models.ForeignKey(CvSamplingfeaturetype, models.PROTECT, db_column='SamplingFeatureTypeCV',default="Site",verbose_name="Tipo")  # Field name made lowercase.
    samplingfeaturecode = models.CharField(db_column='SamplingFeatureCode', unique=True, max_length=50,verbose_name="Codigo Estación")  # Field name made lowercase.
    samplingfeaturename = models.CharField(db_column='SamplingFeatureName', max_length=255, blank=True, null=True,verbose_name="Nombre Estación")  # Field name made lowercase.
    samplingfeaturedescription = models.CharField(db_column='SamplingFeatureDescription', max_length=5000, blank=True, null=True,verbose_name="Descripcion Estación")  # Field name made lowercase.
    samplingfeaturegeotypecv = models.ForeignKey(CvSamplingfeaturegeotype, models.PROTECT, db_column='SamplingFeatureGeotypeCV', blank=True, null=True, default="Point",verbose_name="Tipo geográfico")  # Field name made lowercase.
    featuregeometry = models.TextField(db_column='FeatureGeometry', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    featuregeometrywkt = models.CharField(db_column='FeatureGeometryWKT', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    elevation_m = models.FloatField(db_column='Elevation_m', blank=True, null=True)  # Field name made lowercase.
    elevationdatumcv = models.ForeignKey(CvElevationdatum, models.PROTECT, db_column='ElevationDatumCV', blank=True, null=True,default="MSL")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingfeatures'

        verbose_name="Estacion microcoom"
        verbose_name_plural="Estaciones microcoom"
        ordering=['samplingfeatureid']

    def __str__(self):
        return f"{self.samplingfeaturecode}_{self.samplingfeaturename}"

    def delete(self, using=None, keep_parents=False):
        featureactions=Featureactions.objects.filter(samplingfeatureid=self.samplingfeatureid)
        if featureactions:
            actions=Actions.objects.filter(featureactionid=featureactions[0].featureactionid)
            if actions:
                print(f"borrando {actions}")
                actions.delete()                
            featureactions.delete()
        super().delete()   

    def from_gestor(self, obj):
        self.samplingfeaturecode=obj.le_codigo_txt
        self.samplingfeaturename=obj.le_nombre_corto
        self.samplingfeaturedescription=obj.le_nombre
        self.elevation_m=obj.le_utm_z     
'''
    def save(self, *args, **kwargs):
        self.samplingfeatureuuid=self.generate_uuid() 
        return super().save(*args, **kwargs)

    def generate_uuid(self):
        generate_uuid(f"station_{self.samplingfeatureid}")    
'''


class Sites(models.Model):
    samplingfeatureid=models.OneToOneField(Samplingfeatures, models.CASCADE, db_column='SamplingFeatureID', primary_key=True)  # Field name made lowercase.
    # samplingfeatureid = models.IntegerField(db_column='SamplingFeatureID', primary_key=True)  # Field name made lowercase.
    sitetypecv = models.CharField(db_column='SiteTypeCV', max_length=255)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude')  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude')  # Field name made lowercase.
    spatialreferenceid = models.IntegerField(db_column='SpatialReferenceID',default=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sites'

    def __str__(self):
        return f"{self.samplingfeatureid}"

    def from_gestor(self,obj):
        #self.samplingfeatureid=obj.le_codigo_txt
        #self.sitetypecv=obj.le_tipo_estacion.te_codigo
        (x,y)= conversion.to_latlon(obj.le_utm_x,obj.le_utm_y, 30, 'T',strict=False)
        self.latitude=y
        self.longitude=x
        #self.spatialreferenceid=obj.le_utm_huso    

#Resultados (Son las señales junto con Result y Action)
class Timeseriesresults(models.Model):
    resultid = models.OneToOneField(Results,db_column='ResultID', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID', blank=True, null=True,default=3)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID', blank=True, null=True,default=3)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID', blank=True, null=True,default=3)  # Field name made lowercase.
    spatialreferenceid = models.IntegerField(db_column='SpatialReferenceID', blank=True, null=True,default=2)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True, null=True,default=5,verbose_name="Intervalo entre mediciones")  # Field name made lowercase.
    intendedtimespacingunitsid = models.IntegerField(db_column='IntendedTimeSpacingUnitsID', blank=True, null=True,default=5,verbose_name="Unidades del intervalo entre mediciones")  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic,on_delete=models.PROTECT,db_column='AggregationStatisticCV',default ="Average",verbose_name="Estadística de agregación")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeseriesresults'
        verbose_name='Datos señal'
        verbose_name_plural='Datos señales'

    def __str__(self):
        return f"{self.resultid}"    

    def save(self, *args, **kwargs):
        print(f"Saving {self.resultid}")
        featureactionid=Results.objects.get(resultid=self.resultid.resultid).featureactionid
        samplingfeatureid=Featureactions.objects.get(featureactionid=featureactionid.featureactionid).samplingfeatureid
        site=Sites.objects.get(samplingfeatureid=samplingfeatureid)
        samplingfeature=Samplingfeatures.objects.get(samplingfeatureid=samplingfeatureid.samplingfeatureid)
        print(f"Coordenadas: {site.longitude},{site.latitude}")
        location=conversion.from_latlon(site.latitude, site.longitude,29)
        xlocation=location[0]
        ylocation=location[1]
        zlocation=samplingfeature.elevation_m            
        #print(f"XLOCATION: {xlocation}, YLOCATION: {ylocation}, ZLOCATION: {zlocation}")
        print(f"LOCATION: {location} ZLOCATION: {zlocation}")
        self.xlocation=xlocation
        self.ylocation=ylocation
        self.zlocation=zlocation
        return super().save(*args, **kwargs)



    
#Anotaciones de los valores (relación)
class Timeseriesresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Timeseriesresultvalues', models.CASCADE, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.PROTECT, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeseriesresultvalueannotations'

#Los valores como tal (DATOS)
class Timeseriesresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Results, models.CASCADE, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    censorcodecv = models.CharField(db_column='CensorCodeCV', max_length=255)  # Field name made lowercase.
    qualitycodecv = models.CharField(db_column='QualityCodeCV', max_length=255)  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeseriesresultvalues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset', 'censorcodecv', 'qualitycodecv', 'timeaggregationinterval', 'timeaggregationintervalunitsid'),)
        verbose_name='Valor señal'
        verbose_name_plural='Valores señales'

    def __str__(self):
        return f"{self.valuedatetime}:{self.datavalue}({self.qualitycodecv})"    
