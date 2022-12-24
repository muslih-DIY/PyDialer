
from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM

enumvalue = lambda obj: [e.value for e in obj]


class ast_bool_values(str,Enum):
	low:str = '0'
	high:str = '1'
	off:str = 'off'
	on:str = 'on'
	false:str = 'false'
	true:str = 'true'
	no:str = 'no'
	yes:str = 'yes'

Sql_ast_bool_values = ENUM(
	ast_bool_values,
	name='ast_bool_values',
	create_type=True,
	values_callable=enumvalue
)

class iax_encryption_values(str,Enum):
	yes:str = 'yes'
	no:str = 'no'
	aes128:str = 'aes128'

Sql_iax_encryption_values = ENUM(
	iax_encryption_values,
	name='iax_encryption_values',
	create_type=True,
	values_callable=enumvalue
)

class iax_requirecalltoken_values(str,Enum):
	yes:str = 'yes'
	no:str = 'no'
	auto:str = 'auto'

Sql_iax_requirecalltoken_values = ENUM(
	iax_requirecalltoken_values,
	name='iax_requirecalltoken_values',
	create_type=True,
	values_callable=enumvalue
)

class iax_transfer_values(str,Enum):
	yes:str = 'yes'
	no:str = 'no'
	mediaonly:str = 'mediaonly'

Sql_iax_transfer_values = ENUM(
	iax_transfer_values,
	name='iax_transfer_values',
	create_type=True,
	values_callable=enumvalue
)

class moh_mode_values(str,Enum):
	custom:str = 'custom'
	files:str = 'files'
	mp3nb:str = 'mp3nb'
	quietmp3nb:str = 'quietmp3nb'
	quietmp3:str = 'quietmp3'
	playlist:str = 'playlist'

