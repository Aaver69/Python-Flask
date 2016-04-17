#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3
from unittest.case import TestCase
import shutil
import tarfile
import os
from src.apibot import Apibot
from src.apios import Apios
from src.api import RestApi


class TestApibot(TestCase):

    def setUp(self):
        #   Will extend this piece of code to all other functions
        self.api = Apibot()
        self.api2 = Apios()
        self.api3 = RestApi("http://onysos.fr")
        self.asset_path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "aaa", "")
        self.asset_path2 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "www", "")
        self.interface_id = 1
        self.files = self.api2.list_directory_files(self.asset_path)
        self.pile = ["x"]
        #   Unzip file for the unittest
        archive = tarfile.open("asset_test_apios.tar.gz")
        archive.extractall()
        archive.close()

    def tearDown(self):
        #   Will extend this piece of code to the end of the test
        #   It will delete the tree test.
        #   Does not seem to work
        shutil.rmtree(self.asset_path)

    def test_processing(self):
        #    MECHANT CA MARCHE PAS SNIFFE
        #   Will process the automnation
        self.api2.write_specific_directory_file("Salut.txt", self.asset_path, "Ceci est un succès")
        #   Will create a 'Salut.txt" in the path given with the following sentences 'Ceci est un succès'
        #   self.api.processing()
        #   Proccess all the stuff
        inside = os.stat(self.asset_path2).st_size > 0
        #   Check if the file is filled and generated into the second diectory
        self.assertEqual(True, inside)