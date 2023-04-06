# default mongodb daemon stop.
systemctl stop mongod

#stop shard process
./stop_shard.sh

# remove data directory
if [ -d data ]; then
    rm -rf ./data
fi

# config server
mkdir -pv /shard/data/configdb
mkdir -pv /shard/data/logs
touch /shard/data/logs/configsvr.log

mongod --config /shard/mongodConfig.conf &
sleep 3s
mongo 192.168.1.54:27019 < rs.init

# router Server
touch /shard/data/logs/mongorouter.log

mongos --config /shard/mongodRouter.conf &
sleep 3s

# shard1 Sever
mkdir -pv /shard/data/shard1db
touch /shard/data/logs/shard1.log

mongod --config /shard/mongodShard1.conf &
sleep 2s
mongo 192.168.1.54:27021 < rs.init

# shard1 Sever
mkdir -pv /shard/data/shard2db
touch /shard/data/logs/shard2.log

mongod --config /shard/mongodShard2.conf &
sleep 2s
mongo 192.168.1.54:27022 < rs.init

# process status
ps -ef | grep mongo
sleep 2s

# netstatus
netstat -ntlp

# mongo 192.168.1.54:27017

mongo 192.168.1.54:27017 < rs.addShard 
