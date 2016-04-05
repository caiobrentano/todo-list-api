from api.app import create_app
from api.models import db, User


app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    u = User(username='caio', password='senha')
    db.session.add(u)

    db.session.commit()

app.run(debug=True)
