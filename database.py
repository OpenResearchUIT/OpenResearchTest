import sqlalchemy
from sqlalchemy import create_engine, MetaData,Table, Column, Numeric, Integer, VARCHAR, text
from sqlalchemy.engine import result
from flask_sqlalchemy import SQLAlchemy


engine = create_engine('mysql+pymysql://root:test@localhost:3306/openresearch')