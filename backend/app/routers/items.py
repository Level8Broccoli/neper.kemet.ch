from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.get("/")
def get_all_items():
    return "nice!"
