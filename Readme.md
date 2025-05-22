##Intranet para la Confederación Hidrográfica

###Introducción

El objetivo de esta intranet es permitir la gestión de la información de una Confederación Hidrográfica. Contiene información sobre estaciones y señales pudiendo mostrarla en gráficos y tablas así como en un mapa interactivo. Contiene además una aplicacación para la visualización de datos de predicciones de caudal, un gestor que permite administrar la base de datos de Señales y Estaciones Remotas y un gestor de usuarios.

###Características

- Gestión de usuarios
- Gestión de estaciones y señales
- Visualización de datos en gráficos y tablas
- Visualización de datos en un mapa interactivo
- Visualización de predicciones de caudal
- Gestión de la base de datos de Señales y Estaciones Remotas
- Gestión de la base de datos de predicciones de caudal

###Desarrollo

La Intranet se ha desarrollado con Django 5.2 y Python 3.12. para el backend y Vanila Javascript para el frontend.

La aplicación main_app es la app principal que controla la lógica del backend de la intranet.

La aplicación gestor contiene la lógica de las páginas de admin que gestionan la BB.DD del gestor, a partir de la cual actualizan las demás bases de datos

La aplicación vsad contiene la lógica de las páginas de predicciones de caudal.

La aplicación vsad_test es una palicación Python que gestiona la base de datos de predicción de caudal a partir de archivos XML generados por un modelo.

El archivo main_app/views.py contiene la lógica de las páginas principales de la intranet, mientras que el archivo main_app/requests.py contiene requests en JSON para la comunicación asíncrona del frontend con el backend.
