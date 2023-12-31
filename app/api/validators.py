from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectUpdate


async def check_name_duplicate(
    charity_project_name: str,
    session: AsyncSession,
) -> None:
    """Проверка уникальности названия проекта."""

    charity_project_id = await charity_project_crud.get_charity_project_id_by_name(
        charity_project_name, session
    )
    if charity_project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Проект с таким именем уже существует!",
        )


async def check_charity_project_exists(
    project_id: int, session: AsyncSession
) -> CharityProject:
    """Проверка наличия проекта в базе данных."""

    charity_project = await charity_project_crud.get_charity_project_by_id(
        project_id, session
    )
    if not charity_project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Проект не найден!"
        )
    return charity_project


async def check_full_amount_befor_edit_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession,
):
    """Проверка суммы инвестирования при корректировке проекта."""

    charity_project = await charity_project_crud.get_charity_project_by_id(
        project_id, session
    )
    if obj_in.full_amount < charity_project.invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Нельзя скорректировать сумму проекта в меньшую сторону!",
        )


async def check_the_project_is_closed(
    project_id: int,
    session: AsyncSession,
):
    """Проверяем закрыт ли проект."""
    charity_project = await charity_project_crud.get_charity_project_by_id(
        project_id, session
    )
    if charity_project.close_date is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Закрытый проект нельзя редактировать!",
        )


async def check_invested_amount(
    project_id: int,
    session: AsyncSession,
):
    charity_project = await charity_project_crud.get_charity_project_by_id(
        project_id, session
    )
    if charity_project.invested_amount != 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="В проект были внесены средства, не подлежит удалению!",
        )
