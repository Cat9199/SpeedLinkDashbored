from app import db, app, Admins
with app.app_context():
    info = Admins(username='admin',password='123')
    db.session.add(info)
    db.session.commit()
