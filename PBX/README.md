##### Run the Asterisk container

docker run -d \
	--name PYPBX \
	-e POSTGRES_PASSWORD=PyPbX-secret \
    -e POSTGRES_USER=AsteriskPBX \
    -e POSTGRES_DB=PYPBX-RDB \
	--network Pydialer_bridge \
    asterisk18:latest

docker exec -it DB-PYPBX psql -U AsteriskPBX -d PYPBX-RDB -c "create database test_ast_rdb;"

docker exec -it DB-PYPBX psql -U AsteriskPBX -d test_ast_rdb

docker exec -it DB-PYPBX mkdir /asterisk/

docker cp ./postgresql/ PYPBX:/asterisk/

docker exec  DB-PYPBX psql -U AsteriskPBX -d test_ast_rdb -f /asterisk/postgresql/postgresql_config.sql

docker exec  DB-PYPBX psql -U AsteriskPBX -d test_ast_rdb -f /asterisk/postgresql/postgresql_cdr.sql

docker exec  DB-PYPBX psql -U AsteriskPBX -d test_ast_rdb -f /asterisk/postgresql/postgresql_voicemail.sql

