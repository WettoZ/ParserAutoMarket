from  creat_db import  *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  asc

def add_mark(name):
    Session = sessionmaker(bind=engine)
    session = Session()
    se = session.query(Mark).filter_by(name = name).first()
    if se:
        id_mark = se.id
        print('Марка уже есть')
    else:
        post = Mark(name = name)
        session.add(post)
        id_mark = session.query(Mark).count()
        print('Добавил марку')

    session.commit()
    return id_mark

def add_model(name, id_mark):
    Session = sessionmaker(bind=engine)
    session = Session()
    se = session.query(Model).filter_by(name = name, id_mark = id_mark).first()
    if se:
        id_model = se.id
        print('Модель уже есть')
    else:
        post = Model(name = name, id_mark = id_mark)
        session.add(post)
        id_model = session.query(Mark).count()
        print('Добавил модель')

    session.commit()
    return id_model


def add_ads(mark, model, salone, price, mile, year, motor, rudder, trans, gear, href, img, description):
    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(Ads).filter_by(href = href).first():
        print('Данное объявление уже в базе')
        return 0

    else:
        id_mark = add_mark(mark)
        id_model = add_model(model, id_mark)

        post = Ads(id_mark = id_mark,
        id_model = id_model,
        salone = salone,
        price = price,
        mile = mile,
        year = year,
        motor = motor,
        rudder =rudder,
        trans = trans,
        gear = gear,
        href = href,
        img = img,
        description = description)
        print('Объявление добавлено')
        session.add(post)
        session.commit()

def view_mark():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(Mark).order_by(asc(Mark.name)).all()

def view_model(mark):
    Session = sessionmaker(bind=engine)
    session = Session()
    id_mark = session.query(Mark).filter_by(Mark.name == mark).first()
    id_mark = id_mark.id
    return session.query(Model).filter_by(Model.name == id_mark).all()


view_mark()
