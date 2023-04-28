Pagina web de Rosas Sandillú, Julián para el curso de Python de Coderhouse

Las funcionalidades de la página y la forma de actuar es la siguiente:

Clona este repositorio en tu máquina local.
Abrí una terminal y navega hasta la raíz del proyecto
Activa el entorno virtual:
    En Windows: .\TerceraPreEntregaRS\Scripts\activate.
    En Linux/Mac: source ./TerceraPreEntregaRS/bin/activate.
Instala las dependencias del proyecto: pip install -r requirements.txt.
En la terminal, navega hasta la carpeta del proyecto con cd App3raEntrega.
Ejecuta las migraciones de Django con el comando: python manage.py migrate.
Ejecuta el servidor con el comando: python manage.py runserver.
Abre un navegador y navega hasta http://127.0.0.1:8000/Appdjango/ para ver la página principal.
Para acceder a la vista de los libros de Julián y la lista total de libros en la db, hace click en la navbar en "Libros" o accede a http://127.0.0.1:8000/libros.
Para acceder a la vista de las películas de Julián y la lista total de peliculas en la db, hace click en la navbar en "Películas" o accede a http://127.0.0.1:8000/peliculas.
Para acceder a la vista de la música de Julián y la lista total de música en la db, hace click en la navbar en "Música" o accede a http://127.0.0.1:8000/musica.
Para agregar un nuevo libro, hace click en "Agregar" en el de "Agrega tus libros" o accede al formulario en http://127.0.0.1:8000/agregar-libro.
Para agregar una nueva película, hace click en "Agregar" en el de "Agrega tus películas" o accede al formulario en http://127.0.0.1:8000/agregar-peli.
Para agregar una nueva música, hace click en "Agregar" en el de "Agrega tu música" o accede al formulario en http://127.0.0.1:8000/music/agregar-musica.
Para buscar peliculas por género entre todas las que hay guardadas, hace click en la navbar en "Búsqueda de Género de películas" o accede al formulario en http://127.0.0.1:8000/busq-gen.
Para acceder al administrador de la página, dirigirse a http://127.0.0.1:8000/admin y tipear el usuario: "julian" y la contraseña "julinob74".

Esas son todas las funcionalidades de la página web con 3 models distintos, formularios para cada uno y formulario de busqueda que consiste en poder visualizar los libros, películas y la música que uno quiere guardar para tener organizado.
