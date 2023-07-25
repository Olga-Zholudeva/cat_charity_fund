# from app.core.db import AsyncSessionLocal
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_charity_project_id_by_name(
        self,
        charity_project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        """Получаем id существующего проекта из базы данных."""

        db_charity_project_id = await session.execute(
            select(CharityProject.id).where(CharityProject.name == charity_project_name)
        )
        db_charity_project_id = db_charity_project_id.scalars().first()
        return db_charity_project_id

    async def get_charity_project_by_id(
        self,
        charity_project_id: int,
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        """Получаем проект по id."""

        db_charity_project = await session.execute(
            select(CharityProject).where(CharityProject.id == charity_project_id)
        )
        db_charity_project = db_charity_project.scalars().first()
        return db_charity_project


charity_project_crud = CRUDCharityProject(CharityProject)
