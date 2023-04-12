# Tercera-pre-entrega-RosasSandillu
Tercera pre entrega del curso de python en Coderhouse

Instrucciones

Para probar el código, seguí los siguientes pasos:

    Clona este repositorio en tu máquina local.
    Abrí una terminal y navega hasta la raíz del proyecto.
    Crea un entorno virtual en la raíz del proyecto: python -m venv env.
    Activa el entorno virtual:
        En Windows: env\Scripts\activate.
        En Linux/Mac: source env/bin/activate.
    Instala las dependencias del proyecto: pip install -r requirements.txt.
    En la terminal, navega hasta la carpeta del proyecto con cd App3raEntrega.
    Ejecuta las migraciones de Django con el comando: python manage.py migrate.
    Ejecuta el servidor con el comando: python manage.py runserver.
    Abre un navegador y navega hasta http://127.0.0.1:8000/ para ver la página principal.
    Para acceder a la lista de libros, accede a http://127.0.0.1:8000/books/.
    Para acceder a la lista de películas, accede a http://127.0.0.1:8000/movies/.
    Para acceder a la lista de música, accede a http://127.0.0.1:8000/music/.
    Para crear un nuevo libro, accede a http://127.0.0.1:8000/books/create/.
    Para crear una nueva película, accede a http://127.0.0.1:8000/movies/create/.
    Para crear una nueva canción, accede a http://127.0.0.1:8000/music/create/.

Descripción del código

Este código es una aplicación de Django que permite listar y crear libros, películas y canciones. Para ello, cuenta con tres modelos: Libro, Pelicula y Musica. Cada uno de ellos cuenta con los campos titulo, autor/director y descripcion.

La aplicación cuenta con tres vistas basadas en clases para listar los libros, películas y canciones: BookListView, MovieListView y MusicListView, respectivamente. Además, cuenta con tres vistas basadas en funciones para crear nuevos libros, películas y canciones: book_create, movie_create y music_create.

Los formularios utilizados para la creación de libros, películas y canciones son LibroForm, PeliculaForm y MusicaForm, respectivamente. Estos formularios permiten crear instancias de los modelos mencionados anteriormente.
