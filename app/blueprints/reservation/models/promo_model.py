from ....extensions import db, Column, Text, String, Numeric, orm

class Promo(db.Model):
    __tablename__ = 'promotbl'

    promoID = Column(String, primary_key=True, name='promoid')
    discount = Column(Numeric(8,2), nullable=False, name='discount')
    description = Column(Text, name='description')

    bookings = orm.relationship('Booking', back_populates='promos')