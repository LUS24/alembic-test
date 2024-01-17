"""Add another test table

Revision ID: 7d4f35f67b35
Revises: 6a0466b077c6
Create Date: 2024-01-17 09:55:12.808371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d4f35f67b35'
down_revision: Union[str, None] = '6a0466b077c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests_migrations_2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tests_migrations_2')
    # ### end Alembic commands ###