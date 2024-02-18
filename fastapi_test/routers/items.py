

from fastapi import APIRouter, FastAPI


# router = APIRouter(prefix='/items', tags=['items'])
router = FastAPI()


@router.get('/')
async def index():
    return 'items/ here'

@router.get('/{price}')
async def get_by_price():
    return r'items/{price} here'