Sql_moh_mode_values = ENUM(
	moh_mode_values,
	name='moh_mode_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_100rel_values(str,Enum):
	no:str = 'no'
	required:str = 'required'
	yes:str = 'yes'

Sql_pjsip_100rel_values = ENUM(
	pjsip_100rel_values,
	name='pjsip_100rel_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_auth_type_values_v2(str,Enum):
	md5:str = 'md5'
	userpass:str = 'userpass'
	google_oauth:str = 'google_oauth'

Sql_pjsip_auth_type_values_v2 = ENUM(
	pjsip_auth_type_values_v2,
	name='pjsip_auth_type_values_v2',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_cid_privacy_values(str,Enum):
	allowed_not_screened:str = 'allowed_not_screened'
	allowed_passed_screened:str = 'allowed_passed_screened'
	allowed_failed_screened:str = 'allowed_failed_screened'
	allowed:str = 'allowed'
	prohib_not_screened:str = 'prohib_not_screened'
	prohib_passed_screened:str = 'prohib_passed_screened'
	prohib_failed_screened:str = 'prohib_failed_screened'
	prohib:str = 'prohib'
	unavailable:str = 'unavailable'

Sql_pjsip_cid_privacy_values = ENUM(
	pjsip_cid_privacy_values,
	name='pjsip_cid_privacy_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_connected_line_method_values(str,Enum):
	invite:str = 'invite'
	reinvite:str = 'reinvite'
	update:str = 'update'

Sql_pjsip_connected_line_method_values = ENUM(
	pjsip_connected_line_method_values,
	name='pjsip_connected_line_method_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_direct_media_glare_mitigation_values(str,Enum):
	none:str = 'none'
	outgoing:str = 'outgoing'
	incoming:str = 'incoming'

Sql_pjsip_direct_media_glare_mitigation_values = ENUM(
	pjsip_direct_media_glare_mitigation_values,
	name='pjsip_direct_media_glare_mitigation_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_dtls_setup_values(str,Enum):
	active:str = 'active'
	passive:str = 'passive'
	actpass:str = 'actpass'

Sql_pjsip_dtls_setup_values = ENUM(
	pjsip_dtls_setup_values,
	name='pjsip_dtls_setup_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_dtmf_mode_values_v3(str,Enum):
	rfc4733:str = 'rfc4733'
	inband:str = 'inband'
	info:str = 'info'
	auto:str = 'auto'
	auto_info:str = 'auto_info'

Sql_pjsip_dtmf_mode_values_v3 = ENUM(
	pjsip_dtmf_mode_values_v3,
	name='pjsip_dtmf_mode_values_v3',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_media_encryption_values(str,Enum):
	no:str = 'no'
	sdes:str = 'sdes'
	dtls:str = 'dtls'

Sql_pjsip_media_encryption_values = ENUM(
	pjsip_media_encryption_values,
	name='pjsip_media_encryption_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_redirect_method_values(str,Enum):
	user:str = 'user'
	uri_core:str = 'uri_core'
	uri_pjsip:str = 'uri_pjsip'

Sql_pjsip_redirect_method_values = ENUM(
	pjsip_redirect_method_values,
	name='pjsip_redirect_method_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_t38udptl_ec_values(str,Enum):
	none:str = 'none'
	fec:str = 'fec'
	redundancy:str = 'redundancy'

Sql_pjsip_t38udptl_ec_values = ENUM(
	pjsip_t38udptl_ec_values,
	name='pjsip_t38udptl_ec_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_taskprocessor_overload_trigger_values(str,Enum):
	none:str = 'none'
	Global:str = 'global'
	pjsip_only:str = 'pjsip_only'

Sql_pjsip_taskprocessor_overload_trigger_values = ENUM(
	pjsip_taskprocessor_overload_trigger_values,
	name='pjsip_taskprocessor_overload_trigger_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_timer_values(str,Enum):
	forced:str = 'forced'
	no:str = 'no'
	required:str = 'required'
	yes:str = 'yes'

Sql_pjsip_timer_values = ENUM(
	pjsip_timer_values,
	name='pjsip_timer_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_transport_method_values(str,Enum):
	default:str = 'default'
	unspecified:str = 'unspecified'
	tlsv1:str = 'tlsv1'
	sslv2:str = 'sslv2'
	sslv3:str = 'sslv3'
	sslv23:str = 'sslv23'

Sql_pjsip_transport_method_values = ENUM(
	pjsip_transport_method_values,
	name='pjsip_transport_method_values',
	create_type=True,
	values_callable=enumvalue
)

class pjsip_transport_protocol_values_v2(str,Enum):
	udp:str = 'udp'
	tcp:str = 'tcp'
	tls:str = 'tls'
	ws:str = 'ws'
	wss:str = 'wss'
	flow:str = 'flow'

Sql_pjsip_transport_protocol_values_v2 = ENUM(
	pjsip_transport_protocol_values_v2,
	name='pjsip_transport_protocol_values_v2',
	create_type=True,
	values_callable=enumvalue
)

class queue_autopause_values(str,Enum):
	yes:str = 'yes'
	no:str = 'no'
	all:str = 'all'

Sql_queue_autopause_values = ENUM(
	queue_autopause_values,
	name='queue_autopause_values',
	create_type=True,
	values_callable=enumvalue
)

class queue_strategy_values(str,Enum):
	ringall:str = 'ringall'
	leastrecent:str = 'leastrecent'
	fewestcalls:str = 'fewestcalls'
	random:str = 'random'
	rrmemory:str = 'rrmemory'
	linear:str = 'linear'
	wrandom:str = 'wrandom'
	rrordered:str = 'rrordered'

Sql_queue_strategy_values = ENUM(
	queue_strategy_values,
	name='queue_strategy_values',
	create_type=True,
	values_callable=enumvalue
)

class sha_hash_values(str,Enum):
	SHA1:str = 'SHA-1'
	SHA256:str = 'SHA-256'

Sql_sha_hash_values = ENUM(
	sha_hash_values,
	name='sha_hash_values',
	create_type=True,
	values_callable=enumvalue
)

class sip_callingpres_values(str,Enum):
	allowed_not_screened:str = 'allowed_not_screened'
	allowed_passed_screen:str = 'allowed_passed_screen'
	allowed_failed_screen:str = 'allowed_failed_screen'
	allowed:str = 'allowed'
	prohib_not_screened:str = 'prohib_not_screened'
	prohib_passed_screen:str = 'prohib_passed_screen'
	prohib_failed_screen:str = 'prohib_failed_screen'
	prohib:str = 'prohib'

Sql_sip_callingpres_values = ENUM(
	sip_callingpres_values,
	name='sip_callingpres_values',
	create_type=True,
	values_callable=enumvalue
)

class sip_directmedia_values_v2(str,Enum):
	yes:str = 'yes'
	no:str = 'no'
	nonat:str = 'nonat'
	update:str = 'update'
	outgoing:str = 'outgoing'

Sql_sip_directmedia_values_v2 = ENUM(
	sip_directmedia_values_v2,
	name='sip_directmedia_values_v2',
	create_type=True,
	values_callable=enumvalue
)

class sip_dtmfmode_values(str,Enum):
	rfc2833:str = 'rfc2833'
	info:str = 'info'
	shortinfo:str = 'shortinfo'
	inband:str = 'inband'
	auto:str = 'auto'

Sql_sip_dtmfmode_values = ENUM(
	sip_dtmfmode_values,
	name='sip_dtmfmode_values',
	create_type=True,
	values_callable=enumvalue
)

class sip_progressinband_values(str,Enum):
	yes:str = 'yes'
	no:str = 'no'
	never:str = 'never'

Sql_sip_progressinband_values = ENUM(
	sip_progressinband_values,
	name='sip_progressinband_values',
	create_type=True,
	values_callable=enumvalue
)

class sip_session_refresher_values(str,Enum):
	uac:str = 'uac'
	uas:str = 'uas'

Sql_sip_session_refresher_values = ENUM(
	sip_session_refresher_values,
	name='sip_session_refresher_values',
	create_type=True,
	values_callable=enumvalue
)

class sip_session_timers_values(str,Enum):
	accept:str = 'accept'
	refuse:str = 'refuse'
	originate:str = 'originate'

Sql_sip_session_timers_values = ENUM(
	sip_session_timers_values,
	name='sip_session_timers_values',
	create_type=True,
	values_callable=enumvalue
)

class sip_transport_values(str,Enum):
	udp:str = 'udp'
	tcp:str = 'tcp'
	tls:str = 'tls'
	ws:str = 'ws'
	wss:str = 'wss'
	udp_tcp:str = 'udp,tcp'
	tcp_udp:str = 'tcp,udp'

Sql_sip_transport_values = ENUM(
	sip_transport_values,
	name='sip_transport_values',
	create_type=True,
	values_callable=enumvalue
)

class type_values(str,Enum):
	friend:str = 'friend'
	user:str = 'user'
	peer:str = 'peer'

Sql_type_values = ENUM(
	type_values,
	name='type_values',
	create_type=True,
	values_callable=enumvalue
)

class yes_no_values(str,Enum):
	yes:str = 'yes'
	no:str = 'no'

Sql_yes_no_values = ENUM(
	yes_no_values,
	name='yes_no_values',
	create_type=True,
	values_callable=enumvalue
)

class yesno_values(str,Enum):
	yes:str = 'yes'
	no:str = 'no'

Sql_yesno_values = ENUM(
	yesno_values,
	name='yesno_values',
	create_type=True,
	values_callable=enumvalue
)
