from typing import Annotated, Dict, List, Optional
from fastapi import Body, Cookie, Depends, FastAPI, Header, Query, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, SecretStr, field_validator, validator
import uvicorn
import os
from routers import items

app = FastAPI()
template = Jinja2Templates(directory='fastapi/templazes')

#app.include_router(items.router)
app.mount('/subapp/items', items.router)


@app.middleware('http')
async def add_header(req:Request, call_next):
    print('inside add_header middleware')
    res:Response = await call_next(req)
    res.headers.append('X-G-Value', 'top GGG')
    return res


# @app.get('/{path_parameter}')
# async def index(
#     path_parameter:str, 
#     query_parameter: Annotated[str | None, Query(max_length=3)] = None):
#     return {
#         'path_parameter': path_parameter,
#         'query_parameter': query_parameter
#         }

@app.get('/')
async def index(req:Request):
    return template.TemplateResponse(
    'test.html', context={'request': req, 'name': 'top g'}, status_code=201    
    )

async def req_in_dep(req:Request, Accept_Language:Annotated[str, Header()]):
    return repr(req.url) + Accept_Language

@app.get('/{name}')
async def kekw(req: Request, name:str, rep: Response, url = Depends(req_in_dep)):
    print(os.getcwd())
    return url

    # rep.status_code = 201
    # return 'lmao'

    # return template.TemplateResponse(
    #     'test.html', context={'request': req, 'name': name}, status_code=201
    #     )

class Student(BaseModel):
    name:str|None = 'lmaddo'
    subjects: Annotated[Dict[str|int, str|int|bool] | None, Field()] = {'gg':666}
    secret: Annotated[SecretStr, Field(max_length=3)] 

@app.post('/students')
async def create_student(s: Student):
    return s


class Product(BaseModel):
    prodId:int
    prodName: Annotated[str, Field(max_length=5)]
    price:float
    class Config:
        from_attributes=True
    
    @field_validator('price')
    def validate_price(cls, x):
        if x > 2:
            raise ValueError('price is t000 much')
        return x
        

type(type('hehe')('gggg'))

# from contextlib import contextmanager
# @contextmanager
# def test_exception():
#     try:
#         yield ValueError('hehe')
#     finally:
#         print('i closed heheheheheheheheheheh')

# with test_exception() as excep:
#     raise excep

# err = test_exception()
# raise next(err)



@app.post('/post')
async def post_test(
    body_int: Annotated[int, Body(lt=555)],
    #prod: Product | None = None, 
    prod_list: List[Product],
    body_nullable_str: Annotated[str|None, Body(max_length=3)] = '333',
    ):
    dic = prod_list[0].model_dump()
    print(dic)
    print(prod_list[1].prodName)
    return {
        'body_int': body_int,
        'body_nullable_str': body_nullable_str,
        #'prod': prod
        'prod_list': prod_list
    }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')