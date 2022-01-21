from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:123@localhost:3306/storedb")

con = engine.connect()