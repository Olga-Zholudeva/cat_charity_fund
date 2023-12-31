"""Измения в моделях проект и пожертвование

Revision ID: a5e232ef6f7e
Revises: 7afcb5d7b3cf
Create Date: 2023-07-24 19:57:24.898581

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "a5e232ef6f7e"
down_revision = "7afcb5d7b3cf"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("charityproject", schema=None) as batch_op:
        batch_op.alter_column("full_amount", existing_type=sa.INTEGER(), nullable=False)

    with op.batch_alter_table("donation", schema=None) as batch_op:
        batch_op.alter_column("full_amount", existing_type=sa.INTEGER(), nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("donation", schema=None) as batch_op:
        batch_op.alter_column("full_amount", existing_type=sa.INTEGER(), nullable=True)

    with op.batch_alter_table("charityproject", schema=None) as batch_op:
        batch_op.alter_column("full_amount", existing_type=sa.INTEGER(), nullable=True)

    # ### end Alembic commands ###
