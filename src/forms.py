#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 3

from wtforms import *
from flask import request
import logging
import jinja2.ext
logger = logging.getLogger(__name__)


class DynamicForm(Form):

    def add_field(self, name, unbound_field):
        """
        Add a field named 'name' to the form
        :param unicode name : field's name
        :param Field unbound_field : field to add
        :return: None
        """
        options = dict(name=name, prefix=self._prefix, translations=self._get_translations())
        field = self.meta.bind_field(self, unbound_field, options)
        field.process(request.form)
        self._fields[name] = field


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()






