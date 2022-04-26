from flask_wtf import *
from wtforms import *
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from queries import *

class UploadDocumentForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    authors = StringField(validators=[DataRequired()])
    description = TextAreaField([validators.optional(), validators.length(max=10000)])
    date = DateField(format='%Y-%m-%d')
    visibility = SelectField(choices=[(str(i.idAccess),i.AccesType) for i in fetchAccessRights()])
    type = SelectField(choices=[('1', 'Bachelor'), ('2', 'Masters')])
    subject = SelectField(choices=[(str(i.idCatalog),i.CatalogName) for i in fetchAllCatalogs()])
    file = FileField(validators=[FileRequired()])
    tags = StringField(validators=[DataRequired()])