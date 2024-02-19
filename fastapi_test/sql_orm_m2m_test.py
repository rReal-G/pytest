
from sqlalchemy.orm.session import Session
from fastapi_test.sql_orm_o2o_test import get_db


with get_db() as session: 
    session:Session