#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3
import time
import io
import jinja2.ext
from shutil import copyfile


class Apibot(object):
    def __init__(self, api, apios):
        """
        Apibot will attempt to make an automantion of the whole
        processing programm
        :param src.api.RestApi api: RestApi endpoint
        :param src.apios.Apios apios: Apios endpoint
        :return:
        """
        self.api = api
        self.apios = apios

    def apibot_pile(self, pile):
        """
        Create a pile of interface
        :param unicode pile: name of the pile
        :return: Pile
        """
        return pile

    def apibot_depile(self, pile, interface):
        """
        Will pop the current pile
        :param pile: pile
        :param interface: interface to pop
        :return: pile
        """
        pile = list(pile)
        pile = pile.pop(interface)
        return pile

    def apibot_empile(self, pile, interface):
        """
        Will append a interface to the current pile
        :param unicode pile: name of the pile
        :param interface: interface to append
        :return: pile
        """
        pile = list(pile)
        interface = interface
        pile = pile.append(interface)
        return pile

    def apibot_pile_empty(self, pile):
        """
        Will check if a pile is empty or not
        :param list pile: name of the pile
        :return:  len(pile) == 0
        """
        return len(pile) == 0

    def apibot_index_pile(self, pile):
        """
        return the current index pile
        :param pile: name of the pile
        :return: current index pile
        """
        s = len(pile) - 1
        return s

    def apibot_pile_sommet(self, pile):
        """
        return the sommet of the pile without popping everything around
        :param pile: name of the pile
        :return: sommet or max whatever (mad)
        """
        x = pile[Apibot.apibot_index_pile(self, pile)]
        return x

    def apibot_reverse_pile(self, pile):
        """
        WIll reverse the current pile
        :param pile: name of the pile
        :return: pile
        """
        Q = []
        while not (Apibot.apibot_pile_empty(self, pile)):
            x = pile.pop()
            Q.append(x)
            return x

    def apibot_copy_past_file_in_folder(self, path1, path2, filename):
        """
        This function will copy a file from a directory to another
        :param path1: path to the source file directory
        :param path2: path to the destination file directory
        :param filename: name of the file to copy and paste
        :return: None
        """
        path1 = path1
        path2 = path2
        filename = filename
        copyfile(path1 + filename, path2 + filename)
        return 'Success'

    def processing(self, configs):
        """
        First, we have to check if there is files in the src folder
        and we open them all
        Then we got the interface_id to get the files
        An finally we write the first 2048 first  Bytes into a file
        Will process all the tasks to perform
        :param list[dict] configs: list of configs
        :return: True if the process has been validated
        """
        pile = configs
        while pile:
            config = pile[0]
            if self.apios.check_files_in_directory(config['fichiers']['src']):
                files = self.apios.open_all_src_files(config, self.api.get_config(int(config['interface'])))
                generation_id = self.api.generate(config['interface'], files, config['environnements'])
                while self.api.status(generation_id):
                    time.sleep(0.1)

                flxs = self.api.get_files(generation_id)
                for file_name, stream in flxs.items():
                    path = config['fichiers'][file_name]
                    with open(path, "wb+") as f:
                        while True:
                            buffer = stream.read(2048)
                            f.write(buffer)
                            return True
            else:
                pile.pop()
