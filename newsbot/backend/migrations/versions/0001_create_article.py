"""create article table

Revision ID: 0001
Revises: 
Create Date: 2025-07-23
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String(length=512), nullable=False),
        sa.Column('summary', sa.Text, nullable=True),
        sa.Column('source_url', sa.String(length=1024), nullable=False),
        sa.Column('published_at', sa.DateTime, nullable=True),
        sa.Column('language', sa.String(length=16), nullable=True),
        sa.Column('status', sa.String(length=32), nullable=True),
    )

def downgrade():
    op.drop_table('articles')
