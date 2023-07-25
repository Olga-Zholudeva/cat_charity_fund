from sqlalchemy import Column, String, Text


from app.models.base import CharityProjectDonationBaseModel


class CharityProject(CharityProjectDonationBaseModel):
    """Модель проекта."""

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
