"""Add user relationship to Donation

Revision ID: 7afcb5d7b3cf
Revises: c7df9a4b4251
Create Date: 2023-07-23 15:41:00.483530

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "7afcb5d7b3cf"
down_revision = "c7df9a4b4251"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("donation", schema=None) as batch_op:
        batch_op.add_column(sa.Column("user_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "fk_donation_user_id_user", "user", ["user_id"], ["id"]
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("donation", schema=None) as batch_op:
        batch_op.drop_constraint("fk_donation_user_id_user", type_="foreignkey")
        batch_op.drop_column("user_id")

    # ### end Alembic commands ###
