#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Python 3
"""
modul that contains all API related stuff
"""
import jinja2.ext
import io
import logging
import random
import os

logger = logging.getLogger(__name__)


interfaces = [
    {
        'id': 1,
        'nom': 'od paie',
        'description': 'blabla',
        'fichiers': [
            {
                'nom': 'src',
                'display_nom': "fichier source",
                'type': 'txt',
                'est_sources': True,
                'nom_fichier_telecharge': 'source.pnl'
            },
            {
                'nom': 'dst',
                'display_nom': "fichier generé",
                'type': 'txt',
                'est_sources': False,
                'nom_fichier_telecharge': '{source}.txt'
            }
        ],
        'environnements': [
            {
                'nom': 'code soc',
                'display_nom': 'code societe',
                'type': 'str',
                'valeur_defaults': '123'
            }
        ]
    },
    {
        'id': 2,
        'nom': 'essais',
        'description': 'ceci est un essais ',
        'fichiers': [
        ],
        'environnements': [
            {
                'nom': 'cb',
                'display_nom': 'numero de CB',
                'type': 'str',
                'valeur_defaults': ''
            }
        ]
    }
]


class RestApi(object):
    """
    authenticate the current user in Interface web service and
    manipulate the generation for this client
    """
    def __init__(self, url):
        self.url = url
        asset_path = os.path.join(os.path.dirname(__file__), "..", "asset_running")
        self.configs = [
            {
                "id": 1,
                "nom": "generation du matin",
                "interface": 1,
                'fichiers': {
                    "src": os.path.join(asset_path, "a", "YIPYIP0"),
                    "dst": os.path.join(asset_path, "a", "toto.txt"),
                },
                'environnements': {
                    'code soc': '12345'
                }
            },
            {
                "id": 2,
                "nom": "generation du soir",
                "interface": 1,
                'fichiers': {
                    "src": os.path.join(asset_path, "e", ""),
                    "dst": "/tmp/bsoir.txt",
                },
                'environnements': {
                    'code soc': '12345'
                }
            },
            {
                "id": 3,
                "nom": "essais",
                "interface": 2,
                'fichiers': {


                },
                'environnements': {
                    'cd': '123456789',
                }
            }
        ]



    def list(self):
        """
        Get all the client's config
        """
        return self.configs

    def auth(self, token):
        """
        Authenticate the user via a server token provided by the web service
        :param token: the token given by the web service
        :return: True if the authentication is ok
        """

        pass

    def get(self, interface_id):
        """
        Get the id of the interface the client choosen earlier
        :param interface_id
        """
        for interface in interfaces:
            if interface_id == interface['id']:
                return interface

    def generate(self, interface_id, files, environments):
        """
        Enable the user to launch a generation.
        Args:
            interface_id: id of the interface
            files: files to generate
            environments: folders where the generated files go

        """
        return 1
        #   fake id generation

    def status(self, generation_id):
        """
        Will return the status for a generation_id given
        :param generation_id:  generation_id
        :return:
        """
        if generation_id == 1:
            if random.randint(1, 5) % 2 == 0:
                return True
            else:
                return False
        else:
            raise NotImplementedError()

    def get_files(self, generation_id):
        """
        get the content of the files for the given generation
        :param generation_id: the id of the generation
        :return: the dict containing the data downloaded from the interface api
        we indicate here the 'b' argument to warm that is bytes data
        :rtype: dict[str, stream]
        """
        if generation_id == 1:
            return {"dst": io.BytesIO(b"coucou ceci est un fichier resultat")}
        else:
            raise NotImplementedError()

    def get_config(self, config_id):
        """
        pull the config for the current client from the web service
        :param  config_id : id of the config
        :return config
        """
        for config in self.configs:
            if config_id == config['id']:
                return config

    def set_config(self, config):
        """
        replace the config with the one given
        :param dict config: the config
        :return:
        """
        for i, local_cfg in enumerate(self.configs):
            if config["id"] == local_cfg['id']:
                self.configs[i] = config

    def push_config(self):
        """
        push the current config to the remote endpoint for long term retention
        :return:
        """


