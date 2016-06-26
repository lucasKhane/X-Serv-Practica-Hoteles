# X-Serv-Practica-Hoteles
Repositorio para la práctica final de SARO/SAT. Curso 2015-2016 

1.-Nombre y titulacion: Daniel Rodriguez Cabello - Grado en Tecnologías de la telecomunicación
2.-Nombre de su cuenta en el laboratorio del alumno: drodca
3.-Nombre de usuario en GitHub: lucaskhane
4.-Resumen de las peculiaridades que se quieran mencionar sobre lo implementado en la parte obligatoria.
Cuando la base de datos está vacia y no hay nadie registrado aun, si alguien se loguea en su pagina de usuario dispone de un boton para poder recargar los hoteles en la base de datos (funciona, no darle que va lentote)
Todo está cuidado con excepciones, para que la pagina no se cuelgue o aparezcan errores al acceder a algun registro de la base de datos que no existe
Hasta que no te logueas, hay cosas que no puedes ver y hay funcionalidades que no puedes acceder, como la pestaña que te redirige a tu pagina de usuario y algunos formularios por ejemplo
El Css parece sencillo, pero no lo es tanto...en realidad, en general le he dedicado tiempo a dejarlo bien
Para el cambio del css requerido por el usuario, he aniadido mas opciones, cambiar bordes y el color de los bordes
Los botones del menu de la cabecera y los botones de la autentificacion tienen la propiedad hover en el css
5.-Lista de funcionalidades opcionales que se hayan implementado, y breve descripcion de cada una.
Algunas serán más interesantes  que otras, pero pongo todo lo que me parece relevante que he hecho de más y que podía no haber hecho.
En la parte inferior de la página, he utilizado Bootstrap para poner un footer que este fijo en el borde inferior de la página. Para que no quede enterrado si hay mucha información o no se quede colgado en la mitad de la página si hay poca.
El registro, logueo y deslogueo de los usuarios es dinamico.
Para ello he utilizado algunas de las plantillas que venian con Django y otras que he aniadido yo.
He utilizado el carrusel de bootstrap para mostrar las fotos de los hoteles (no se si esto cuenta como opcional)
He usado un plugin de bootstrap de seleccion multiple en formularios para dejar mucho mejor los formularios cuando el usuario pida cambiar el css
He usado scripts de javascript y jquery en alguna ocasion dentro de los htmls
Para acceder a la información de los liks de XML he usado un glypicon anexado al footer
6.-URL del video demostracion de la funcionalidad basica:
https://youtu.be/fDBhQy-y_Qg
7.-URL del video demostracion de la funcionalidad optativa, si se ha realizado funcionalidad optativa
https://youtu.be/Ogkme2RRVYg
