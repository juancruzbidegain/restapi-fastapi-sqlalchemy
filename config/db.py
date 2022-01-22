from sqlalchemy import create_engine, MetaData



engine = create_engine("mysql+pymysql://test:1234@localhost:3306/store")


meta = MetaData()

con = engine.connect()