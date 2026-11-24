from peewee import (
    Model, AutoField, CharField, IntegerField,
    DateField, BooleanField, ForeignKeyField
)
from datos.conexion import base_datos
from datos.modelos.pais import Pais


class Usuario(Model):
    id_usuario = AutoField(primary_key=True)
    rut = CharField(max_length=11, null=True)
    nombre = CharField(max_length=25)
    apellido = CharField(max_length=25)
    correo = CharField(max_length=255)
    pais = ForeignKeyField(Pais, column_name='pais', backref='usuarios', null=True)
    fecha_nacimiento = DateField(null=True)
    genero = IntegerField()
    fecha_incorporacion = DateField()
    habilitado = BooleanField(default=True)

    class Meta:
        database = base_datos
        table_name = 'usuarios'
