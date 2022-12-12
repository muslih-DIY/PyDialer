"""asterisk realtimedb

Revision ID: cd3ad9aead73
Revises: 
Create Date: 2022-12-10 21:47:33.469789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd3ad9aead73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('extensions',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('context', sa.String(length=40), nullable=True),
    sa.Column('exten', sa.String(length=40), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('app', sa.String(length=40), nullable=True),
    sa.Column('appdata', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('context', 'exten', 'priority', name='cont_ext_pr_unq')
    )
    op.create_index(op.f('ix_extensions_id'), 'extensions', ['id'], unique=False)
    op.create_table('ps_aors',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('contact', sa.String(length=40), nullable=True),
    sa.Column('default_expiration', sa.Integer(), nullable=True),
    sa.Column('mailboxes', sa.String(length=80), nullable=True),
    sa.Column('max_contacts', sa.Integer(), nullable=True),
    sa.Column('minimum_expiration', sa.Integer(), nullable=True),
    sa.Column('remove_existing', sa.String(length=20), nullable=True),
    sa.Column('qualify_frequency', sa.Integer(), nullable=True),
    sa.Column('authenticate_qualify', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ps_aors_id'), 'ps_aors', ['id'], unique=False)
    op.create_table('ps_auth',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('auth_type', sa.String(length=40), nullable=True),
    sa.Column('nonce_lifetime', sa.Integer(), nullable=True),
    sa.Column('md5_cred', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.Column('realm', sa.String(length=40), nullable=True),
    sa.Column('username', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ps_auth_id'), 'ps_auth', ['id'], unique=False)
    op.create_table('ps_endpoint',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('transport', sa.String(length=40), nullable=True),
    sa.Column('aors', sa.String(length=200), nullable=True),
    sa.Column('auth', sa.String(length=40), nullable=True),
    sa.Column('context', sa.String(length=40), nullable=True),
    sa.Column('disallow', sa.String(length=200), nullable=True),
    sa.Column('allow', sa.String(length=200), nullable=True),
    sa.Column('direct_media', sa.String(length=40), nullable=True),
    sa.Column('connected_line_method', sa.String(length=40), nullable=True),
    sa.Column('direct_media_method', sa.String(length=40), nullable=True),
    sa.Column('direct_media_glare_mitigation', sa.String(length=40), nullable=True),
    sa.Column('disable_direct_media_on_nat', sa.String(length=40), nullable=True),
    sa.Column('dtmf_mode', sa.String(length=40), nullable=True),
    sa.Column('external_media_address', sa.String(length=40), nullable=True),
    sa.Column('force_rport', sa.String(length=40), nullable=True),
    sa.Column('ice_support', sa.String(length=40), nullable=True),
    sa.Column('identify_by', sa.String(length=40), nullable=True),
    sa.Column('mailboxes', sa.String(length=40), nullable=True),
    sa.Column('moh_suggest', sa.String(length=40), nullable=True),
    sa.Column('outbound_auth', sa.String(length=40), nullable=True),
    sa.Column('outbound_proxy', sa.String(length=40), nullable=True),
    sa.Column('rewrite_contact', sa.String(length=40), nullable=True),
    sa.Column('rtp_ipv6', sa.String(length=40), nullable=True),
    sa.Column('rtp_symmetric', sa.String(length=40), nullable=True),
    sa.Column('send_diversion', sa.String(length=40), nullable=True),
    sa.Column('send_pai', sa.String(length=40), nullable=True),
    sa.Column('send_rpid', sa.String(length=40), nullable=True),
    sa.Column('timers_min_se', sa.Integer(), nullable=True),
    sa.Column('timers', sa.String(length=40), nullable=True),
    sa.Column('timers_sess_expires', sa.Integer(), nullable=True),
    sa.Column('callerid', sa.String(length=40), nullable=True),
    sa.Column('callerid_privacy', sa.String(length=40), nullable=True),
    sa.Column('callerid_tag', sa.String(length=40), nullable=True),
    sa.Column('100rel', sa.String(length=40), nullable=True),
    sa.Column('aggregate_mwi', sa.String(length=40), nullable=True),
    sa.Column('trust_id_inbound', sa.String(length=40), nullable=True),
    sa.Column('trust_id_outbound', sa.String(length=40), nullable=True),
    sa.Column('use_ptime', sa.String(length=40), nullable=True),
    sa.Column('use_avpf', sa.String(length=40), nullable=True),
    sa.Column('media_encryption', sa.String(length=40), nullable=True),
    sa.Column('inband_progress', sa.String(length=40), nullable=True),
    sa.Column('call_group', sa.String(length=40), nullable=True),
    sa.Column('pickup_group', sa.String(length=40), nullable=True),
    sa.Column('named_call_group', sa.String(length=40), nullable=True),
    sa.Column('named_pickup_group', sa.String(length=40), nullable=True),
    sa.Column('device_state_busy_at', sa.Integer(), nullable=True),
    sa.Column('fax_detect', sa.String(length=40), nullable=True),
    sa.Column('t38_udptl', sa.String(length=40), nullable=True),
    sa.Column('t38_udptl_ec', sa.String(length=40), nullable=True),
    sa.Column('t38_udptl_maxdatagram', sa.Integer(), nullable=True),
    sa.Column('t38_udptl_nat', sa.String(length=40), nullable=True),
    sa.Column('t38_udptl_ipv6', sa.String(length=40), nullable=True),
    sa.Column('tone_zone', sa.String(length=40), nullable=True),
    sa.Column('language', sa.String(length=40), nullable=True),
    sa.Column('one_touch_recording', sa.String(length=40), nullable=True),
    sa.Column('record_on_feature', sa.String(length=40), nullable=True),
    sa.Column('record_off_feature', sa.String(length=40), nullable=True),
    sa.Column('rtp_engine', sa.String(length=40), nullable=True),
    sa.Column('allow_transfer', sa.String(length=40), nullable=True),
    sa.Column('allow_subscribe', sa.String(length=40), nullable=True),
    sa.Column('sdp_owner', sa.String(length=40), nullable=True),
    sa.Column('sdp_session', sa.String(length=40), nullable=True),
    sa.Column('tos_audio', sa.Integer(), nullable=True),
    sa.Column('tos_video', sa.Integer(), nullable=True),
    sa.Column('cos_audio', sa.Integer(), nullable=True),
    sa.Column('cos_video', sa.Integer(), nullable=True),
    sa.Column('sub_min_expiry', sa.Integer(), nullable=True),
    sa.Column('from_domain', sa.String(length=40), nullable=True),
    sa.Column('from_user', sa.String(length=40), nullable=True),
    sa.Column('mwi_fromuser', sa.String(length=40), nullable=True),
    sa.Column('dtls_verify', sa.String(length=40), nullable=True),
    sa.Column('dtls_rekey', sa.String(length=40), nullable=True),
    sa.Column('dtls_cert_file', sa.String(length=200), nullable=True),
    sa.Column('dtls_private_key', sa.String(length=200), nullable=True),
    sa.Column('dtls_cipher', sa.String(length=200), nullable=True),
    sa.Column('dtls_ca_file', sa.String(length=200), nullable=True),
    sa.Column('dtls_ca_path', sa.String(length=200), nullable=True),
    sa.Column('dtls_setup', sa.String(length=40), nullable=True),
    sa.Column('srtp_tag_32', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ps_endpoint_id'), 'ps_endpoint', ['id'], unique=False)
    op.create_table('ps_transports',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('async_operations', sa.Integer(), nullable=True),
    sa.Column('bind', sa.String(length=40), nullable=True),
    sa.Column('ca_list_file', sa.String(length=200), nullable=True),
    sa.Column('cert_file', sa.String(length=200), nullable=True),
    sa.Column('cipher', sa.String(length=200), nullable=True),
    sa.Column('domain', sa.String(length=40), nullable=True),
    sa.Column('external_media_address', sa.String(length=40), nullable=True),
    sa.Column('external_signaling_address', sa.String(length=40), nullable=True),
    sa.Column('external_signaling_port', sa.Integer(), nullable=True),
    sa.Column('method', sa.String(length=40), nullable=True),
    sa.Column('local_net', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=40), nullable=True),
    sa.Column('priv_key_file', sa.String(length=200), nullable=True),
    sa.Column('protocol', sa.String(length=40), nullable=True),
    sa.Column('require_client_cert', sa.String(length=40), nullable=True),
    sa.Column('verify_client', sa.String(length=40), nullable=True),
    sa.Column('verifiy_server', sa.String(length=40), nullable=True),
    sa.Column('tos', sa.String(length=40), nullable=True),
    sa.Column('cos', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bind', 'protocol', name='protocol_bind_unq')
    )
    op.create_index(op.f('ix_ps_transports_id'), 'ps_transports', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_ps_transports_id'), table_name='ps_transports')
    op.drop_table('ps_transports')
    op.drop_index(op.f('ix_ps_endpoint_id'), table_name='ps_endpoint')
    op.drop_table('ps_endpoint')
    op.drop_index(op.f('ix_ps_auth_id'), table_name='ps_auth')
    op.drop_table('ps_auth')
    op.drop_index(op.f('ix_ps_aors_id'), table_name='ps_aors')
    op.drop_table('ps_aors')
    op.drop_index(op.f('ix_extensions_id'), table_name='extensions')
    op.drop_table('extensions')
    # ### end Alembic commands ###