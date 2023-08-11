"""add last few columns to posts table

Revision ID: 65f96ce382c7
Revises: b5c1ee1174d0
Create Date: 2023-08-11 09:05:34.462127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65f96ce382c7'
down_revision: Union[str, None] = 'b5c1ee1174d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts",
        sa.Column("created_at", sa.TIMESTAMP(timezone=True),server_default=sa.text('NOW()'),  nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "created_at")
    pass
