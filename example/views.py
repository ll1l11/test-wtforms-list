# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

from .forms import TagForm

bp = Blueprint('general', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = TagForm()
    if form.validate_on_submit():
        print(form.tags.data)
    return render_template('index.html', form=form)
