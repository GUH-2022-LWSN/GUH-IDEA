from fastapi import APIRouter

router = APIRouter()

@router.get("/users/online")
async def test_online():
    return [{"Online": True}]
