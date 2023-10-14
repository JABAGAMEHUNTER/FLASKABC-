from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Noticia 
from flaskblog.noticias.forms import NoticiaForm

noticias = Blueprint('noticias', __name__)


@noticias.route("/noticias", methods=['GET', 'POST'])
@login_required
def news():
    page = request.args.get('page', 1, type=int)
    posts = Noticia.query.order_by(Noticia.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('news.html', post=noticias)
