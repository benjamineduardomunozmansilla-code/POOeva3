from peewee import Model, AutoField, CharField, IntegerField, DateField, BooleanField
from datos.conexion import base_datos


class Autor(Model):
    id_autor = AutoField(primary_key=True)
    pais = IntegerField(column_name='pais', index=True, null=True)
    nombre = CharField(max_length=100, null=True)
    pseudonimo = CharField(max_length=25, null=True)
    fecha_nacimiento = DateField(null=True)
    fecha_defuncion = DateField(null=True)
    habilitado = BooleanField(default=True)

    class Meta:
        database = base_datos
        table_name = 'autores'