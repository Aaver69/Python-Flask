#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3
import logging
import sys
from traceback import print_exc
import os
import glob
import jinja2.ext
logging.getLogger(__name__)


class Apios(object):

    def __init__(self):

        pass

    def check_files_in_directory(self, path):
        """
        will check if there are files in the input directory
        :param unicode path : src path to the files
        :return:
        """
        if os.path.exists(path):
            return os.path.isfile(path)

    def list_directory_files(self, path):
        """
        List all src files for a specific config
        :param path path: path to the src files
        :return: list of src files
        """
        if not os.path.exists(path):
            try:
                return None
            except IOError:
                print_exc()
        else:
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            return files

    def read_all_files_directory(self, path):
        """
        read files form src directory
        :param unicode path : path to the src files to read
        /!\ take '*'
        :return: None
        """
        check = Apios.check_files_in_directory(self, path)
        if check:
            src = path + "*"
            files = glob.iglob(src)
            for name in files:
                try:
                    with open(name) as f:
                        sys.stdout.write(f.read())
                except IOError:
                    print_exc()

    def open_all_src_files(self, config, interface):
        """
        Will open all the src files
        all_src_files contains a file name, and a file meta, all present in each file of interface
        we create an empty dictonnary named res for resultat whichs will take the values of the path's src name
        and finally we open all the file available in the directory
        :param config: config given
        :param interface : interface given
        :return: dict of stream
        """
        try:
            all_src_files = [file_name for file_name, file_meta in interface['fichiers'].items() if file_meta["est_sources"]]
            res = {}
            for src_name in all_src_files:
                path_to_file = config["fichiers"][src_name]
                res[src_name] = open(path_to_file, "r")
            return res
        except TypeError:
            pass

    def read_specific_file_directory(self, path,  name):
        """
        read a specific file in the src directory
        :param path : path of the file to read
        :param  unicode name: name of the file to read
        :return: None
        """
        check = Apios.check_files_in_directory(self, path)
        if check:
            src = path + name
            files = glob.iglob(src)
            for file in files:
                try:
                    with open(file) as f:
                        sys.stdout.write(f.read())
                except IOError:
                    print_exc()

    def write_specific_directory_file(self, name, path, sentences):
        """
        will write to a specific src file
        :param unicode sentences : sentences to write
        :param path path : path to the file to write
        :param unicode name: name of the src file
        :return:
        """
        src = path
        if not os.path.exists(src):
            os.makedirs(src)
            glob.iglob(src)
            with open(src + name, "w") as f:
                f.write(sentences)
        else:
            glob.iglob(src)
            with open(src + name, "w") as f:
                f.write(sentences)

    def write_through_all_directory(self, counter, name, path, sentences):
        """
        will write through a directory an amount of files
        :param counter: amount of files to write
        :param name: name of the files to write
        :param path: path where the files are gonna be wrote
        :param sentences: the content of the files
        :return:
        """
        x = 0
        src = path
        glob.iglob(src)
        while x != counter:
            with open(src + name + "{0}".format(x), "w") as f:
                f.write(sentences)
                x += 1

    def create_directory(self, name, path):
        """
        Will check if there is a directory, if there is not, it will create one
        :param unicode name: name of the directory to create
        :param path path: path were the directory have to be created
        :return:
        """
        src = path
        name = name
        if not os.path.exists(src + name):
            os.makedirs(src + name)

    def create_directory_with_file_in(self, name, path, namef, sentences):
        """
        This function will create a directory and write a file in int
        :param unicode name: name of the directory to create
        :param path path: path where the directory has to be create
        :param unicode namef: name of the file to write
        :param unicode sentences: what the file contains
        :return:
        """
        src = path
        name = name
        namef = namef
        sentences = sentences
        self.create_directory(name, src)
        self.write_specific_directory_file(namef, src, sentences)

    def create_multiple_directories(self, counter, name, path):
        """
        This function will create n directory in a path.
        :param int counter: amount of directory to create
        :param unicode name: name of the directory to create
        :param path path: path where the directory have to be created
        :return:
        """
        counter = counter
        name = name
        src = path
        x = 0
        while x != counter:
            if not os.path.exists(src + name):
                os.makedirs(src + name + "{0}".format(x))
                x += 1

    def write_files_into_two_directories_at_different_locations(self, counter,  namef, path1, named1, named2, path2, sentences):
        """
        This function will write files into two directory from different locations
        :param int counter: amount of files to write
        :param unicode namef: name of the files to write
        :param path path1: path to the first location
        :param unicode named1: name of the first directory's location
        :param unicode named2: name of the second directory's location
        :param path path2: path to the second location
        :param unicode sentences: what the files will contain
        :return:
        """
        counter = counter
        namef = namef
        src1 = path1
        src2 = path2
        named1 = named1
        named2 = named2
        sentences = sentences
        x = 0
        while x != counter:
            self.create_directory(named1, src1)
            self.create_directory(named2, src2)
            self.write_through_all_directory(counter, namef, src1, sentences)
            self.write_through_all_directory(counter, namef, src2, sentences)
            x += 1

    def create_multiple_directoy_at_two_different_locations(self, counter, name, name2, path1, path2):
        """
        This function will create n directory at two different locations
        :param int counter: amount of directory to create
        :param unicode name: name of the first directory
        :param unicode name2: name of the second directory
        :param path path1: path to the first location
        :param path path2: path to the second location
        :return:
        """
        counter = counter
        name = name
        name2 = name2
        src = path1
        src2 = path2
        x = 0
        while x != counter:
            if not os.path.exists(src + name) and not os.path.exists(src2 + name2):
                os.makedirs(src + name + "{0}".format(x))
                os.makedirs(src2 + name2 + "{0}".format(x))
                x += 1


















