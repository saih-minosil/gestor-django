# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from utm import conversion


class Actionannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    annotationid = models.ForeignKey('Annotations', models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actionannotations'


class Actionby(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    affiliationid = models.ForeignKey('Affiliations', models.DO_NOTHING, db_column='AffiliationID')  # Field name made lowercase.
    isactionlead = models.IntegerField(db_column='IsActionLead')  # Field name made lowercase.
    roledescription = models.CharField(db_column='RoleDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actionby'


class Actiondirectives(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    directiveid = models.ForeignKey('Directives', models.DO_NOTHING, db_column='DirectiveID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actiondirectives'


class Actionextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    propertyid = models.ForeignKey('Extensionproperties', models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(db_column='PropertyValue', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actionextensionpropertyvalues'


class Actions(models.Model):
    actionid = models.AutoField(db_column='ActionID', primary_key=True)  # Field name made lowercase.
    actiontypecv = models.ForeignKey('CvActiontype', models.DO_NOTHING, db_column='ActionTypeCV')  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime')  # Field name made lowercase.
    begindatetimeutcoffset = models.IntegerField(db_column='BeginDateTimeUTCOffset')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    enddatetimeutcoffset = models.IntegerField(db_column='EndDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.
    actiondescription = models.CharField(db_column='ActionDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    actionfilelink = models.CharField(db_column='ActionFileLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actions'


class Affiliations(models.Model):
    affiliationid = models.AutoField(db_column='AffiliationID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey('People', models.DO_NOTHING, db_column='PersonID')  # Field name made lowercase.
    organizationid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='OrganizationID', blank=True, null=True)  # Field name made lowercase.
    isprimaryorganizationcontact = models.IntegerField(db_column='IsPrimaryOrganizationContact', blank=True, null=True)  # Field name made lowercase.
    affiliationstartdate = models.DateField(db_column='AffiliationStartDate')  # Field name made lowercase.
    affiliationenddate = models.DateField(db_column='AffiliationEndDate', blank=True, null=True)  # Field name made lowercase.
    primaryphone = models.CharField(db_column='PrimaryPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primaryemail = models.CharField(db_column='PrimaryEmail', max_length=255)  # Field name made lowercase.
    primaryaddress = models.CharField(db_column='PrimaryAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personlink = models.CharField(db_column='PersonLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'affiliations'


class Annotations(models.Model):
    annotationid = models.AutoField(db_column='AnnotationID', primary_key=True)  # Field name made lowercase.
    annotationtypecv = models.ForeignKey('CvAnnotationtype', models.DO_NOTHING, db_column='AnnotationTypeCV')  # Field name made lowercase.
    annotationcode = models.CharField(db_column='AnnotationCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    annotationtext = models.CharField(db_column='AnnotationText', max_length=500)  # Field name made lowercase.
    annotationdatetime = models.DateTimeField(db_column='AnnotationDateTime', blank=True, null=True)  # Field name made lowercase.
    annotationutcoffset = models.IntegerField(db_column='AnnotationUTCOffset', blank=True, null=True)  # Field name made lowercase.
    annotationlink = models.CharField(db_column='AnnotationLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    annotatorid = models.ForeignKey('People', models.DO_NOTHING, db_column='AnnotatorID', blank=True, null=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', models.DO_NOTHING, db_column='CitationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'annotations'


class Authorlists(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.
    personid = models.ForeignKey('People', models.DO_NOTHING, db_column='PersonID')  # Field name made lowercase.
    authororder = models.IntegerField(db_column='AuthorOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authorlists'


class Calibrationactions(models.Model):
    actionid = models.OneToOneField(Actions, models.DO_NOTHING, db_column='ActionID', primary_key=True)  # Field name made lowercase.
    calibrationcheckvalue = models.FloatField(db_column='CalibrationCheckValue', blank=True, null=True)  # Field name made lowercase.
    instrumentoutputvariableid = models.ForeignKey('Instrumentoutputvariables', models.DO_NOTHING, db_column='InstrumentOutputVariableID')  # Field name made lowercase.
    calibrationequation = models.CharField(db_column='CalibrationEquation', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'calibrationactions'


class Calibrationreferenceequipment(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Calibrationactions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    equipmentid = models.ForeignKey('Equipment', models.DO_NOTHING, db_column='EquipmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'calibrationreferenceequipment'


class Calibrationstandards(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Calibrationactions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    referencematerialid = models.ForeignKey('Referencematerials', models.DO_NOTHING, db_column='ReferenceMaterialID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'calibrationstandards'


class Categoricalresults(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    qualitycodecv = models.ForeignKey('CvQualitycode', models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoricalresults'


class Categoricalresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Categoricalresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoricalresultvalueannotations'


class Categoricalresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Categoricalresults, models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.CharField(db_column='DataValue', max_length=255)  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoricalresultvalues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset'),)


class Citationextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.
    propertyid = models.ForeignKey('Extensionproperties', models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(db_column='PropertyValue', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citationextensionpropertyvalues'


class Citationexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey('Externalidentifiersystems', models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    citationexternalidentifier = models.CharField(db_column='CitationExternalIdentifier', max_length=255)  # Field name made lowercase.
    citationexternalidentifieruri = models.CharField(db_column='CitationExternalIdentifierURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citationexternalidentifiers'


class Citations(models.Model):
    citationid = models.AutoField(db_column='CitationID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=255)  # Field name made lowercase.
    publicationyear = models.IntegerField(db_column='PublicationYear')  # Field name made lowercase.
    citationlink = models.CharField(db_column='CitationLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citations'


class CvActiontype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_actiontype'


class CvAggregationstatistic(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_aggregationstatistic'


class CvAnnotationtype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_annotationtype'


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


class CvVariabletype(models.Model):
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(db_column='SourceVocabularyURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_variabletype'


class Dataloggerfilecolumns(models.Model):
    dataloggerfilecolumnid = models.AutoField(db_column='DataloggerFileColumnID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='ResultID', blank=True, null=True)  # Field name made lowercase.
    dataloggerfileid = models.ForeignKey('Dataloggerfiles', models.DO_NOTHING, db_column='DataLoggerFileID')  # Field name made lowercase.
    instrumentoutputvariableid = models.ForeignKey('Instrumentoutputvariables', models.DO_NOTHING, db_column='InstrumentOutputVariableID')  # Field name made lowercase.
    columnlabel = models.CharField(db_column='ColumnLabel', max_length=50)  # Field name made lowercase.
    columndescription = models.CharField(db_column='ColumnDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    measurementequation = models.CharField(db_column='MeasurementEquation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scaninterval = models.FloatField(db_column='ScanInterval', blank=True, null=True)  # Field name made lowercase.
    scanintervalunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='ScanIntervalUnitsID', blank=True, null=True)  # Field name made lowercase.
    recordinginterval = models.FloatField(db_column='RecordingInterval', blank=True, null=True)  # Field name made lowercase.
    recordingintervalunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='RecordingIntervalUnitsID', related_name='dataloggerfilecolumns_recordingintervalunitsid_set', blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataloggerfilecolumns'


class Dataloggerfiles(models.Model):
    dataloggerfileid = models.AutoField(db_column='DataLoggerFileID', primary_key=True)  # Field name made lowercase.
    programid = models.ForeignKey('Dataloggerprogramfiles', models.DO_NOTHING, db_column='ProgramID')  # Field name made lowercase.
    dataloggerfilename = models.CharField(db_column='DataLoggerFileName', max_length=255)  # Field name made lowercase.
    dataloggerfiledescription = models.CharField(db_column='DataLoggerFileDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    dataloggerfilelink = models.CharField(db_column='DataLoggerFileLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataloggerfiles'


class Dataloggerprogramfiles(models.Model):
    programid = models.AutoField(db_column='ProgramID', primary_key=True)  # Field name made lowercase.
    affiliationid = models.ForeignKey(Affiliations, models.DO_NOTHING, db_column='AffiliationID')  # Field name made lowercase.
    programname = models.CharField(db_column='ProgramName', max_length=255)  # Field name made lowercase.
    programdescription = models.CharField(db_column='ProgramDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    programversion = models.CharField(db_column='ProgramVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    programfilelink = models.CharField(db_column='ProgramFileLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataloggerprogramfiles'


class Dataquality(models.Model):
    dataqualityid = models.IntegerField(db_column='DataQualityID', primary_key=True)  # Field name made lowercase.
    dataqualitytypecv = models.ForeignKey(CvDataqualitytype, models.DO_NOTHING, db_column='DataQualityTypeCV')  # Field name made lowercase.
    dataqualitycode = models.CharField(db_column='DataQualityCode', unique=True, max_length=255)  # Field name made lowercase.
    dataqualityvalue = models.FloatField(db_column='DataQualityValue', blank=True, null=True)  # Field name made lowercase.
    dataqualityvalueunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='DataQualityValueUnitsID', blank=True, null=True)  # Field name made lowercase.
    dataqualitydescription = models.CharField(db_column='DataQualityDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    dataqualitylink = models.CharField(db_column='DataQualityLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataquality'


class Datasetcitations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey('Datasets', models.DO_NOTHING, db_column='DataSetID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datasetcitations'


class Datasets(models.Model):
    datasetid = models.AutoField(db_column='DatasetID', primary_key=True)  # Field name made lowercase.
    datasetuuid = models.CharField(db_column='DatasetUUID', max_length=36)  # Field name made lowercase.
    datasettypecv = models.ForeignKey(CvDatasettype, models.DO_NOTHING, db_column='DatasetTypeCV')  # Field name made lowercase.
    datasetcode = models.CharField(db_column='DatasetCode', unique=True, max_length=50)  # Field name made lowercase.
    datasettitle = models.CharField(db_column='DatasetTitle', max_length=255)  # Field name made lowercase.
    datasetabstract = models.CharField(db_column='DatasetAbstract', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datasets'


class Datasetsresults(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Datasets, models.DO_NOTHING, db_column='DatasetID')  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datasetsresults'


class Derivationequations(models.Model):
    derivationequationid = models.AutoField(db_column='DerivationEquationID', primary_key=True)  # Field name made lowercase.
    derivationequation = models.TextField(db_column='DerivationEquation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'derivationequations'


class Directives(models.Model):
    directiveid = models.AutoField(db_column='DirectiveID', primary_key=True)  # Field name made lowercase.
    directivetypecv = models.ForeignKey(CvDirectivetype, models.DO_NOTHING, db_column='DirectiveTypeCV')  # Field name made lowercase.
    directivedescription = models.CharField(db_column='DirectiveDescription', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'directives'


class Equipment(models.Model):
    equipmentid = models.AutoField(db_column='EquipmentID', primary_key=True)  # Field name made lowercase.
    equipmentcode = models.CharField(db_column='EquipmentCode', unique=True, max_length=50)  # Field name made lowercase.
    equipmentname = models.CharField(db_column='EquipmentName', max_length=255)  # Field name made lowercase.
    equipmenttypecv = models.ForeignKey(CvEquipmenttype, models.DO_NOTHING, db_column='EquipmentTypeCV')  # Field name made lowercase.
    equipmentmodelid = models.ForeignKey('Equipmentmodels', models.DO_NOTHING, db_column='EquipmentModelID')  # Field name made lowercase.
    equipmentserialnumber = models.CharField(db_column='EquipmentSerialNumber', max_length=50)  # Field name made lowercase.
    equipmentownerid = models.ForeignKey('People', models.DO_NOTHING, db_column='EquipmentOwnerID')  # Field name made lowercase.
    equipmentvendorid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='EquipmentVendorID')  # Field name made lowercase.
    equipmentpurchasedate = models.DateTimeField(db_column='EquipmentPurchaseDate')  # Field name made lowercase.
    equipmentpurchaseordernumber = models.CharField(db_column='EquipmentPurchaseOrderNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipmentdescription = models.CharField(db_column='EquipmentDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    equipmentdocumentationlink = models.CharField(db_column='EquipmentDocumentationLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipment'


class Equipmentannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='EquipmentID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipmentannotations'


class Equipmentmodels(models.Model):
    equipmentmodelid = models.AutoField(db_column='EquipmentModelID', primary_key=True)  # Field name made lowercase.
    modelmanufacturerid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='ModelManufacturerID')  # Field name made lowercase.
    modelpartnumber = models.CharField(db_column='ModelPartNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modelname = models.CharField(db_column='ModelName', max_length=255)  # Field name made lowercase.
    modeldescription = models.CharField(db_column='ModelDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    isinstrument = models.IntegerField(db_column='IsInstrument')  # Field name made lowercase.
    modelspecificationsfilelink = models.CharField(db_column='ModelSpecificationsFileLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modellink = models.CharField(db_column='ModelLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipmentmodels'


class Equipmentused(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='EquipmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipmentused'


class Extensionproperties(models.Model):
    propertyid = models.AutoField(db_column='PropertyID', primary_key=True)  # Field name made lowercase.
    propertyname = models.CharField(db_column='PropertyName', max_length=255)  # Field name made lowercase.
    propertydescription = models.CharField(db_column='PropertyDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    propertydatatypecv = models.ForeignKey(CvPropertydatatype, models.DO_NOTHING, db_column='PropertyDataTypeCV')  # Field name made lowercase.
    propertyunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='PropertyUnitsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extensionproperties'


class Externalidentifiersystems(models.Model):
    externalidentifiersystemid = models.AutoField(db_column='ExternalIdentifierSystemID', primary_key=True)  # Field name made lowercase.
    externalidentifiersystemname = models.CharField(db_column='ExternalIdentifierSystemName', max_length=255)  # Field name made lowercase.
    identifiersystemorganizationid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='IdentifierSystemOrganizationID')  # Field name made lowercase.
    externalidentifiersystemdescription = models.CharField(db_column='ExternalIdentifierSystemDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    externalidentifiersystemurl = models.CharField(db_column='ExternalIdentifierSystemURL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'externalidentifiersystems'


class Featureactions(models.Model):
    featureactionid = models.AutoField(db_column='FeatureActionID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID')  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'featureactions'


class Instrumentoutputvariables(models.Model):
    instrumentoutputvariableid = models.AutoField(db_column='InstrumentOutputVariableID', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Equipmentmodels, models.DO_NOTHING, db_column='ModelID')  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    instrumentmethodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='InstrumentMethodID')  # Field name made lowercase.
    instrumentresolution = models.CharField(db_column='InstrumentResolution', max_length=255, blank=True, null=True)  # Field name made lowercase.
    instrumentaccuracy = models.CharField(db_column='InstrumentAccuracy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    instrumentrawoutputunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='InstrumentRawOutputUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'instrumentoutputvariables'


class Maintenanceactions(models.Model):
    actionid = models.OneToOneField(Actions, models.DO_NOTHING, db_column='ActionID', primary_key=True)  # Field name made lowercase.
    isfactoryservice = models.IntegerField(db_column='IsFactoryService')  # Field name made lowercase.
    maintenancecode = models.CharField(db_column='MaintenanceCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maintenancereason = models.CharField(db_column='MaintenanceReason', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maintenanceactions'


class Measurementresults(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='XLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='YLocationUnitsID', related_name='measurementresults_ylocationunitsid_set', blank=True, null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='ZLocationUnitsID', related_name='measurementresults_zlocationunitsid_set', blank=True, null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='TimeAggregationIntervalUnitsID', related_name='measurementresults_timeaggregationintervalunitsid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'measurementresults'


class Measurementresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Measurementresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'measurementresultvalueannotations'


class Measurementresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Measurementresults, models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'measurementresultvalues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset'),)


class Methodannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methodannotations'


class Methodcitations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methodcitations'


class Methodextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(db_column='PropertyValue', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methodextensionpropertyvalues'


class Methodexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    methodexternalidentifier = models.CharField(db_column='MethodExternalIdentifier', max_length=255)  # Field name made lowercase.
    methodexternalidentifieruri = models.CharField(db_column='MethodExternalIdentifierURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methodexternalidentifiers'


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


class Modelaffiliations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    modelid = models.IntegerField(db_column='ModelID')  # Field name made lowercase.
    affiliationid = models.IntegerField(db_column='AffiliationID')  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='IsPrimary')  # Field name made lowercase.
    roledescription = models.CharField(db_column='RoleDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modelaffiliations'


class Models(models.Model):
    modelid = models.AutoField(db_column='ModelID', primary_key=True)  # Field name made lowercase.
    modelcode = models.CharField(db_column='ModelCode', unique=True, max_length=50)  # Field name made lowercase.
    modelname = models.CharField(db_column='ModelName', max_length=255)  # Field name made lowercase.
    modeldescription = models.CharField(db_column='ModelDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modellink = models.CharField(db_column='ModelLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'models'


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


class People(models.Model):
    personid = models.AutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    personfirstname = models.CharField(db_column='PersonFirstName', max_length=255)  # Field name made lowercase.
    personmiddlename = models.CharField(db_column='PersonMiddleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personlastname = models.CharField(db_column='PersonLastName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'people'


class Personexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey(People, models.DO_NOTHING, db_column='PersonID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    personexternalidentifier = models.CharField(db_column='PersonExternalIdentifier', max_length=255)  # Field name made lowercase.
    personexternalidentifieruri = models.CharField(db_column='PersonExternalIdentifierURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personexternalidentifiers'


class Pointcoverageresults(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='ZLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedxspacing = models.FloatField(db_column='IntendedXSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedxspacingunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='IntendedXSpacingUnitsID', related_name='pointcoverageresults_intendedxspacingunitsid_set', blank=True, null=True)  # Field name made lowercase.
    intendedyspacing = models.FloatField(db_column='IntendedYSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedyspacingunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='IntendedYSpacingUnitsID', related_name='pointcoverageresults_intendedyspacingunitsid_set', blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pointcoverageresults'


class Pointcoverageresultvalueannotations(models.Model):
    bridgeid = models.BigAutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Pointcoverageresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pointcoverageresultvalueannotations'


class Pointcoverageresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Pointcoverageresults, models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='XLocationUnitsID')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation')  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='YLocationUnitsID', related_name='pointcoverageresultvalues_ylocationunitsid_set')  # Field name made lowercase.
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pointcoverageresultvalues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset', 'xlocation', 'xlocationunitsid', 'ylocation', 'ylocationunitsid', 'censorcodecv', 'qualitycodecv'),)


class Processinglevels(models.Model):
    processinglevelid = models.AutoField(db_column='ProcessingLevelID', primary_key=True)  # Field name made lowercase.
    processinglevelcode = models.CharField(db_column='ProcessingLevelCode', unique=True, max_length=50)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    explanation = models.CharField(db_column='Explanation', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'processinglevels'


class Profileresults(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='XLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='YLocationUnitsID', related_name='profileresults_ylocationunitsid_set', blank=True, null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedzspacing = models.FloatField(db_column='IntendedZSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedzspacingunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='IntendedZSpacingUnitsID', related_name='profileresults_intendedzspacingunitsid_set', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='IntendedTimeSpacingUnitsID', related_name='profileresults_intendedtimespacingunitsid_set', blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profileresults'


class Profileresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Profileresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profileresultvalueannotations'


class Profileresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Profileresults, models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation')  # Field name made lowercase.
    zaggregationinterval = models.FloatField(db_column='ZAggregationInterval')  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='ZLocationUnitsID')  # Field name made lowercase.
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='TimeAggregationIntervalUnitsID', related_name='profileresultvalues_timeaggregationintervalunitsid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profileresultvalues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset', 'zlocation', 'zaggregationinterval', 'zlocationunitsid', 'censorcodecv', 'qualitycodecv', 'timeaggregationinterval', 'timeaggregationintervalunitsid'),)


class Referencematerialexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    referencematerialid = models.ForeignKey('Referencematerials', models.DO_NOTHING, db_column='ReferenceMaterialID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    referencematerialexternalidentifier = models.CharField(db_column='ReferenceMaterialExternalIdentifier', max_length=255)  # Field name made lowercase.
    referencematerialexternalidentifieruri = models.CharField(db_column='ReferenceMaterialExternalIdentifierURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referencematerialexternalidentifiers'


class Referencematerials(models.Model):
    referencematerialid = models.AutoField(db_column='ReferenceMaterialID', primary_key=True)  # Field name made lowercase.
    referencematerialmediumcv = models.ForeignKey(CvMedium, models.DO_NOTHING, db_column='ReferenceMaterialMediumCV')  # Field name made lowercase.
    referencematerialorganizationid = models.ForeignKey(Organizations, models.DO_NOTHING, db_column='ReferenceMaterialOrganizationID')  # Field name made lowercase.
    referencematerialcode = models.CharField(db_column='ReferenceMaterialCode', unique=True, max_length=50)  # Field name made lowercase.
    referencemateriallotcode = models.CharField(db_column='ReferenceMaterialLotCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    referencematerialpurchasedate = models.DateTimeField(db_column='ReferenceMaterialPurchaseDate', blank=True, null=True)  # Field name made lowercase.
    referencematerialexpirationdate = models.DateTimeField(db_column='ReferenceMaterialExpirationDate', blank=True, null=True)  # Field name made lowercase.
    referencematerialcertificatelink = models.CharField(db_column='ReferenceMaterialCertificateLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referencematerials'


class Referencematerialvalues(models.Model):
    referencematerialvalueid = models.AutoField(db_column='ReferenceMaterialValueID', primary_key=True)  # Field name made lowercase.
    referencematerialid = models.ForeignKey(Referencematerials, models.DO_NOTHING, db_column='ReferenceMaterialID')  # Field name made lowercase.
    referencematerialvalue = models.FloatField(db_column='ReferenceMaterialValue')  # Field name made lowercase.
    referencematerialaccuracy = models.FloatField(db_column='ReferenceMaterialAccuracy', blank=True, null=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='UnitsID')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referencematerialvalues'


class Relatedactions(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedactionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='RelatedActionID', related_name='relatedactions_relatedactionid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedactions'


class Relatedannotations(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedannotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='RelatedAnnotationID', related_name='relatedannotations_relatedannotationid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedannotations'


class Relatedcitations(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedcitationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='RelatedCitationID', related_name='relatedcitations_relatedcitationid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedcitations'


class Relateddatasets(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Datasets, models.DO_NOTHING, db_column='DataSetID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relateddatasetid = models.ForeignKey(Datasets, models.DO_NOTHING, db_column='RelatedDatasetID', related_name='relateddatasets_relateddatasetid_set')  # Field name made lowercase.
    versioncode = models.CharField(db_column='VersionCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relateddatasets'


class Relatedequipment(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='EquipmentID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedequipmentid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='RelatedEquipmentID', related_name='relatedequipment_relatedequipmentid_set')  # Field name made lowercase.
    relationshipstartdatetime = models.DateTimeField(db_column='RelationshipStartDateTime')  # Field name made lowercase.
    relationshipstartdatetimeutcoffset = models.IntegerField(db_column='RelationshipStartDateTimeUTCOffset')  # Field name made lowercase.
    relationshipenddatetime = models.DateTimeField(db_column='RelationshipEndDateTime', blank=True, null=True)  # Field name made lowercase.
    relationshipenddatetimeutcoffset = models.IntegerField(db_column='RelationshipEndDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedequipment'


class Relatedfeatures(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.IntegerField(db_column='SamplingFeatureID')  # Field name made lowercase.
    relationshiptypecv = models.CharField(db_column='RelationshipTypeCV', max_length=255)  # Field name made lowercase.
    relatedfeatureid = models.IntegerField(db_column='RelatedFeatureID')  # Field name made lowercase.
    spatialoffsetid = models.IntegerField(db_column='SpatialOffsetID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedfeatures'


class Relatedmodels(models.Model):
    relatedid = models.AutoField(db_column='RelatedID', primary_key=True)  # Field name made lowercase.
    modelid = models.IntegerField(db_column='ModelID')  # Field name made lowercase.
    relationshiptypecv = models.CharField(db_column='RelationshipTypeCV', max_length=255)  # Field name made lowercase.
    relatedmodelid = models.IntegerField(db_column='RelatedModelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedmodels'


class Relatedresults(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedresultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='RelatedResultID', related_name='relatedresults_relatedresultid_set')  # Field name made lowercase.
    versioncode = models.CharField(db_column='VersionCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    relatedresultsequencenumber = models.IntegerField(db_column='RelatedResultSequenceNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedresults'


class Resultannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultannotations'


class Resultderivationequations(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    derivationequationid = models.ForeignKey(Derivationequations, models.DO_NOTHING, db_column='DerivationEquationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultderivationequations'


class Resultextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(db_column='PropertyValue', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultextensionpropertyvalues'


class Resultnormalizationvalues(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    normalizedbyreferencematerialvalueid = models.ForeignKey(Referencematerialvalues, models.DO_NOTHING, db_column='NormalizedByReferenceMaterialValueID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultnormalizationvalues'


class Results(models.Model):
    resultid = models.BigAutoField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    resultuuid = models.CharField(db_column='ResultUUID', max_length=36)  # Field name made lowercase.
    featureactionid = models.ForeignKey(Featureactions, models.DO_NOTHING, db_column='FeatureActionID')  # Field name made lowercase.
    resulttypecv = models.ForeignKey(CvResulttype, models.DO_NOTHING, db_column='ResultTypeCV')  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='UnitsID')  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('Taxonomicclassifiers', models.DO_NOTHING, db_column='TaxonomicClassifierID', blank=True, null=True)  # Field name made lowercase.
    processinglevelid = models.ForeignKey(Processinglevels, models.DO_NOTHING, db_column='ProcessingLevelID')  # Field name made lowercase.
    resultdatetime = models.DateTimeField(db_column='ResultDateTime', blank=True, null=True)  # Field name made lowercase.
    resultdatetimeutcoffset = models.BigIntegerField(db_column='ResultDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.
    validdatetime = models.DateTimeField(db_column='ValidDateTime', blank=True, null=True)  # Field name made lowercase.
    validdatetimeutcoffset = models.BigIntegerField(db_column='ValidDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.
    statuscv = models.ForeignKey(CvStatus, models.DO_NOTHING, db_column='StatusCV', blank=True, null=True)  # Field name made lowercase.
    sampledmediumcv = models.ForeignKey(CvMedium, models.DO_NOTHING, db_column='SampledMediumCV')  # Field name made lowercase.
    valuecount = models.IntegerField(db_column='ValueCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'results'


class Resultsdataquality(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Results, models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    dataqualityid = models.ForeignKey(Dataquality, models.DO_NOTHING, db_column='DataQualityID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultsdataquality'


class Samplingfeatureannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingfeatureannotations'


class Samplingfeatureextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(db_column='PropertyValue', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingfeatureextensionpropertyvalues'


class Samplingfeatureexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    samplingfeatureexternalidentifier = models.CharField(db_column='SamplingFeatureExternalIdentifier', max_length=255)  # Field name made lowercase.
    samplingfeatureexternalidentifieruri = models.CharField(db_column='SamplingFeatureExternalIdentifierURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingfeatureexternalidentifiers'


class Samplingfeatures(models.Model):
    samplingfeatureid = models.AutoField(db_column='SamplingFeatureID', primary_key=True)  # Field name made lowercase.
    samplingfeatureuuid = models.CharField(db_column='SamplingFeatureUUID', max_length=36)  # Field name made lowercase.
    samplingfeaturetypecv = models.ForeignKey(CvSamplingfeaturetype, models.DO_NOTHING, db_column='SamplingFeatureTypeCV')  # Field name made lowercase.
    samplingfeaturecode = models.CharField(db_column='SamplingFeatureCode', unique=True, max_length=50)  # Field name made lowercase.
    samplingfeaturename = models.CharField(db_column='SamplingFeatureName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    samplingfeaturedescription = models.CharField(db_column='SamplingFeatureDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    samplingfeaturegeotypecv = models.ForeignKey(CvSamplingfeaturegeotype, models.DO_NOTHING, db_column='SamplingFeatureGeotypeCV', blank=True, null=True)  # Field name made lowercase.
    featuregeometry = models.TextField(db_column='FeatureGeometry', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    featuregeometrywkt = models.CharField(db_column='FeatureGeometryWKT', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    elevation_m = models.FloatField(db_column='Elevation_m', blank=True, null=True)  # Field name made lowercase.
    elevationdatumcv = models.ForeignKey(CvElevationdatum, models.DO_NOTHING, db_column='ElevationDatumCV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingfeatures'

    def from_gestor(self, obj):
        self.samplingfeaturecode=obj.le_codigo_txt
        self.samplingfeaturename=obj.le_nombre_txt
        self.samplingfeaturedescription=obj.le_descripcion_txt
        self.elevation_m=obj.le_utm_z
        

class Sectionresults(models.Model):
    resultid = models.OneToOneField(Results, models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='YLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedxspacing = models.FloatField(db_column='IntendedXSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedxspacingunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='IntendedXSpacingUnitsID', related_name='sectionresults_intendedxspacingunitsid_set', blank=True, null=True)  # Field name made lowercase.
    intendedzspacing = models.FloatField(db_column='IntendedZSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedzspacingunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='IntendedZSpacingUnitsID', related_name='sectionresults_intendedzspacingunitsid_set', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='IntendedTimeSpacingUnitsID', related_name='sectionresults_intendedtimespacingunitsid_set', blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sectionresults'


class Sectionresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Sectionresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sectionresultvalueannotations'


class Sectionresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.BigIntegerField(db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xaggregationinterval = models.FloatField(db_column='XAggregationInterval')  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID')  # Field name made lowercase.
    zlocation = models.BigIntegerField(db_column='ZLocation')  # Field name made lowercase.
    zaggregationinterval = models.FloatField(db_column='ZAggregationInterval')  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID')  # Field name made lowercase.
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sectionresultvalues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset', 'xlocation', 'xaggregationinterval', 'xlocationunitsid', 'zlocation', 'zaggregationinterval', 'zlocationunitsid', 'censorcodecv', 'qualitycodecv', 'aggregationstatisticcv', 'timeaggregationinterval', 'timeaggregationintervalunitsid'),)


class Simulations(models.Model):
    simulationid = models.AutoField(db_column='SimulationID', primary_key=True)  # Field name made lowercase.
    actionid = models.IntegerField(db_column='ActionID')  # Field name made lowercase.
    simulationname = models.CharField(db_column='SimulationName', max_length=255)  # Field name made lowercase.
    simulationdescription = models.CharField(db_column='SimulationDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    simulationstartdatetime = models.DateTimeField(db_column='SimulationStartDateTime')  # Field name made lowercase.
    simulationstartdatetimeutcoffset = models.IntegerField(db_column='SimulationStartDateTimeUTCOffset')  # Field name made lowercase.
    simulationenddatetime = models.DateTimeField(db_column='SimulationEndDateTime')  # Field name made lowercase.
    simulationenddatetimeutcoffset = models.IntegerField(db_column='SimulationEndDateTimeUTCOffset')  # Field name made lowercase.
    timestepvalue = models.FloatField(db_column='TimeStepValue')  # Field name made lowercase.
    timestepunitsid = models.IntegerField(db_column='TimeStepUnitsID')  # Field name made lowercase.
    inputdatasetid = models.IntegerField(db_column='InputDataSetID', blank=True, null=True)  # Field name made lowercase.
    modelid = models.IntegerField(db_column='ModelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'simulations'


class Sites(models.Model):
    samplingfeatureid = models.IntegerField(db_column='SamplingFeatureID', primary_key=True)  # Field name made lowercase.
    sitetypecv = models.CharField(db_column='SiteTypeCV', max_length=255)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude')  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude')  # Field name made lowercase.
    spatialreferenceid = models.IntegerField(db_column='SpatialReferenceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sites'

    def from_gestor(self,obj):
        self.samplingfeatureid=obj.le_codigo_txt
        #self.sitetypecv=obj.le_tipo_estacion.te_codigo
        (x,y)= conversion.to_latlon(obj.le_utm_x,obj.le_utm_y, 30, 'T',strict=False)
        self.latitude=y
        self.longitude=obj.x
        #self.spatialreferenceid=obj.le_utm_huso


class Spatialoffsets(models.Model):
    spatialoffsetid = models.AutoField(db_column='SpatialOffsetID', primary_key=True)  # Field name made lowercase.
    spatialoffsettypecv = models.CharField(db_column='SpatialOffsetTypeCV', max_length=255)  # Field name made lowercase.
    offset1value = models.FloatField(db_column='Offset1Value')  # Field name made lowercase.
    offset1unitid = models.IntegerField(db_column='Offset1UnitID')  # Field name made lowercase.
    offset2value = models.FloatField(db_column='Offset2Value', blank=True, null=True)  # Field name made lowercase.
    offset2unitid = models.IntegerField(db_column='Offset2UnitID', blank=True, null=True)  # Field name made lowercase.
    offset3value = models.FloatField(db_column='Offset3Value', blank=True, null=True)  # Field name made lowercase.
    offset3unitid = models.IntegerField(db_column='Offset3UnitID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spatialoffsets'


class Spatialreferenceexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    spatialreferenceexternalidentifier = models.CharField(db_column='SpatialReferenceExternalIdentifier', max_length=255)  # Field name made lowercase.
    spatialreferenceexternalidentifieruri = models.CharField(db_column='SpatialReferenceExternalIdentifierURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spatialreferenceexternalidentifiers'


class Spatialreferences(models.Model):
    spatialreferenceid = models.AutoField(db_column='SpatialReferenceID', primary_key=True)  # Field name made lowercase.
    srscode = models.CharField(db_column='SRSCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    srsname = models.CharField(db_column='SRSName', max_length=255)  # Field name made lowercase.
    srsdescription = models.CharField(db_column='SRSDescription', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    srslink = models.CharField(db_column='SRSLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spatialreferences'


class Specimenbatchpostions(models.Model):
    featureactionid = models.OneToOneField(Featureactions, models.DO_NOTHING, db_column='FeatureActionID', primary_key=True)  # Field name made lowercase.
    batchpositionnumber = models.IntegerField(db_column='BatchPositionNumber')  # Field name made lowercase.
    batchpositionlabel = models.CharField(db_column='BatchPositionLabel', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specimenbatchpostions'


class Specimens(models.Model):
    samplingfeatureid = models.IntegerField(db_column='SamplingFeatureID', primary_key=True)  # Field name made lowercase.
    specimentypecv = models.CharField(db_column='SpecimenTypeCV', max_length=255)  # Field name made lowercase.
    specimenmediumcv = models.CharField(db_column='SpecimenMediumCV', max_length=255)  # Field name made lowercase.
    isfieldspecimen = models.IntegerField(db_column='IsFieldSpecimen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specimens'


class Specimentaxonomicclassifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.IntegerField(db_column='SamplingFeatureID')  # Field name made lowercase.
    taxonomicclassifierid = models.IntegerField(db_column='TaxonomicClassifierID')  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specimentaxonomicclassifiers'


class Spectraresults(models.Model):
    resultid = models.BigIntegerField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    spatialreferenceid = models.IntegerField(db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedwavelengthspacing = models.FloatField(db_column='IntendedWavelengthSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedwavelengthspacingunitsid = models.IntegerField(db_column='IntendedWavelengthSpacingUnitsID', blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.CharField(db_column='AggregationStatisticCV', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectraresults'


class Spectraresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Spectraresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectraresultvalueannotations'


class Spectraresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.BigIntegerField(db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    excitationwavelength = models.FloatField(db_column='ExcitationWavelength')  # Field name made lowercase.
    emissionwavelength = models.FloatField(db_column='EmissionWavelength')  # Field name made lowercase.
    wavelengthunitsid = models.IntegerField(db_column='WavelengthUnitsID')  # Field name made lowercase.
    censorcodecv = models.CharField(db_column='CensorCodeCV', max_length=255)  # Field name made lowercase.
    qualitycodecv = models.CharField(db_column='QualityCodeCV', max_length=255)  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectraresultvalues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset', 'excitationwavelength', 'emissionwavelength', 'wavelengthunitsid', 'censorcodecv', 'qualitycodecv', 'timeaggregationinterval', 'timeaggregationintervalunitsid'),)


class Taxonomicclassifierexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('Taxonomicclassifiers', models.DO_NOTHING, db_column='TaxonomicClassifierID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    taxonomicclassifierexternalidentifier = models.CharField(db_column='TaxonomicClassifierExternalIdentifier', max_length=255)  # Field name made lowercase.
    taxonomicclassifierexternalidentifieruri = models.CharField(db_column='TaxonomicClassifierExternalIdentifierURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxonomicclassifierexternalidentifiers'


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


class Timeseriesresults(models.Model):
    resultid = models.BigIntegerField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    spatialreferenceid = models.IntegerField(db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.IntegerField(db_column='IntendedTimeSpacingUnitsID', blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.CharField(db_column='AggregationStatisticCV', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeseriesresults'


class Timeseriesresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Timeseriesresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeseriesresultvalueannotations'


class Timeseriesresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.BigIntegerField(db_column='ResultID')  # Field name made lowercase.
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


class Trajectoryresults(models.Model):
    resultid = models.BigIntegerField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.IntegerField(db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedtrajectoryspacing = models.FloatField(db_column='IntendedTrajectorySpacing', blank=True, null=True)  # Field name made lowercase.
    intendedtrajectoryspacingunitsid = models.IntegerField(db_column='IntendedTrajectorySpacingUnitsID', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.IntegerField(db_column='IntendedTimeSpacingUnitsID', blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.CharField(db_column='AggregationStatisticCV', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trajectoryresults'


class Trajectoryresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Trajectoryresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trajectoryresultvalueannotations'


class Trajectoryresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.BigIntegerField(db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation')  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID')  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation')  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID')  # Field name made lowercase.
    trajectorydistance = models.FloatField(db_column='TrajectoryDistance')  # Field name made lowercase.
    trajectorydistanceaggregationinterval = models.FloatField(db_column='TrajectoryDistanceAggregationInterval')  # Field name made lowercase.
    trajectorydistanceunitsid = models.IntegerField(db_column='TrajectoryDistanceUnitsID')  # Field name made lowercase.
    censorcodecv = models.CharField(db_column='CensorCodeCV', max_length=255)  # Field name made lowercase.
    qualitycodecv = models.CharField(db_column='QualityCodeCV', max_length=255)  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trajectoryresultvalues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset', 'xlocation', 'xlocationunitsid', 'ylocation', 'ylocationunitsid', 'zlocation', 'zlocationunitsid', 'trajectorydistance', 'trajectorydistanceaggregationinterval', 'trajectorydistanceunitsid', 'censorcodecv', 'qualitycodecv', 'timeaggregationinterval'),)


class Transectresults(models.Model):
    resultid = models.BigIntegerField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    spatialreferenceid = models.IntegerField(db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedtransectspacing = models.FloatField(db_column='IntendedTransectSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedtransectspacingunitsid = models.IntegerField(db_column='IntendedTransectSpacingUnitsID', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.IntegerField(db_column='IntendedTimeSpacingUnitsID', blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.CharField(db_column='AggregationStatisticCV', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transectresults'


class Transectresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Transectresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transectresultvalueannotations'


class Transectresultvalues(models.Model):
    valueid = models.BigAutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.BigIntegerField(db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation')  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID')  # Field name made lowercase.
    transectdistance = models.FloatField(db_column='TransectDistance')  # Field name made lowercase.
    transectdistanceaggregationinterval = models.FloatField(db_column='TransectDistanceAggregationInterval')  # Field name made lowercase.
    transectdistanceunitsid = models.IntegerField(db_column='TransectDistanceUnitsID')  # Field name made lowercase.
    censorcodecv = models.CharField(db_column='CensorCodeCV', max_length=255)  # Field name made lowercase.
    qualitycodecv = models.CharField(db_column='QualityCodeCV', max_length=255)  # Field name made lowercase.
    aggregationstatisticcv = models.CharField(db_column='AggregationStatisticCV', max_length=255)  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transectresultvalues'
        unique_together = (('resultid', 'datavalue', 'valuedatetime', 'valuedatetimeutcoffset', 'xlocation', 'xlocationunitsid', 'ylocation', 'ylocationunitsid', 'transectdistance', 'transectdistanceaggregationinterval', 'transectdistanceunitsid', 'censorcodecv', 'qualitycodecv', 'aggregationstatisticcv', 'timeaggregationinterval', 'timeaggregationintervalunitsid'),)


class Units(models.Model):
    unitsid = models.AutoField(db_column='UnitsID', primary_key=True)  # Field name made lowercase.
    unitstypecv = models.ForeignKey(CvUnitstype, models.DO_NOTHING, db_column='UnitsTypeCV')  # Field name made lowercase.
    unitsabbreviation = models.CharField(db_column='UnitsAbbreviation', max_length=50)  # Field name made lowercase.
    unitsname = models.CharField(db_column='UnitsName', max_length=255)  # Field name made lowercase.
    unitslink = models.CharField(db_column='UnitsLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'units'


class Variableextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(db_column='PropertyValue', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variableextensionpropertyvalues'


class Variableexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    variableexternalidentifer = models.CharField(db_column='VariableExternalIdentifer', max_length=255)  # Field name made lowercase.
    variableexternalidentifieruri = models.CharField(db_column='VariableExternalIdentifierURI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variableexternalidentifiers'


class Variables(models.Model):
    variableid = models.AutoField(db_column='VariableID', primary_key=True)  # Field name made lowercase.
    variabletypecv = models.ForeignKey(CvVariabletype, models.DO_NOTHING, db_column='VariableTypeCV')  # Field name made lowercase.
    variablecode = models.CharField(db_column='VariableCode', unique=True, max_length=50)  # Field name made lowercase.
    variablenamecv = models.ForeignKey(CvVariablename, models.DO_NOTHING, db_column='VariableNameCV')  # Field name made lowercase.
    variabledefinition = models.CharField(db_column='VariableDefinition', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    speciationcv = models.ForeignKey(CvSpeciation, models.DO_NOTHING, db_column='SpeciationCV', blank=True, null=True)  # Field name made lowercase.
    nodatavalue = models.FloatField(db_column='NoDataValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variables'
