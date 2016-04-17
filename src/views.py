#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3
import time
from traceback import print_exc
from flask import Flask, render_template, request, redirect, flash, url_for, Response
from wtforms.validators import DataRequired
from flask_wtf.form import _is_hidden
from wtforms import StringField, SelectField, BooleanField, SubmitField
from src import forms
from src.api import interfaces
import itertools
import jinja2.ext
import os
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def display_templates(app, api, apios, apibot):
    """
    init the app using givent api endpoint
    :param Flask app: the flask app
    :param src.api.RestApi api: the api endpoint
    :param src.apios.Apios apios: the apios endpoint
    :param src.apibot.Apibot apibot : the apibot endpoint
    :return:
    """

    @app.route('/config/list/')
    def config_list():
        #   Get the config list in ResAPi Class and display the list
        configs = api.list()

        return render_template('config_list.html', configs=configs)

    @app.route('/progress/<config_id>/')
    def process(config_id):
        captured = config_id
        configs = api.get_config(int(captured))
        interface = api.get(interface['id'] for interface in interfaces)
        flash(u'Fichier généré YOUPI', "success")
        apios.open_all_src_files(configs, interface)
        apibot.processing([configs])
        return redirect(url_for("config_detail", config_id=config_id))

    @app.route('/config/detail/<config_id>/', methods=["POST", "GET"])
    def config_detail(config_id):
        #   Enables you to capture the config id to edit the config
        form = forms.DynamicForm()
        captured = config_id
        config = api.get_config(int(captured))
        #   Display the list of files in a directory
        liste = []
        for fichier, path in config['fichiers'].items():
            #   If the file is source, we display it.
            if (interface['fichiers']['est_sources']for interface in interfaces):
                liste.append((os.path.exists(path), fichier, path))

        return render_template('config_detail.html', form=form, is_hidden=_is_hidden, config=config, id=config_id,
                               liste=liste)

    @app.route('/config/edit/<config_id>/', methods=["GET", "POST"])
    def config_edit(config_id):

        #   Create the form
        form = forms.DynamicForm()
        captured = config_id
        #    config_id is a 'int', it will displays in the url like /1/ | /2/ |/3/
        config = api.get_config(int(captured))
        try:
            #   Choices define here the default choices available in the 'interface choice field'
            choices = [(interface['id'], interface['nom']) for interface in interfaces]
            #   Add field to the form dynamically
            form.add_field('name', StringField("nom de la config", validators=[DataRequired()], default=config['nom']))
            form.add_field('interface', SelectField('interface', choices=choices, default=config['interface']))
            try:
                interface_id = int(form.data['interface'])
            except KeyError:
                pass
            else:
                #   Get the interface id to add the field below or not to the form.
                interface = api.get(interface_id)
                for fichier in interface['fichiers']:
                    #   Browsing through the list of dictionnary to display values.
                    form.add_field(fichier['nom'], StringField(
                        fichier["display_nom"],
                        validators=[DataRequired],
                        default=config['fichiers'][fichier['nom']]
                    ))
                for environnement in interface['environnements']:
                    form.add_field(environnement['nom'], StringField(
                        environnement['display_nom'],
                        validators=[DataRequired],
                        default=config['environnements'][environnement['nom']]
                    ))
        except Exception:
            print_exc()

        if request.method == "POST":
            try:
                #   If the form is posted, the new entries will be applied to the current one.
                config['nom'] = form.data['name']
                config['interface'] = form.data['interface']
                try:
                    interface_id = int(form.data['interface'])
                except KeyError:
                    pass
                else:
                    interface = api.get(interface_id)
                    for fichier, environnement in itertools.product(interface['fichiers'], interface['environnements']):
                        nom_file = fichier['nom']
                        config['fichiers'][nom_file] = form.data[nom_file]
                        config['environnements'][environnement['nom']] = form.data[environnement['nom']]
                    api.set_config(config)
                    #   will apply the new config to the current one
                    flash(u"Configuration sauvegardée avec succès", "success")
                    #   flash will display a success message if the form is saved
                return redirect(url_for('config_list'))
                #   return at the config_list page
            except Exception:
                print_exc()

        return render_template('config_edit.html', form=form, config=config, is_hidden=_is_hidden, data=form.data)
    #   return a config_edit page with his context

    @app.route('/config/files/select/', methods=['GET', 'POST'])
    def are_you_sure():
        if request.method == "POST":
            checked = request.form['checkbox']
            print(checked)
            return render_template('select_files.html', checked=checked)

    return app.run(debug=True)
#   Launch the app


