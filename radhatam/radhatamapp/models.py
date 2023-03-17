from django.db import models

# Create your models here.
DATA_TYPES = (
    ('TEXT', 'Text'),
    ('INTEGER', 'Integer'),
    ('NUMERIC', 'Numeric'),
    ('DATE', 'Date'),
    ('BINARY', 'Binary'),
    ('PNG_IMAGE', 'PNG Image'),
    ('COLUMN', 'Column'),
    ('DERIVED', 'Derived'),
)


FUNCTION_TYPES = (
    ('CALCULATION', 'Calculation'),
    ('VISUALIZE', 'Visualize'),
    ('DATASCIENCE', 'DataScience'),
)

OP_TYPES = (
    ('EXACT', 'EXACT'),
    ('NOT', 'NOT'),
    ('LT','LESS THAN')

)

SQL_OP_TYPES = {'EXACT': '=', 'NOT': '!=','LT':'<'}


class Entity(models.Model):
    name = models.CharField(max_length=30, unique=True)
    # child = models.ForeignKey('self',on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.name


class FunctionMeta(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(
        max_length=20, choices=FUNCTION_TYPES, default='CALCULATION')
    return_type = models.CharField(
        max_length=20, choices=DATA_TYPES, default='TEXT')
    return_sql = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class ArgumentMeta(models.Model):
    function = models.ForeignKey(
        FunctionMeta, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=DATA_TYPES, default='TEXT')

    def __str__(self):
        return self.name


class Field(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True)
    actual_name = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    main = models.BooleanField(default=False)
    type = models.CharField(max_length=64, choices=DATA_TYPES, default='TEXT')
    child_entity_id = models.IntegerField(null=True)
    child_field_id = models.IntegerField(null=True)
    derived_level = models.IntegerField(default=0)
    function = models.ForeignKey(
        FunctionMeta, on_delete=models.DO_NOTHING, null=True)
    # order = models.IntegerField()

    def __str__(self):
        return self.name


class FieldFilter(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=False)
    filter_col = models.CharField(max_length=30, null=False)
    filter_op = models.CharField(
        max_length=30, null=False, choices=OP_TYPES, default='EXACT')
    filter_val = models.CharField(max_length=120, null=False)


class DerivedFieldArgument(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True)
    argument_name = models.CharField(max_length=30, null=True)
    argument_value = models.CharField(max_length=30, null=True)
    argument_type = models.CharField(max_length=30, null=True)
