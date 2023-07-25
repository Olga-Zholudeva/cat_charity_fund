"""First migration

Revision ID: 0d394b25cd37
Revises: 
Create Date: 2023-07-19 14:59:20.786694

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0d394b25cd37"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "charityproject",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("charityproject")
    # ### end Alembic commands ###
