

# Polipox

![](https://github.com/orzaez/PolipoX/blob/master/images/GIF_Polipox.gif)

## Descripción

Polipox es un proyecto desarrollado para el área digestiva del Hospital Reina Sofía de Córdoba. Surge de la necesidad de facilitar el registro de las características de los pólipos durante las colonoscopias, una tarea que resultaba difícil para los clínicos.

El proyecto consiste en un dispositivo que permite realizar un registro en tiempo real de los pólipos encontrados durante la exploración mediante comandos de voz. Además, se incluye una plataforma web donde estos registros quedan almacenados para su posterior visualización y consulta.

## Características

- **Registro de Pólipos en Tiempo Real**: El dispositivo permite al clínico registrar los pólipos encontrados durante la colonoscopia de forma inmediata y precisa mediante comandos de voz.

- **Plataforma Web**: Los registros de los pólipos se almacenan en una plataforma web accesible desde cualquier dispositivo con conexión a Internet. Esto facilita la visualización y consulta de los datos recopilados durante las exploraciones.

- **Interfaz Intuitiva**: Tanto el dispositivo como la plataforma web cuentan con interfaces diseñadas para ser intuitivas y de fácil uso, lo que facilita su adopción por parte del personal médico.

## Instalación y Uso

### Requisitos

- Python 3
- FasterWhisper

## Descripción Técnica

A continuación explicaremos el lado técnico de PolipoX, centrándonos en el hardware, software y arquitectura que compone nuestro sistema.

### Hardware

Para el hardware nos hemos decantado por una Raspberry Pi 5 con 4 GB de RAM para ser capaz de soportar el motor de UI y el servidor VNC.

### Software

Nuestro sistema se compone de dos subsistemas complementarios:

- **Asistente Virtual**: Cuenta con una UI que puede ser accedida desde cualquier dispositivo mediante el protocolo VNC para ayudar al clínico a interactuar con el asistente de voz.
- **Plataforma Web**: Permite al clínico visualizar la información de las distintas exploraciones y los pólipos encontrados en cada una de ellas.

### Arquitectura

La arquitectura de PolipoX funciona de la siguiente manera:

- **Asistente de Voz**: Se conecta mediante peticiones HTTP a un servidor desplegado en EC2 que ejecuta el modelo Faster Whisper de OpenAI, un modelo de reconocimiento de voz open source.
- **Plataforma Web**: Realiza peticiones POST a nuestro servidor web desplegado en Vercel, el cual está conectado a nuestra base de datos PostgreSQL para almacenar la información de los pólipos.
- **Base de Datos**: Utilizamos una base de datos PostgreSQL, la misma que utiliza nuestra aplicación web para visualizar la información.


### Futuras Mejoras

Se planean las siguientes mejoras para el proyecto:

- **Capturar y Transmitir Video en Tiempo Real a la Plataforma Web**: Permitirá a los médicos visualizar la colonoscopia en tiempo real.
- **Volcar Diagnóstico Revisado por el Clínico a la Base de Datos Diraya**: Integrar el diagnóstico del médico en la plataforma para un acceso más completo al historial del paciente.



1. Clona este repositorio:
2. Creación y activación de un entorno vistual
python3 -m venv venv (buscar en google como crear venv con python)
source ./venv/bin/activate
3. Instalacion de los requisitos
python3 -m pip install -f ./requirements.txt
