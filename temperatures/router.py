from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from cities import crud as cities_crud
from temperatures import crud, schemas, service

router = APIRouter(prefix="/temperatures", tags=["Temperatures"])


@router.post(
    "/",
    response_model=schemas.Temperature,
    status_code=status.HTTP_201_CREATED
)
async def update_temperature_for_city(city_id: int, db: Session = Depends(get_db)):
    db_city = cities_crud.get_city(db, city_id=city_id)
    if not db_city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="City not found",
        )

    current_temp = await service.fetch_temperature_for_city(db_city.name)
    if current_temp is None:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Could not fetch weather data for city '{db_city.name}'",
        )

    temp_create = schemas.TemperatureCreate(
        city_id=city_id,
        temperature=current_temp,
    )
    return crud.create_temperature(db=db, temperature=temp_create)


@router.get("/", response_model=list[schemas.Temperature])
def read_temperatures(
    city_id: int | None = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    if city_id is not None:
        db_city = cities_crud.get_city(db, city_id=city_id)
        if not db_city:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="City not found",
            )

    return crud.get_temperatures(db=db, skip=skip, limit=limit, city_id=city_id)