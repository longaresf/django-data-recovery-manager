from django.db import models
from inmobiliaria_app.models import Usuario, Inmueble, Usuario_Inmueble, Comuna, Provincia, Region, Image

def crear_usuario(rut, nombres, apellidos, direccion, telefono, email, tipo_user, activo, creado_por):
    nuevo_usuario = Usuario.objects.create(rut=rut, nombres=nombres, apellidos=apellidos, direccion=direccion, telefono=telefono, email=email, tipo_user=tipo_user, activo=activo, creado_por=creado_por)
    return nuevo_usuario

def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, cant_estacionamientos, cant_habitaciones, cant_banios, direccion, comuna, tipo_inmueble, precio_mes_arriendo, activo, creado_por):
    nuevo_inmueble = Inmueble.objects.create(nombre=nombre, descripcion=descripcion, m2_construidos=m2_construidos, m2_totales=m2_totales, cant_estacionamientos=cant_estacionamientos, cant_habitaciones=cant_habitaciones, cant_banios=cant_banios, direccion=direccion, comuna=comuna, tipo_inmueble=tipo_inmueble, precio_mes_arriendo=precio_mes_arriendo, activo=activo, creado_por=creado_por)
    return nuevo_inmueble

def add_image_inmueble(id, image):
    inmueble = Inmueble.objects.get(id=id)
    image_add = Image.objects.create(nombre=image, inmueble=inmueble)
    return image_add

def lista_propiedades_comuna(comuna):
    inmuebles = Inmueble.objects.filter(comuna=comuna)
    return inmuebles

def listar_propiedades():
    inmuebles = Inmueble.objects.all()
    return inmuebles

def update_inmueble(id, nombre, descripcion, m2_construidos, m2_totales, cant_estacionamientos, cant_habitaciones, cant_banios, direccion, comuna, tipo_inmueble, precio_mes_arriendo, activo, creado_por):
    update_inmueble = Inmueble.objects.filter(pk=id).update(nombre=nombre, descripcion=descripcion, m2_construidos=m2_construidos, m2_totales=m2_totales, cant_estacionamientos=cant_estacionamientos, cant_habitaciones=cant_habitaciones, cant_banios=cant_banios, direccion=direccion, comuna=comuna, tipo_inmueble=tipo_inmueble, precio_mes_arriendo=precio_mes_arriendo, activo=activo, creado_por=creado_por)
    return update_inmueble

def eliminar_propiedades(inmueble):
    eliminar_inmueble = Inmueble.objects.get(pk=inmueble)
    eliminar_inmueble.delete()
    return eliminar_inmueble

def solicitud_arriendo(rut, inmueble):
    arrendatario = Usuario.objects.get(pk=rut)
    inmueble = Inmueble.objects.get(pk=inmueble)
    Solicitud_arriendo = Usuario_Inmueble.objects.create(arrendatario=arrendatario, inmueble=inmueble, creado_por=arrendatario)
    return Solicitud_arriendo

def listar_estado_propiedades(estado):
        inmueble = Usuario_Inmueble.objects.all().filter(estado=estado)
        print(f'inmueble: {inmueble}')

def eliminar_propiedad_por_aprobacion_arriendo(id):
    eliminar_solicitud_arriendo = Usuario_Inmueble.objects.get(id=id)
    eliminar_solicitud_arriendo.delete()
    return eliminar_solicitud_arriendo

def aceptar_arrendatario(rut, id, estado):
    inmueble = Inmueble.objects.get(id=id)
    arrendatario = Usuario.objects.get(pk=rut)
    try:
        arriendo = Usuario_Inmueble.objects.filter(inmueble=id, arrendatario=rut).get(estado=estado)
        if arriendo.estado == 'Pendiente':
            arriendo = Usuario_Inmueble.objects.filter(inmueble=id, arrendatario=rut).update(estado='Aprobado')
            print('Se ha Aceptado el Arrendatario')
            return arriendo
        elif arriendo.estado == 'Rechazado':
            print('Arriendo fue Rechazado')
        else:
            print('El Arrendatario ya fue Aceptado anteriormente')
    except:
        print(f'Arrendatario no presenta inmueble en estado: {estado}')    

def print_inmueble_comuna():
    inmueble_comuna = Inmueble.objects.values_list('comuna', 'nombre', 'descripcion')
    
    comunas = sorted(set([i[0] for i in inmueble_comuna]))
    for comuna in comunas:
        print(f"Comuna: {comuna}")
        for dato in [j for j in inmueble_comuna if j[0]==comuna]:
            print(f"\tNombre: {dato[1]} \n\tDescripción: {dato[2]}")
            
    f=open("inmueble_comuna.txt","a", encoding="utf-8")
    for i in inmueble_comuna:
        f.write(str(i[0]))
        f.write(',')
        f.write(str(i[1]))
        f.write(',')
        f.write(str(i[2]))
        f.write("\n")
    f.close()

def print_inmueble_region():
    inm_com = Inmueble.objects.values_list('comuna')
    for c in inm_com:
        inmueble_com = Inmueble.objects.get(comuna=c[0])
        inmueble = Inmueble.objects.get(id=inmueble_com.id)
        comuna_nom = Comuna.objects.get(nombre=c[0])
        comuna = Comuna.objects.get(id=comuna_nom.id)
        
        #print(f'Inmueble: {inmueble.nombre}, {comuna.nombre}, {comuna_nom.comuna_provincia.nombre}, {comuna_nom.comuna_provincia.provincia_region.nombre}')
        # comunas print(f'{(str(c[0]))}')
        #print(f'{(str(inmueble.nombre))}')
     
        f=open("inmueble_regiones.txt","a", encoding="utf-8")
        f.write(f'Inmueble: {inmueble.nombre}, {comuna.nombre}, {comuna_nom.comuna_provincia.nombre}, {comuna_nom.comuna_provincia.provincia_region.nombre}')
        f.write("\n")
    f.close()
    
    
    