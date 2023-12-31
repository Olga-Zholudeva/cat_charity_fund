"""Вторая миграция

Revision ID: 10ff371d106f
Revises: 0d394b25cd37
Create Date: 2023-07-19 19:11:51.265544

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "10ff371d106f"
down_revision = "0d394b25cd37"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "charityproject", sa.Column("full_amount", sa.Integer(), nullable=True)
    )
    op.add_column(
        "charityproject", sa.Column("invested_amount", sa.Integer(), nullable=True)
    )
    op.add_column(
        "charityproject", sa.Column("fully_invested", sa.Boolean(), nullable=True)
    )
    op.add_column(
        "charityproject", sa.Column("create_date", sa.DateTime(), nullable=True)
    )
    op.add_column(
        "charityproject", sa.Column("close_date", sa.DateTime(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("charityproject", "close_date")
    op.drop_column("charityproject", "create_date")
    op.drop_column("charityproject", "fully_invested")
    op.drop_column("charityproject", "invested_amount")
    op.drop_column("charityproject", "full_amount")
    # ### end Alembic commands ###
