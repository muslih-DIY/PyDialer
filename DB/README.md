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