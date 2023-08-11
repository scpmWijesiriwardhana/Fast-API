"""create post table

Revision ID: ad3c76005848
Revises: 
Create Date: 2023-08-10 16:24:08.745073

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad3c76005848'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.Integer, nullable=False,primary_key=True),
                    sa.Column("title", sa.String, nullable=False),
                    sa.Column("content", sa.String, nullable=False),
                    sa.Column("published", sa.Boolean, nullable=False),
                    )

    pass


def downgrade():
    op.drop_table("posts")
    
    pass
