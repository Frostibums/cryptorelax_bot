"""initial

Revision ID: db5a7a574479
Revises: 
Create Date: 2024-02-18 21:25:21.192846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db5a7a574479'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscription_plans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subscription_time', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('txn_hashs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chain', sa.String(), nullable=False),
    sa.Column('transaction_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('transaction_hash')
    )
    op.create_table('users',
    sa.Column('telegram_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('telegram_username', sa.String(), nullable=True),
    sa.Column('registered_at', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('telegram_id')
    )
    op.create_table('subscriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_telegram_id', sa.BigInteger(), nullable=True),
    sa.Column('subscription_plan_id', sa.BigInteger(), nullable=True),
    sa.Column('txn_hash_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.DATE(), nullable=True),
    sa.Column('end_time', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['owner_telegram_id'], ['users.telegram_id'], ),
    sa.ForeignKeyConstraint(['subscription_plan_id'], ['subscription_plans.id'], ),
    sa.ForeignKeyConstraint(['txn_hash_id'], ['txn_hashs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscriptions')
    op.drop_table('users')
    op.drop_table('txn_hashs')
    op.drop_table('subscription_plans')
    # ### end Alembic commands ###
