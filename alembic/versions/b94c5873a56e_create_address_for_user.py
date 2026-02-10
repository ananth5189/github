"""create address for user

Revision ID: b94c5873a56e
Revises: 
Create Date: 2026-02-09 16:29:22.822667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b94c5873a56e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users',sa.Column('address',sa.String(),nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
