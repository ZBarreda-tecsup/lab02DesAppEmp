from django.shortcuts import render
from math import pi

def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html',context)
def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas' : request.POST.getlist('idioma'),
        'correo': request.POST['email'],
        'website' : request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html',context)

def tomar_datos(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/operaciones.html',context)

def operador(request):
    num1 = request.POST['numero1'],
    num2 = request.POST['numero2'],
    ope = request.POST['operacion'],
    ope = ope[0]
    num1 = int(num1[0])
    num2 = int(num2[0])
    
    match ope:
        case 'suma':
            ope = '+'
            resultado = num1 + num2
        case 'resta':
            ope = '-'
            resultado = num1 - num2
        case 'division':
            ope = 'x'
            resultado = num1 * num2
        case 'division':
            ope = '/'
            resultado = num1 / num2
        case _:
            ope = 'Operación no válida'

    context = {
        'titulo': "Respuesta",
        'operacion': ope,
        'valor1': num1,
        'valor2': num2,
        'resultado': resultado,
    }

    return render(request, 'encuesta/resultados.html',context)

def VolumenCilindro(request):
    context = {
        'titulo': "CALCULO DE VOLUMEN DE UN CILINDRO",
    }
    return render(request, 'encuesta/Volumen.html',context)

def calcular(request):
    diametro = request.POST['diametro'],
    altura = request.POST['altura'],
    diametro = float(diametro[0])
    altura = float(altura[0])
    radio = diametro / 2
    volumen = pi * (radio ** 2) * altura

    context = {
        'volumen': volumen,
    }
    return render(request, 'encuesta/calculo.html',context)
