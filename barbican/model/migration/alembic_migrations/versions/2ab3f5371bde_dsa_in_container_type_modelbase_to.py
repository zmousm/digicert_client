"""dsa in container type modelbase_to

Revision ID: 2ab3f5371bde
Revises: 4070806f6972
Create Date: 2014-09-02 12:11:43.524247

"""

# revision identifiers, used by Alembic.
revision = '2ab3f5371bde'
down_revision = '4070806f6972'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('container_secret', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('container_secret', sa.Column('deleted', sa.Boolean(), nullable=False))
    op.add_column('container_secret', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('container_secret', sa.Column('id', sa.String(length=36), nullable=False))
    op.add_column('container_secret', sa.Column('status', sa.String(length=20), nullable=False))
    op.add_column('container_secret', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.execute( 'ALTER TABLE container_secret DROP PRIMARY KEY, ADD PRIMARY KEY(`id`,`container_id`,`secret_id`)');
    op.execute( 'ALTER TABLE containers CHANGE type type ENUM(\'generic\',\'rsa\',\'dsa\',\'certificate\') DEFAULT NULL');
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('container_secret', 'updated_at')
    op.drop_column('container_secret', 'status')
    op.drop_column('container_secret', 'id')
    op.drop_column('container_secret', 'deleted_at')
    op.drop_column('container_secret', 'deleted')
    op.drop_column('container_secret', 'created_at')
    op.execute( 'ALTER TABLE container_secret DROP PRIMARY KEY, ADD PRIMARY KEY(`container_id`,`secret_id`)');
    op.execute( 'ALTER TABLE containers CHANGE type type ENUM(\'generic\',\'rsa\',\'certificate\') DEFAULT NULL');
    ### end Alembic commands ###
