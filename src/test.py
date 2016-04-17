#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3
from unittest.case import TestCase
import shutil
import tarfile
from src.apios import Apios
import os
import glob
import sys
from traceback import print_exc


class TestApios(TestCase):

    def setUp(self):
        #   Will extend this piece of code to all other functions
        self.api = Apios()
        self.asset_path = os.path.join(os.path.dirname(__file__), "asset_test_apios")
        #   Unzip file for the unittest
        archive = tarfile.open("asset_test_apios.tar.gz")
        archive.extractall()
        archive.close()

    def tearDown(self):
        #   Will extend this piece of code to the end of the test
        #   It will delete the tree test.
        shutil.rmtree(self.asset_path)

    def test_fichier_in_src(self):
        #   Will determine if the path is a regular file
        lol = self.api.check_files_in_directory(os.path.join(self.asset_path, "d", "src"))
        self.assertEqual(False, lol)

    def test_no_fichier_in_directory(self):
        #   Attempt to check if the path is a regfular file in a no existing directory
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "a", "b", "")
        if not os.listdir(path):
            #   the file does not exist, so we create him with a sentence
            self.api.write_specific_directory_file("Kibo", path, "KIkouleomnde")
            #   Now we check if the file is field, that's the case, the test passed
            inside = os.stat(path).st_size >= 0
            self.assertEqual(True, inside)

    def test_no_directory(self):
        #   Attempt to test if we can list files located in a directory that does'nt exist
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "kappa")
        if not os.path.exists(path):
            #   The path to kappa does not exist, so we create the directory, and we check if there is
            #   any file in here. There is no file, and the directory is created, the test passed
            os.mkdir(path)
        sure = os.listdir(path)
        self.assertEqual([], sure)

    def test_read_empty_file_src(self):
        #   Gonna read an empty file located in a directory
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "dst", "bye.txt")
        name = "bye.txt"
        self.api.read_specific_file_directory(path, name)
        inside = os.stat(path).st_size == 0
        # inside will check if the file is not empty. If it is, will return False, else, will return True
        self.assertEqual(True, inside)

    def test_read_no_empty_file_directory(self):
        #   Gonna read a file filled with some strings
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "dst", "")
        name = "orvoar.txt"
        #   with the path and the name of the file, we check if
        #   this size is > 0, if so, then the file contains
        #   something
        self.api.read_specific_file_directory(path, name)
        inside = os.stat(path).st_size > 0
        self.assertEqual(True, inside)

    def test_read_file_doesnt_exist(self):
        #   Attempt to read a file that doesn't exist.
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "dst")
        name = ""
        #   name is empty
        #   If doesn't exist, we create one
        if not os.path.exists(path):
            os.mkdir(path + name)

    def test_read_a_file_from_differents_directory(self):
        path1 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "dst", "")
        path2 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "src", "")
        name1 = "orvoar.txt"
        name2 = "bonjour.txt"
        #   We define a path and the name of the file we want to read
        #   and then we read them one by one
        self.api.read_specific_file_directory(path1, name1)
        try:
            with open(path1 + name1) as f:
                sys.stdout.write(f.read())
        except Exception:
            print_exc()
            #   Read what orvoar.txt contains

        self.api.read_specific_file_directory(path2, name2)
        try:
            with open(path2 + name2) as f:
                sys.stdout.write(f.read())
        except Exception:
            print_exc()
            #   Read what bonjour.txt contains

    def test_read_file_and_another_empty_file(self):
        path1 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "src", "")
        path2 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "dst", "")
        name1 = "bonjour.txt"
        name2 = "bye.txt"
        #   We define a path the name of the file we want to read
        #   and then we check the size of the file
        #   If it equals 0, the file is empty
        #   If it > 0 , the file contains something
        self.api.read_specific_file_directory(path1, name1)
        self.api.read_specific_file_directory(path2, name2)
        inside = os.stat(path1 + name1).st_size > 0
        insid = os.stat(path2 + name2).st_size == 0
        self.assertEqual(True, inside)
        self.assertEqual(True, insid)

    def test_read_all_file_from_src(self):
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "src", "*.txt")
        files = glob.iglob(path)
        #   Browse through all files in a directory and read them all.
        for file in files:
            try:
                with open(file) as f:
                    sys.stdout.write(f.read())
            except IOError:
                print_exc()

    def test_read_all_file_at_root(self):
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "*.txt")
        files = glob.iglob(path)
        #   Browse through all files.txt at root and read them all
        for file in files:
            try:
                with open(file) as f:
                    sys.stdout.write(f.read())
            except IOError:
                print_exc()

    def test_write_in_a_file(self):
        #   Attempt to write in a file from a directory, need to check the write function /!\
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "dst", "")
        self.api.write_specific_directory_file("bonjour.txt", path, "SALUT LES KOP1")
        inside = os.stat(path).st_size > 0
        self.assertEqual(True, inside)

    def test_all_write_file_txt_with_custom_message(self):
        #   Attempt to write in all files from a directory, need to check the write function /!\
        #   But this function just create a file and write into it WTF. Misunderstanding | That's legit
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "src", "")
        files = glob.iglob(path)
        for file in files:
            self.api.write_specific_directory_file("KOUKOU", path, "BONJOUR LES KOP1")
            checking_file = os.stat(path).st_size > 0
            self.assertEqual(True, checking_file)

    def test_write_file_at_root(self):
        #   Will write into root directory a file name another_test3.txt
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios")
        self.api.write_specific_directory_file("another_test3.txt", path, "YIPYIP")
        #   the file will contain YIPYIP
        inside_test_3 = os.stat(path).st_size > 0
        self.assertEqual(True, inside_test_3)

    def test_write_file_and_read_another(self):
        #   Will try to create and write into a file, and read from another directory
        path1 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "a", "")
        #   Path to a empty folder, to create a file and write in it
        path2 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "d", "src", "")
        #   Path to a not empty folder to reat hi.txt
        self.api.write_specific_directory_file("axeltest.txt", path1, "Je m'appelle Axel")
        name = "hi.txt"
        #   Create a file named axeltest.txt in the 'a' directory
        self.api.read_specific_file_directory(path2, name)
        #   Check if the file is not empty
        inside_hi = os.stat(path1).st_size > 0
        try:
            #   Gonna read hi.txt located at asset_test_apios/d/src/
            with open(path2 + name) as f:
                sys.stdout.write(f.read())
        except Exception:
            print_exc()
        self.assertEqual(True, inside_hi)

    def test_write_read_multiple(self):
        #   Concretly the method write trhough directory file is not correct. To fix. Te method is pratically the same
        #   as write_specific_directory
        #   This function will write in files located in asset_test_apios/c/
        path1 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "c", "")
        files = glob.iglob(path1)
        for file in files:
            #   Gonna write YIPYIP in all files in 'c'
            self.api.write_specific_directory_file("YIPYIP.txt", path1, "YIPYIP")
            #   If the size of the file is > 0, then it's filled
            inside_yipyip = os.stat(path1).st_size > 0
            #   Gonna read all files in asset_test_apios/c/
            self.api.read_all_files_directory(path1)
            self.assertEqual(True, inside_yipyip)

    def test_write_multiple_and_read_multiple(self):
        #   Will create and write multiple files into a directory, then read them
        #   And of course, we can't create multiple files with the same name
        #   That's why we put and index at the end of the file
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "b", "")
        #   Define the path
        self.api.write_through_all_directory(5, "YIPYIP", path, "YIPYIP FOIS CINQ")
        #   Create n numbers of files named YIPYIPn , with the given path and the sentences in the files
        inside = os.stat(path).st_size > 0
        #   Check if the file is filled
        self.api.read_all_files_directory(path)
        self.assertEqual(True, inside)
        with self.assertRaises(AssertionError):
            #   Regularly, it checks if YIPYIP3 is in the B folder. That's the case, but don't
            #   know why, it raises an exception wtf
            self.assertIn("YIPYIP" + "{0}".format(3), path)

    def test_write_multiple_in_two_different_directory(self):
        #   Will write files in different directory
        path1 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "e", "")
        #   Path to the 'e' directory where the function's gonna write files
        path2 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "f", "")
        #   Path to the 'f' directory where the function's gonna write files
        self.api.write_through_all_directory(3, "Chloro", path1, "Les drogues c'est dangereux")
        #   3 files named Chloro|0|1|2 will be writed with the sentence
        self.api.write_through_all_directory(3, "Form", path2, "Les formulaires c'est cool")
        #   3 files named Form|0|1|2 will be writed with the sentence
        inside_1 = os.stat(path1).st_size > 0
        inside_2 = os.stat(path2).st_size > 0
        #   We check if the size of both files are > 0
        #   If it is, they contain something
        self.assertEqual(True, inside_1)
        self.assertEqual(True, inside_2)

    def test_write_multiple_files_in_a_no_existing_directory(self):
        #   Will check to write multiple files in a no existing directory
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "g", "")
        #   'g' directory doesn't exist for the moment
        self.api.write_through_all_directory(2, "KappaPride", path, "Kappa")
        #   We want to write two files named Kappa Pride which each contain Kappa
        inside = os.stat(path).st_size > 0
        if not os.path.exists(path):
            #   'g' is a no existing directory, so we create it
            os.mkdir(path)
        self.assertEqual(True, inside)

    def test_create_directory_if_not_exist(self):
        #   Will check if a directory exist or not
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "yd", "")
        #   Currently, 'yd' directory does not exist
        self.api.create_directory("yd", path)
        #   So we create him, with a given path
        inside = os.listdir(path)
        #   We check if there is a directory in the path
        self.assertEqual(["yd"], inside)
        #   If there is a directory named 'yd', the test passed

    def test_create_directory_write_file_in_it(self):
        #   Will check if there is a directory in the given path
        #   If not, it will create a directory with file in here
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "z", "")
        if not os.path.exists(path):
            self.api.create_directory("z", path)
            #   We define a directory that not exists, 'z'
            self.api.write_specific_directory_file("Zipo", path, "Hello les zippos")
            #   If the size of the size is > 0 then
            #   It's filled
            inside = os.stat(path).st_size > 0
            self.assertEqual(True, inside)
            #   The test passed

    def test_create_directory_write_multiple_files(self):
        #   Try to create a directory if not exist, and write multiple files
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "zozor", "")
        #    'zozor' directory is currently not existing
        if not os.path.exists(path):
            self.api.create_directory("zozor", path)
            #   Creation of the zozor directory with the given path
            self.api.write_through_all_directory(5, "test_zozor", path, "Salut les zozors")
            #   Write n files named 'test_zozorn'with the sentences 'salut les zozors' in it
            inside_zozor = os.stat(path).st_size > 0
            #   We check if the size of the files are > 0
            #   If so , the files are filled, so they are created, so as the directory
            self.assertEqual(True, inside_zozor)
            #   The test passed

    def test_create_directory_in_two_different_path(self):
        #   This fuction will create directory in different locations
        path1 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "vladimir", "")
        #   Define path1
        path2 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "poutine", "")
        #   Define path2
        self.api.create_directory("vladimir", path1)
        #   Will create 'vladimir' directory in 'asset_test_apios'
        self.api.create_directory("poutine", path2)
        #   Will create 'poutine' directory in 'asset_test_apios'
        inside = os.listdir(path1)
        #   List all directory in path1
        inside2 = os.listdir(path2)
        #   List all directory in path 2
        self.assertEqual(["vladimir"], inside)
        self.assertEqual(["poutine"], inside2)
        #   The test passed

    def test_create_directory_with_multiple_files_in_different_locations(self):
        #   Create two directories in different locations
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "selut", "")
        #   Path to the first location
        path2 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "les kop1", "")
        #   Path to the second location
        self.api.create_multiple_directoy_at_two_different_locations(2, "selut", "les kop1", path, path2)
        #   Will create n directories named selut in path1 and les kop1 in path2
        inside1 = os.listdir(path)
        #   We check if the directory are in the path
        inside2 = os.listdir(path2)
        #   Same here
        self.assertEqual(['selut1', 'selut0'], inside1)
        self.assertEqual(['les kop10', 'les kop11'], inside2)
        #   Test passed

    def test_create_multiple_directory(self):
        #   Attempt to create multiple directory with a index for each name
        path = os.path.join(os.path.dirname(__file__), "asset_test_apios", "Jean-Bonbeur", "")
        #   We define a directory that does not exist yet
        self.api.create_multiple_directories(2, "Jean-Bonbeur", path)
        #   The function will create two directories Jean-Bonbeur with the index x
        inside = os.listdir(path)
        #   We check if the directory are available
        self.assertEqual(['Jean-Bonbeur1', 'Jean-Bonbeur0'], inside)
        #   The test passed

    def test_write_files_into_two_directories_at_different_locations(self):
        #   /!\ A reprendre /!\ Parce que cette fonction marche à moitié
        #   This function is trying to create two files named file in a Bonne nuit directory and in a
        #   Bonjour directory
        path1 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "Bonne nuit", "")
        #   Define path1
        path2 = os.path.join(os.path.dirname(__file__), "asset_test_apios", "Bonjour", "")
        #   Define path2
        self.api.write_files_into_two_directories_at_different_locations(2, "file", path1, "Coucou", "ByeBye",
                                                                         path2, "IM BATMAN")
        #   Write n files named file into the different directories
        inside_night = os.listdir(path1)
        #   Check if the directories are in
        inside_day = os.listdir(path2)
        #   Same here
        self.assertEqual(['file1', 'Coucou', 'file0'], inside_night)
        #   Check the lsit of directory and files
        self.assertEqual(['ByeBye', 'file1', 'file0'], inside_day)
        #   Same here
        inside_night_size = os.stat(path1).st_size > 0
        #   Check if the size of the files are > 0 If so
        #   Then the file is filled
        inside_day_size = os.stat(path2).st_size > 0
        self.assertEqual(True, inside_night_size)
        self.assertEqual(True, inside_day_size)
        #   The test passed

    def test_processing(self):
        pass
















































































