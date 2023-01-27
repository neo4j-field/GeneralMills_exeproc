def read_roles_hardcode(tx):
    result = tx.run(query = '''
        SHOW PROCEDURES YIELD name 
        WHERE name =~ "^gds.*.fastRP.*" 
        OR name=~"^gds.*.graphSage.*" 
        OR name=~"^gds.*.node2vec.*" 
        OR name=~"^gds.*.nodeSimilarity.*" 
        OR name=~"^gds.*.nodeSimilarity.filtered.*" 
        OR name=~"^gds.*.knn.*" 
        OR name=~"^gds.*.knn.filtered.*"
        OR name=~"^gds.*.*.mutate"
        OR name=~"^gds.*.*.write"
        RETURN name''')

    return result.value()





























def read_roles(*args):
    '''
    Retrieves procedures from database
    :return:
    '''

    list_of_args = args

    first_arg = list_of_args[0]

    remaining_args = list_of_args[1:]


    query = f'SHOW PROCEDURES YIELD name WHERE name =~ {first_arg}'

    if len(remaining_args) > 0 & len(remaining_args) <= 1:

        remaining_where_conditions = 'OR name=~' + first_arg

        final_query = query + ' ' + remaining_where_conditions

        return final_query
    elif len(remaining_args) > 1:


        remaining_where_conditions = 'OR name=~'.join(remaining_args)
        final_query = query + ' ' + remaining_where_conditions + f'OR name=~{first_arg}'
        return final_query

    else:
        return query




