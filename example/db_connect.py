from sqlalchemy import create_engine
from sqlalchemy_prometheus import track

from prometheus_metrics import POSTGRES_CHECKEDOUT_CONNECTIONS, POSTGRES_CHECKEDIN_CONNECTIONS, \
    POSTGRES_TOTAL_CONNECTIONS, POSTGRES_DETACHED_CONNECTIONS, POSTGRES_CHECKOUTS_COUNT, POSTGRES_INVALIDATED_COUNT, \
    POSTGRES_CONNECTS_COUNT, POSTGRES_DISCONNECTS_COUNT

connection_str = 'postgres://postgres@localhost:5432/postgres'
service_name = 'my_app'

engine = create_engine(connection_str)
track.track_database(engine, service_name,
                     checkedout_connections_metric=POSTGRES_CHECKEDOUT_CONNECTIONS,
                     checkedin_connections_metric=POSTGRES_CHECKEDIN_CONNECTIONS,
                     total_connections_metric=POSTGRES_TOTAL_CONNECTIONS,
                     detached_connections_metric=POSTGRES_DETACHED_CONNECTIONS,
                     checkouts_count_metric=POSTGRES_CHECKOUTS_COUNT,
                     invalidated_count_metric=POSTGRES_INVALIDATED_COUNT,
                     connects_count_metric=POSTGRES_CONNECTS_COUNT,
                     disconnects_count_metric=POSTGRES_DISCONNECTS_COUNT,
                     )
