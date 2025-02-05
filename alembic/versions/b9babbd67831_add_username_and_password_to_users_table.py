"""add username and password to users table

Revision ID: b9babbd67831
Revises: 
Create Date: 2025-01-31 03:17:18.949021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9babbd67831'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'age',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'age',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('users', 'password')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
