import cx_Oracle
import psycopg2

cx_Oracle.init_oracle_client(lib_dir="/Users/rrgayer/Downloads/instantclient_19_16")

print("Programa para copiar uma tabela Oracle para PostgreSQL")

oracle_conn_str = "rrgayer/Prud@123@localhost:1521/FREE"
pg_conn_str = "dbname='postgres' user='postgres' password='Prud@123' host='localhost' port='5432'"

oracle_query = "SELECT cd_produto, ds_produto, tx_produto FROM produto"
oracle_conn = cx_Oracle.connect(oracle_conn_str)
oracle_cursor = oracle_conn.cursor()

pg_conn = psycopg2.connect(pg_conn_str)
pg_cursor = pg_conn.cursor()

produtos = oracle_cursor.execute(oracle_query).fetchall()

for produto in produtos:
    cd_produto = produto[0]
    ds_produto = produto[1]
    tx_produto = produto[2].read()

    print(tx_produto)

    pg_cursor.execute("insert into produto (cd_produto, ds_produto, tx_produto) values (%s, %s, %s)",
                      (cd_produto, ds_produto, tx_produto))

    pg_cursor.execute("commit")

oracle_cursor.close()
oracle_conn.close()
