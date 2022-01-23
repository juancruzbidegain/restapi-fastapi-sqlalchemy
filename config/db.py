from sqlalchemy import create_engine, MetaData



engine = create_engine("mysql+pymysql://testdb:testdb@localhost:3306/store")


meta = MetaData()

con = engine.connect()