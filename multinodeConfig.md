Cassandra Multinode

cassandra-env.sh file

Error: CassandraDaemon.java:731 Cannot start node if snitch's data center (del) differs from previous data
center (datacenter1)

JVM_OPTS="$JVM_OPTS -Dcassandra.ignore_dc-true"
JVM_OPTS="$JVM_OPTS -Deassandra.ignore_rack-true"


cassandra.yaml filo
1. - seeds: "172.31.27.170, 172.31.24.115,172.31.24.138"
2. listen address: 172.31.24.130
3. endpoint snitch: Rackinferringsnitch

bin/cassandra -f
Type and
nodetool status
nodetool -h localhost getendpoints <keyspaceName> <tableName> <key>

bin/eqish