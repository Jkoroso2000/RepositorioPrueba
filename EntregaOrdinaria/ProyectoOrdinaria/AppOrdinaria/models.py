from django.db import models

class ProveedorBD(models.Model) :
    nombreEmpresaProveedor = models.CharField(max_length=40)
    telefonoProveedor = models.IntegerField()

class EmpleadoBD(models.Model) :
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefonoEmpleado = models.IntegerField()

class EquipoBD(models.Model) :
    numeroSerie = models.CharField(max_length=40, primary_key=True)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    fechaAdquisicion = models.DateField()
    fechaPuestaMarcha = models.DateField()
    ubicacion = models.CharField(max_length=40)
    empresaProveedor = models.ForeignKey(ProveedorBD, on_delete=models.CASCADE)

class TicketBD(models.Model) :
    referenciaTicket = models.IntegerField(primary_key=True)
    nSerieEquipo = models.ForeignKey(EquipoBD, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=500)
    fechaCreacion = models.DateTimeField()
    fechaVencimiento = models.DateTimeField()
    prioridad = models.CharField(max_length=20)
    estado = models.CharField(max_length=10)
    empleadoResponsable = models.ForeignKey(EmpleadoBD, on_delete=models.CASCADE)
    comentarioAbrir = models.TextField(max_length=1000)
    comentarioCerrar = models.TextField(max_length=1000)
