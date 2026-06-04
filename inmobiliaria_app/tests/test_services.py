from django.test import TestCase
from django.db import models
from inmobiliaria_app.models import Usuario, Inmueble
from inmobiliaria_app.services import crear_usuario, crear_inmueble, listar_propiedades, solicitud_arriendo, publicar_propiedades, lista_propiedades_comuna, update_inmueble, eliminar_propiedades, aceptar_arrendatario

class ServicesTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    # def test_crear_usuario(self):
    #     nuevo_arrendatario = Usuario.objects.create(rut='111111111', nombres='Juan Pedro', apellidos='Aguilar Silva', direccion='Pandora 3212, Maipu, Santiago', telefono='999999999', email='juan@mail.cl', tipo_user='Arrendatario', activo='True', creado_por='Admin')
    #     self.assertTrue(nuevo_arrendatario)
        
    # def test_crear_inmueble(self):
    #     nuevo_inmueble = Inmueble.objects.create(nombre='Departamento Francisco De Villagra', descripcion='No amoblado, 1 dormitorio, 1 baño, No Admite mascotas, 1 estacionamiento, Año de construcción: 2015', m2_construidos=28, m2_totales=33, cant_estacionamientos='1', cant_habitaciones='1', cant_banios='1', direccion='Francisco De Villagra', comuna='Ñuñoa', tipo_inmueble='Departamento', precio_mes_arriendo=530000, activo=True, creado_por='Admin')
    #     self.assertTrue(nuevo_inmueble)

    # def test_lista_propiedades_comuna(self):
    #     inmuebles_comuna = Inmueble.objects.filter(comuna='Ñuñoa')
    #     for i in inmuebles_comuna:
    #         self.assertEqual(i.nombre, 'Departamento Francisco De Villagra')

    def setUp(self):
        # nuevo_arrendador = Usuario.objects.create(rut='222222222', nombres='Elizabeth', apellidos='Barre', direccion='Juncal 455, Cerrillo, Santiago', telefono='988888888', email='eli@mail.cl', tipo_user='Arrendador', activo='True', creado_por='Admin')
        # self.assertTrue(nuevo_arrendador)

        nuevo_arrendatario = Usuario.objects.create(rut='111111111', nombres='Juan Pedro', apellidos='Aguilar Silva', direccion='Pandora 3212, Maipu, Santiago', telefono='999999999', email='juan@mail.cl', tipo_user='Arrendatario', activo='True', creado_por='Admin')
        self.assertTrue(nuevo_arrendatario)
        
        nuevo_inmueble = Inmueble.objects.create(nombre='Departamento Francisco De Villagra', descripcion='No amoblado, 1 dormitorio, 1 baño, No Admite mascotas, 1 estacionamiento, Año de construcción: 2015', m2_construidos=28, m2_totales=33, cant_estacionamientos='1', cant_habitaciones='1', cant_banios='1', direccion='Francisco De Villagra', comuna='Ñuñoa', tipo_inmueble='Departamento', precio_mes_arriendo=530000, activo=True, creado_por='Admin')
        self.assertTrue(nuevo_inmueble)
        
#      Revisar
    def test_solicitud_arriendo(self):
        id_arrendatario = Usuario.objects.get(pk='111111111')
        solicitud_inmueble = Inmueble.objects.get(pk='1')#.update(arriendo=id_arrendatario)
#        self.assertTrue(solicitud_inmueble.usuarios.add(id_arrendatario))
        self.assertTrue(solicitud_inmueble.usuario.create(usuario=id_arrendatario))

    # def test_publicar_propiedades(self):
    #     publicar_inmueble = Inmueble.objects.filter(pk='1')
    #     for i in publicar_inmueble:
    #         self.assertTrue(i.nombre)

    # def test_listar_propiedades(self):
    #     inmuebles = Inmueble.objects.all()
    #     for i in inmuebles:
    #         self.assertTrue(i.nombre)

    # def test_update_inmueble(self):
    #     update_inmueble = Inmueble.objects.update(nombre='Departamento Francisco De Villagra', descripcion='No amoblado, 1 dormitorio, 1 baño, No Admite mascotas, 1 estacionamiento, Año de construcción: 2015', m2_construidos=28, m2_totales=33, cant_estacionamientos='1', cant_habitaciones='1', cant_banios='1', direccion='Francisco De Villagra', comuna='Ñuñoa', tipo_inmueble='Departamento', precio_mes_arriendo=530000, activo=True, creado_por='Admin')
    #     self.assertTrue(update_inmueble)

    # def test_eliminar_propiedades(self):
    #     eliminar_inmueble = Inmueble.objects.filter(pk='1')
        
    #     self.assertTrue(eliminar_inmueble.delete())

#     # Revisar
#     def test_aceptar_arrendatario(self):
#         id_usuario_id = Usuario.objects.get(pk='rut')
#         nuevo_user_inmueble = Inmueble.objects.filter(pk=id).update(activo=True)
#         nuevo_user_inmueble.arriendo.add(id_usuario_id)
#         self.assertTrue(nuevo_user_inmueble)


