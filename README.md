---------------------------------------------------------------
///////////////////////////////////////////////////////////////

                     InterfaceCli V 0.0.1

///////////////////////////////////////////////////////////////

This program is able to manipulate files and paths
through a Web Friendly User Interface (WFUI) according to
some Configurations and Interfaces.
In the first place, you will see a list of configurations.
They are pre-established in the RestApi.

It's written with Python using Flask Framework and
works on Windows Operating System and any distributions
of Linux Operating System.

You have to intall all the depedences listed
in 'requirement.txt' file for both Operating System.

I encourage you to reffer yourself to the Flask Documentation.
---------------------------------------------------------------

Three API(s) are currently used :
///////////////////////////////////////////////////////////////

                        api.RestApi()

///////////////////////////////////////////////////////////////
To make the program communicates with the WFUI, we use a REST
API which contains all the configurations and interfaces.

///////////////////////////////////////////////////////////////

                        apios.Apios()

///////////////////////////////////////////////////////////////
Apios will care about all manipulations related to files
and paths. Those functions seems a little bit too heavy.

///////////////////////////////////////////////////////////////

                        apibot.Apibot()

///////////////////////////////////////////////////////////////
Apibot is going to attempt to automatize some tasks to perform
like get the files in a directory, take some bytes in these
files, and then write them into a new file in a new directory.

---------------------------------------------------------------
///////////////////////////////////////////////////////////////

                 Configurations in REST API

///////////////////////////////////////////////////////////////
Configurations are divided as a list of dictionnaries like :

[
    {
    Id : id of the configuration,
    Nom : 'name of the configuration',
    Interface : id of the used interface,
    Fichiers : {
    src : 'path to the src directory',
    dst : 'path to the dst directory'}
    }
]
---------------------------------------------------------------
///////////////////////////////////////////////////////////////

                 Interfaces in REST API

///////////////////////////////////////////////////////////////
Interfaces are divied as a liste of dictionnaries like :

[
    {
     id: 1,
     nom: 'name of the interface',
     description: 'Description of the interface',
       fichiers: [
            {
              nom': 'name of the src directory',
              display_nom': "source file name",
              type': 'type of the file (txt)',
              est_sources': Is this a source file (True/False),
              nom_fichier_telecharge': 'name of the downloaded file'
            }
                ]
     }
]
---------------------------------------------------------------
///////////////////////////////////////////////////////////////

                            Unittest

///////////////////////////////////////////////////////////////
This package include a test.py file. It's essentially to
practice my unnittest, but you can improve, fix, it if
you want.
---------------------------------------------------------------
///////////////////////////////////////////////////////////////

                            Views.py

///////////////////////////////////////////////////////////////
It contains all the views related to the WFUI, written
with the Jinja 2 template engine. You can check documentation
on their official website.
---------------------------------------------------------------
///////////////////////////////////////////////////////////////

                            Forms.py

///////////////////////////////////////////////////////////////
Forms.py contains a method which is able to create dynamically
form on a view. With this method, you can create form faster
than ever. You might check the FlaskWTF documentation.
---------------------------------------------------------------
///////////////////////////////////////////////////////////////

                            run.py

///////////////////////////////////////////////////////////////
Enables you to launch the program.
---------------------------------------------------------------
///////////////////////////////////////////////////////////////

                            setup.py

///////////////////////////////////////////////////////////////
Enables you to setup the program.
Use Cx_Freeze Library to port the program on Windows.
Check the doc too.
---------------------------------------------------------------

