========================
    Recurso Usuarios
========================

Recurso LOGIN
-------------

    .. http:post:: /api/users/login/

    Inicia sesión con credenciales de usuario

    * **Campos olbigatorios**

        :username: **(string)** Nombre de usuario
        :password: **(string)** Contraseña del usuario

    * **Ejemplo de petición**

        .. host:: http

            POST /api/users/login/
            Content-Type: json

            {
                "username": "usuariosprueba",
                "password": "usuariosprueba"
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "user": {
                        "username": "usuariosabado3",
                        "last_login": "2021-09-18",
                        "email": "usuariosabado3@sabado.com",
                        "fecha_registro": "2021-09-18",
                        "fecha_nacimiento": "2005-01-31",
                        "institucion_educativa": null,
                        "idiomas": [],
                        "ubicacion": null,
                        "facebookurl": null,
                        "twitterurl": null,
                        "youtubeurl": null,
                        "adulto": false,
                        "foto_perfil": null
                },
                "access_token": "3076c51dad376c39984fef4e9ce9a8167e26c6f4"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "non_field_errors": [
                    "Credenciales incorrectas"
                ]
            }

Recurso SIGNUP
-------------

    .. http:post:: /api/users/signup/

    Realiza el registro de un usuario, sólo pueden ser adultos tras iniciar sesión

    * **Campos olbigatorios**

        :username: **(string)** Nombre de usuario
        :password: **(string)** Contraseña del usuario
        :password_confirmation: **(string)** Verificación de la contraseña del usuario
        :fecha_nacimiento: **(date)** Fecha de nacimiento del usuario en formato yyyy-mm-dd
        :email: **(email)** Correo del usuario en formato usuario@organizacion.tipo

    * **Ejemplo de petición**

        .. host:: http

            POST /api/users/signup/
            Content-Type: json

            {
                "username": "usuarioreal",
                "password": "contraseñausuarioreal",
                "password_confirmation": "contraseñausuarioreal",
                "fecha_nacimiento": "2000-01-22",
                "email": "usuarioreal@realidad.com"
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "username": "usuarioreal",
                "last_login": null,
                "email": "usuarioreal@realidad.com",
                "fecha_registro": "2021-09-18",
                "fecha_nacimiento": "2000-01-22",
                "institucion_educativa": null,
                "idiomas": null,
                "ubicacion": null,
                "facebookurl": null,
                "twitterurl": null,
                "youtubeurl": null,
                "adulto": false,
                "foto_perfil": null
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "username": [
                    "Este campo debe ser único."
                ],
                "email": [
                    "Este campo debe ser único."
                ]
            }  

Recurso WATCH
-------------

    .. http:get:: /api/users/watch/?username=<username>

    Ve la información de un usuario

    * **Campos olbigatorios**

        :username: **(string)** Nombre de usuario a consultar

    * **Ejemplo de petición**

        .. host:: http

            GET /api/users/watch/?username=usuarioreal
            Content-Type: None
            Parameters: username=usuarioreal

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "username": "usuarioreal",
                "last_login": "2021-09-18",
                "email": "usuarioreal@realidad.com",
                "fecha_registro": "2021-09-18",
                "fecha_nacimiento": "2000-01-22",
                "institucion_educativa": null,
                "idiomas": null,
                "ubicacion": null,
                "facebookurl": null,
                "twitterurl": null,
                "youtubeurl": null,
                "adulto": true,
                "foto_perfil": null
            }

            HTTP/1.1 301 REDIRECT
            HTTP/1.1 200 OK
            Content-Type: json

            {
                "username": "usuarioreal",
                "last_login": "2021-09-18",
                "email": "usuarioreal@realidad.com",
                "fecha_registro": "2021-09-18",
                "fecha_nacimiento": "2000-01-22",
                "institucion_educativa": null,
                "idiomas": null,
                "ubicacion": null,
                "facebookurl": null,
                "twitterurl": null,
                "youtubeurl": null,
                "adulto": true,
                "foto_perfil": null
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "Error": "Username inválido"
            }    

:status 200: Petición completada
:status 201: Usuario o token creado
:status 301: Redirigido debido a una solicitud de watch con una URL mal escrita
:status 400: Valores inválidos