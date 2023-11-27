from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

# Диалект в данном случае SQLite

# Путь /test.db в текущей папке.
dns = 'sqlite:///test.db'

# Движок

engine = create_engine(dns)
session = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    orders = relationship('Order', back_populates='user')

    def __str__(self):
        return self.username


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    count = Column(Integer)

    product = relationship("Product", back_populates='orders')
    user = relationship("User", back_populates='orders')

    def __str__(self):
        return f'{self.product} -> {self.user}'


class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(50))
    phone = Column(String(50))

    products = relationship("Product", back_populates='seller')

    def __str__(self):
        return self.company


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    cost = Column(Float)
    count = Column(Integer)
    seller_id = Column(Integer, ForeignKey('sellers.id'))

    orders = relationship('Order', back_populates='product')
    seller = relationship('Seller', back_populates='products')

    def __str__(self):
        return self.name


def create_tables(eng=engine):
    Base.metadata.create_all(eng)


def drop_tables(eng=engine):
    Base.metadata.drop_all(eng)


def add_data_tables(session=session):
    with session() as sess:

        users_data = [
            {"username": "user1", "password": "pass1", "email": "user1@example.com"},
            {"username": "user2", "password": "pass2", "email": "user2@example.com"},
            {"username": "user3", "password": "pass3", "email": "user3@example.com"},
            {"username": "user4", "password": "pass4", "email": "user4@example.com"},
            {"username": "user5", "password": "pass5", "email": "user5@example.com"}
        ]

        for user in users_data:
            new_user = User(**user)
            sess.add(new_user)

        products_data = [
            {"name": "Product1", "cost": 10.5, "count": 100, "seller_id": 1},
            {"name": "Product2", "cost": 20.75, "count": 50, "seller_id": 2},
            {"name": "Product3", "cost": 15.0, "count": 75, "seller_id": 3},
            {"name": "Product4", "cost": 30.25, "count": 120, "seller_id": 4},
            {"name": "Product5", "cost": 12.0, "count": 80, "seller_id": 5}
        ]

        for product in products_data:
            new_product = Product(**product)
            sess.add(new_product)

        sellers_data = [
            {"company": "Seller1", "phone": "1234567890"},
            {"company": "Seller2", "phone": "0987654321"},
            {"company": "Seller3", "phone": "1112223333"},
            {"company": "Seller4", "phone": "4445556666"},
            {"company": "Seller5", "phone": "7778889999"}
        ]

        for seller in sellers_data:
            new_seller = Seller(**seller)
            sess.add(new_seller)

        orders_data = [
            {"user_id": 1, "product_id": 1, "count": 2},
            {"user_id": 2, "product_id": 3, "count": 1},
            {"user_id": 3, "product_id": 2, "count": 3},
            {"user_id": 4, "product_id": 5, "count": 2},
            {"user_id": 5, "product_id": 4, "count": 4}
        ]

        for order in orders_data:
            new_order = Order(**order)
            sess.add(new_order)

        sess.commit()


def queries(session=session):
    print(100 * '#')
    with session() as sess:
        query_orders = Select(Order)
        orders = sess.execute(query_orders).scalars()

        for order in orders:
            print(order)


drop_tables()
create_tables()

add_data_tables()
queries()
