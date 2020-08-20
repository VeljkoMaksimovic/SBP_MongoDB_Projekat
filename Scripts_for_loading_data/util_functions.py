import re


def get_queries(file_path):
    with open(file_path, 'r') as f:
        file_string = f.read().replace('\n', '').replace('\t', '')
    #queries = file_string.split('aggregate(')
    #queries = [i.split(').pretty()')[0] for i in queries[1:]]
    queries = re.findall('aggregate\(((?!\)).)*\)', file_string)
    # this next part is for removing comments
    for i in range(len(queries)):
        queries[i] = re.sub('//((?!{).)*{', '{', queries[i])
    return queries


if __name__ == '__main__':
    qs = get_queries('../aggregations_v1_players_inside_array')
    print(qs[-1])
