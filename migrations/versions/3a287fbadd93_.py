"""empty message

Revision ID: 3a287fbadd93
Revises: bb746be3bcf6
Create Date: 2017-11-29 09:28:05.406000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a287fbadd93'
down_revision = 'bb746be3bcf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('front_user_id', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('customs_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customs_user_id'], ['customs_user.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['front_user_id'], ['front_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message_to_customs_user',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('customs_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customs_user_id'], ['customs_user.id'], ),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.PrimaryKeyConstraint('message_id', 'customs_user_id')
    )
    op.create_table('message_to_employee',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.PrimaryKeyConstraint('message_id', 'employee_id')
    )
    op.create_table('message_to_front_user',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('front_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['front_user_id'], ['front_user.id'], ),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.PrimaryKeyConstraint('message_id', 'front_user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message_to_front_user')
    op.drop_table('message_to_employee')
    op.drop_table('message_to_customs_user')
    op.drop_table('message')
    # ### end Alembic commands ###