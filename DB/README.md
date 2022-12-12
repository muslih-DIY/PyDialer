##### Run the postgres container

docker run -d \
	--name DB-PYPBX \
	-e POSTGRES_PASSWORD=PyPbX-secret \
    -e POSTGRES_USER=AsteriskPBX \
    -e POSTGRES_DB=PYPBX-RDB \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /PYPBX/pgdata:/var/lib/postgresql/data \
	--network Pydialer_bridge
    postgres:14.4-bullseye



docker exec -it DB-PYPBX psql -U AsteriskPBX -d PYPBX-RDB

docker exec -it DB-PYPBX psql -U AsteriskPBX -d PYPBX-RDB -c "create database test_ast_rdb;"

docker exec -it DB-PYPBX psql -U AsteriskPBX -d test_ast_rdb

docker exec -it DB-PYPBX mkdir /asterisk/


docker exec -it DB-PYPBX pg_dump -U AsteriskPBX -d test_ast_rdb 