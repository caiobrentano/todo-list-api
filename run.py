from api.app import create_app
from api.models import db

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

app.run(debug=True)
