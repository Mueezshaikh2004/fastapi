"""initial migration

Revision ID: 121d176f1679
Revises: ab33cf899a27
Create Date: 2026-06-29 12:06:38.220913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '121d176f1679'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Ensure the initial schema exists."""
    op.execute(
        sa.text(
            """
            CREATE TABLE IF NOT EXISTS company (
                id INTEGER NOT NULL,
                name VARCHAR NOT NULL,
                email VARCHAR,
                phone VARCHAR,
                location VARCHAR,
                PRIMARY KEY (id)
            )
            """
        )
    )
    op.execute(sa.text("CREATE INDEX IF NOT EXISTS ix_company_name ON company (name)"))

    op.execute(
        sa.text(
            """
            CREATE TABLE IF NOT EXISTS job (
                id INTEGER NOT NULL,
                title VARCHAR NOT NULL,
                description VARCHAR,
                salary INTEGER,
                company_id INTEGER,
                PRIMARY KEY (id),
                CONSTRAINT fk_job_company_id_company
                    FOREIGN KEY (company_id) REFERENCES company (id)
            )
            """
        )
    )
    op.execute(sa.text("CREATE INDEX IF NOT EXISTS ix_job_id ON job (id)"))


def downgrade() -> None:
    """Remove the initial schema if the migration is reverted."""
    op.execute(sa.text("DROP INDEX IF EXISTS ix_job_id"))
    op.execute(sa.text("DROP TABLE IF EXISTS job"))
    op.execute(sa.text("DROP INDEX IF EXISTS ix_company_name"))
    op.execute(sa.text("DROP TABLE IF EXISTS company"))
    