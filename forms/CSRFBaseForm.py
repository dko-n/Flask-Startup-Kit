import binascii
import os
from flask import session
from wtforms import Form
from wtforms.csrf.session import SessionCSRF

class CSRFBaseForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = binascii.hexlify(os.urandom(36))
        
        @property
        def csrf_context(self):
            return session
