"""empty message

Revision ID: 10f2cc402bf5
Revises: 2a34ebf22397
Create Date: 2024-06-21 20:51:54.493977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10f2cc402bf5'
down_revision = '2a34ebf22397'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['phone_number'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###