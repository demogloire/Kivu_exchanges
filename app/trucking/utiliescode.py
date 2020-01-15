import random
import string
import time
import uuid
from datetime import datetime
from flask import redirect, session, url_for
from dateutil.relativedelta import relativedelta, MO
from functools import wraps

#Code unique trucking
def trucking_number(length=12):
    #put your letters in the following string
    your_letters='1234567890'
    return ''.join((random.choice(your_letters) for i in range(length)))


def truckin_id(f):
    @wraps(f)
    def wrap(*args, **kwargs):
      if 'truck' in session:
        return f(*args, **kwargs)
      else:
        return redirect(url_for('trucking.littruck'))
    return wrap