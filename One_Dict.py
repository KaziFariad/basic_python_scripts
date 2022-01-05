def one_dict(list_dict):
    print(list_dict)
    print()
    keys = list_dict[0].keys()
    print("Keys are:", keys)
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


nba_teams = [{'id': 1610612737,
              'full_name': 'Atlanta Hawks',
              'abbreviation': 'ATL',
              'nickname': 'Hawks',
              'city': 'Atlanta',
              'state': 'Atlanta',
              'year_founded': 1949},
             {'id': 1610612738,
              'full_name': 'Boston Celtics',
              'abbreviation': 'BOS',
              'nickname': 'Celtics',
              'city': 'Boston',
              'state': 'Massachusetts',
              'year_founded': 1946},
             {'id': 1610612739,
              'full_name': 'Cleveland Cavaliers',
              'abbreviation': 'CLE',
              'nickname': 'Cavaliers',
              'city': 'Cleveland',
              'state': 'Ohio',
              'year_founded': 1970}]


print(one_dict(nba_teams))
