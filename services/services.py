from services.parse_liquipedia import parse,matches
from services.converter import actualy_matches,convert_mathes
def all_matches_message():
    all_mathes = ''
    parse()
    convert_mathes()
    for i in actualy_matches.keys():
        all_mathes += i+'\n'
    if all_mathes:
         return all_mathes
    print(all_mathes,actualy_matches)
    return 'В ближайшее врямя официальных матчей не намечается :('