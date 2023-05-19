from fastapi import FastAPI
from pydantic import BaseModel
from database import db_conn
from models import ST_info, ST_grade

app = FastAPI()

db = db_conn()
session = db.sessionmaker()

class Item(BaseModel):
    name : str
    number : int

@app.get('/')
async def healthCheck():
    return "OK"

@app.get('/stinfo')
async def select_st_info():
    result = session.query(ST_info)
    return result.all()

@app.get('/stgrade')
async def select_st_grade():
    result = session.query(ST_grade).all()
    return result

@app.get('/getuser')
async def getuser(id=None, name=None):
    if (id is None) and (name is None):
        return "학번 또는 이름으로 검색하세요."
    else:
        if name is None:
            result = session.query(ST_info).filter(ST_info.ST_ID == id).all()
        elif id is None:
            result = session.query(ST_info).filter(ST_info.NAME == name).all()
        else:
            result = session.query(ST_info).filter(ST_info.ST_ID == id,
            ST_info.NAME == name).all()

    return result

@app.get('/useradd')
async def useradd(id=None, name=None, dept=None):
    if (id and name and dept) is None:
        return "학과, 이름, 학과명을 입력하세요."
    else:
        user = ST_info(ST_ID=id, NAME=name, DEPT=dept)
        session.add(user)
        session.commit()
        result = session.query(ST_info).all()
        return result

@app.get('/userdel')
async def userdel(id=None):
    if id is None:
        return "id를 입력하세요."
    else:
        result = session.query(ST_info).filter(ST_info.ST_ID == id)
        if result.first() is None:
            return "데이터가 존재하지 않습니다."
        else:
            result.delete()
            session.commit()
            result = session.query(ST_info).all()
            return result

@app.get('/userupdate')
async def userupdate(id=None, name=None, dept=None):
    if (id and name and dept) is None:
        return "학과, 이름, 학과명을 입력하세요."
    else:
        user = session.query(ST_info).filter(ST_info.ST_ID == id).first()
        if user is None:
            return "데이터가 존재하지 않습니다."
        else:
            user.NAME = name
            user.DEPT = dept
            session.add(user)
            session.commit()
            result = session.query(ST_info).filter(ST_info.ST_ID == id).all()
            return result