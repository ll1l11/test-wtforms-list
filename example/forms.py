# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms.fields import StringField, FieldList


class TagForm(Form):
    tags = FieldList(StringField('tag'), min_entries=2)
