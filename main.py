import os
from neo4jclient import Neo4jClient,read_roles_hardcode







# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Connection credentials
    url = 'bolt://54.68.133.241:7687'
    username = os.environ.get('NEO4J_CENTRAL_USER')
    password = os.environ.get('NEO4J_CENTRAL_PASSWORD')
    database = 'system'

    neo4j = Neo4jClient(url=url,username=username,password=password,database=database)

    with neo4j.client.session() as session:
        result = session.execute_read(read_roles_hardcode)
        print('these are the results of our read query:')

        print(result)
        print('''



              ''')


        print('next we need to iterate over each procedure, do string interpolation to create the query, and run it against the database')
        for procedure in result:
            cypher_query = f'GRANT EXECUTE PROCEDURE {procedure} ON DBMS TO DataScienceUser'
            print(cypher_query)


















