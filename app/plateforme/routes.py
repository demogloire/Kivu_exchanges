from flask import render_template, flash, url_for, redirect, request, session
from .. import db, bcrypt
from ..models import User, Trucking, Transit 
from app.plateforme.forms import ColisForm
from flask_login import login_user, current_user, logout_user, login_required
from . import plate

@plate.route('/', methods=['GET','POST'])
def index():
   title='Accueil | Kivu Exchange'

   return render_template('plateforme/acceuil.html',  title=title)


@plate.route('/suiviscolis', methods=['GET','POST'])
def suivis():
   title='Suivis colis | Kivu Exchange'
   form=ColisForm()
   trucking_id_client=None
   track_statu=None
   track_transit=None
   if form.validate_on_submit():
      numero=Trucking.query.filter_by(tracking_number=form.numero.data).first()
      if numero is None:
         trucking_id_client=True
         flash("Aucun colis avec ce numéro","danger")
      else:
         trucking_id_client='requete'
         #Requête de vérification du trancking
         track_statu=Trucking.query.filter_by(tracking_number=form.numero.data).first()
         print(track_statu)
         #Transit du colis.
         track_transit=Transit.query.filter_by(trucking_id=track_statu.id).all() 

   return render_template('plateforme/suiviscolis.html', trucking_id_client=trucking_id_client, truck=track_statu, track_transit=track_transit, title=title, form=form)
