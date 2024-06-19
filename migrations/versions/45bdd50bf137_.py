"""empty message

Revision ID: 45bdd50bf137
Revises: c94d98c6050e
Create Date: 2024-06-18 20:27:24.225235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45bdd50bf137'
down_revision = 'c94d98c6050e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('t_subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('t_student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['t_group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('t_teacher_group_subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['t_group.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['t_subject.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['t_teacher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_teacher_group_subject')
    op.drop_table('t_student')
    op.drop_table('t_subject')
    op.drop_table('t_group')
    # ### end Alembic commands ###