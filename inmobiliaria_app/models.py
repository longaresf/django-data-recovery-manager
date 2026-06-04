from django.db import models

# Create your models here.

class Region(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)

class Provincia(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=23, null=False, blank=False)
    provincia_region = models.ForeignKey(Region, related_name = 'prov_region', on_delete=models.CASCADE)

class Comuna(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    comuna_provincia = models.ForeignKey(Provincia, related_name = 'com_prov', on_delete=models.CASCADE)
    
class Usuario(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, null=False)
    nombres = models.CharField(max_length=30, null=False, blank=False)
    apellidos = models.CharField(max_length=30, null=False, blank=False)
    direccion = models.CharField(max_length=80, null=False, blank=False)
    telefono = models.CharField(max_length=16, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    USUARIO = (('ARRENDADOR', 'Arrendador'),
                 ('ARRENDATARIO', 'Arrendatario'))
    tipo_user = models.CharField(choices=USUARIO, default='ARRENDADOR', max_length=12)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return '%s, %s' % (self.apellidos, self.nombres)

class Inmueble(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=80, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    m2_construidos = models.IntegerField(null=False, blank=False)
    m2_totales = models.IntegerField(null=False, blank=False)
    cant_estacionamientos = models.CharField(max_length=2, null=False, blank=False)
    cant_habitaciones = models.CharField(max_length=2, null=False, blank=False)
    cant_banios = models.CharField(max_length=2, null=False, blank=False)
    direccion = models.CharField(max_length=80, null=False, blank=False)
    comuna = models.CharField(max_length=30, null=False, blank=False)

    INMUEBLES = (('CASA', 'Casa'),
                 ('DPTO', 'Departamento'),
                 ('PARC', 'Parcela'))
    tipo_inmueble = models.CharField(choices=INMUEBLES, default='DPTO', max_length=12)
    precio_mes_arriendo = models.IntegerField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    usuario = models.ManyToManyField(Usuario, related_name='user_inmueble', through='Usuario_Inmueble')
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.nombre + " en la comuna de " + self.comuna

class Image(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    inmueble = models.ForeignKey(Inmueble, related_name = 'img_inm', on_delete=models.CASCADE)

class Usuario_Inmueble(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    arrendatario = models.ForeignKey(Usuario, related_name = 'user', on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, related_name = 'inmueble', on_delete=models.CASCADE)

    ESTADO = (('0', 'Aprobado'),
                 ('1', 'Rechazado'),
                 ('2', 'Pendiente'))
    estado = models.CharField(choices=ESTADO, default='Pendiente', max_length=12)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "Arrendatario: " + self.arrendatario.nombres + "" + self.arrendatario.apellidos + " Propiedad: " +  self.inmueble.nombre + " en la comuna de " + self.inmueble.comuna
