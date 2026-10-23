import pandas as pd 
import numpy as np

#high school match logs
match_logs = [
    #barnegat vs henry hudson
    {"date": "8/25", "team_a": "Barnegat", "team_b": "Henry Hudson", "flight": "1S", "winner": "Henry Hudson", "score": "7-6(6), 4-6, 10-5"},
    {"date": "8/25", "team_a": "Barnegat", "team_b": "Henry Hudson", "flight": "2S", "winner": "Henry Hudson", "score": "7-6(4), 4-6, 15-13"},
    {"date": "8/25", "team_a": "Barnegat", "team_b": "Henry Hudson", "flight": "3S", "winner": "Henry Hudson", "score": "6-4, 6-1"},
    {"date": "8/25", "team_a": "Barnegat", "team_b": "Henry Hudson", "flight": "1D", "winner": "Henry Hudson", "score": "6-0, 6-4"},
    {"date": "8/25", "team_a": "Barnegat", "team_b": "Henry Hudson", "flight": "2D", "winner": "Henry Hudson", "score": "6-4, 6-4"},

    #barnegat vs toms river north    
    {"date": "8/26", "team_a": "Barnegat", "team_b": "Toms River North", "flight": "1S", "winner": "Toms River North", "score": "6-1, 6-0"},
    {"date": "8/26", "team_a": "Barnegat", "team_b": "Toms River North", "flight": "2S", "winner": "Toms River North", "score": "7-6(4), 6-2"},
    {"date": "8/26", "team_a": "Barnegat", "team_b": "Toms River North", "flight": "3S", "winner": "Barnegat", "score": "7-5, 7-6(4)"},
    {"date": "8/26", "team_a": "Barnegat", "team_b": "Toms River North", "flight": "1D", "winner": "Toms River North", "score": "7-6(6), 6-4"},
    {"date": "8/26", "team_a": "Barnegat", "team_b": "Toms River North", "flight": "2D", "winner": "Toms River North", "score": "3-6, 6-2, 14-12"},

    #barnegat vs pt pleasant beach
    {"date": "8/31", "team_a": "Barnegat", "team_b": "Point Pleasant Beach", "flight": "1S", "winner": "Barnegat", "score": "6-3, 6-1"},
    {"date": "8/31", "team_a": "Barnegat", "team_b": "Point Pleasant Beach", "flight": "2S", "winner": "Barnegat", "score": "6-2, 1-6, 10-6"},
    {"date": "8/31", "team_a": "Barnegat", "team_b": "Point Pleasant Beach", "flight": "3S", "winner": "Barnegat", "score": "6-1, 6-1"},
    {"date": "8/31", "team_a": "Barnegat", "team_b": "Point Pleasant Beach", "flight": "1D", "winner": "Barnegat", "score": "6-2, 6-3"},
    {"date": "8/31", "team_a": "Barnegat", "team_b": "Point Pleasant Beach", "flight": "2D", "winner": "Point Pleasant Beach", "score": "6-3, 6-4"},

    #barnegat vs freehold twp
    {"date": "9/1", "team_a": "Barnegat", "team_b": "Freehold Township", "flight": "1S", "winner": "Freehold Township", "score": "6-0, 6-0"},
    {"date": "9/1", "team_a": "Barnegat", "team_b": "Freehold Township", "flight": "2S", "winner": "Freehold Township", "score": "6-0, 6-0"},
    {"date": "9/1", "team_a": "Barnegat", "team_b": "Freehold Township", "flight": "3S", "winner": "Freehold Township", "score": "6-0, 6-0"},
    {"date": "9/1", "team_a": "Barnegat", "team_b": "Freehold Township", "flight": "1D", "winner": "Freehold Township", "score": "6-1, 6-3"},
    {"date": "9/1", "team_a": "Barnegat", "team_b": "Freehold Township", "flight": "2D", "winner": "Freehold Township", "score": "6-2, 6-0"},

    #barnegat vs pinelands
    {"date": "9/3", "team_a": "Barnegat", "team_b": "Pinelands", "flight": "1S", "winner": "Pinelands", "score": "6-0, 6-0"},
    {"date": "9/3", "team_a": "Barnegat", "team_b": "Pinelands", "flight": "2S", "winner": "Pinelands", "score": "6-0, 6-0"},
    {"date": "9/3", "team_a": "Barnegat", "team_b": "Pinelands", "flight": "3S", "winner": "Pinelands", "score": "6-0, 6-2"},
    {"date": "9/3", "team_a": "Barnegat", "team_b": "Pinelands", "flight": "1D", "winner": "Pinelands", "score": "6-4, 6-2"},
    {"date": "9/3", "team_a": "Barnegat", "team_b": "Pinelands", "flight": "2D", "winner": "Pinelands", "score": "6-0, 6-0"},

    #neptune vs henry hudson
    {"date": "8/28", "team_a": "Neptune", "team_b": "Henry Hudson", "flight": "1S", "winner": "Henry Hudson", "score": "6-1, 6-2"},
    {"date": "8/28", "team_a": "Neptune", "team_b": "Henry Hudson", "flight": "2S", "winner": "Henry Hudson", "score": "6-0, 6-1"},
    {"date": "8/28", "team_a": "Neptune", "team_b": "Henry Hudson", "flight": "3S", "winner": "Henry Hudson", "score": "6-0, 6-0"},
    {"date": "8/28", "team_a": "Neptune", "team_b": "Henry Hudson", "flight": "1D", "winner": "Henry Hudson", "score": "6-0, 6-0"},
    {"date": "8/28", "team_a": "Neptune", "team_b": "Henry Hudson", "flight": "2D", "winner": "Henry Hudson", "score": "6-1, 6-0"},

    #brick memorial vs central
    {"date": "8/25", "team_a": "Brick Memorial", "team_b": "Central", "flight": "1S", "winner": "Brick Memorial", "score": "7-6(3), 6-1"},
    {"date": "8/25", "team_a": "Brick Memorial", "team_b": "Central", "flight": "2S", "winner": "Brick Memorial", "score": "6-2, 6-0"},
    {"date": "8/25", "team_a": "Brick Memorial", "team_b": "Central", "flight": "3S", "winner": "Brick Memorial", "score": "6-4, 6-1"},
    {"date": "8/25", "team_a": "Brick Memorial", "team_b": "Central", "flight": "1D", "winner": "Central", "score": "6-2, 6-4"},
    {"date": "8/25", "team_a": "Brick Memorial", "team_b": "Central", "flight": "2D", "winner": "Central", "score": "6-4, 6-4"},

    #brick memorial vs freehold boro
    {"date": "8/27", "team_a": "Brick Memorial", "team_b": "Freehold Borough", "flight": "1S", "winner": "Freehold Borough", "score": "6-2, 6-0"},
    {"date": "8/27", "team_a": "Brick Memorial", "team_b": "Freehold Borough", "flight": "2S", "winner": "Brick Memorial", "score": "6-4, 6-0"},
    {"date": "8/27", "team_a": "Brick Memorial", "team_b": "Freehold Borough", "flight": "3S", "winner": "Freehold Borough", "score": "7-6(1), 6-3"},
    {"date": "8/27", "team_a": "Brick Memorial", "team_b": "Freehold Borough", "flight": "1D", "winner": "Brick Memorial", "score": "6-3, 6-3"},
    {"date": "8/27", "team_a": "Brick Memorial", "team_b": "Freehold Borough", "flight": "2D", "winner": "Freehold Borough", "score": "6-1, 6-0"},

    #brick memorial vs howell
    {"date": "9/3", "team_a": "Brick Memorial", "team_b": "Howell", "flight": "1S", "winner": "Howell", "score": "6-1, 6-1"},
    {"date": "9/3", "team_a": "Brick Memorial", "team_b": "Howell", "flight": "2S", "winner": "Brick Memorial", "score": "6-2, 6-1"},
    {"date": "9/3", "team_a": "Brick Memorial", "team_b": "Howell", "flight": "3S", "winner": "Howell", "score": "Forfeit"},
    {"date": "9/3", "team_a": "Brick Memorial", "team_b": "Howell", "flight": "1D", "winner": "Howell", "score": "6-4, 6-4"},
    {"date": "9/3", "team_a": "Brick Memorial", "team_b": "Howell", "flight": "2D", "winner": "Howell", "score": "6-1, 7-6(2)"},

    #brick memorial vs toms river south
    {"date": "9/9", "team_a": "Brick Memorial", "team_b": "Toms River South", "flight": "1S", "winner": "Brick Memorial", "score": "6-1, 7-5"},
    {"date": "9/9", "team_a": "Brick Memorial", "team_b": "Toms River South", "flight": "2S", "winner": "Brick Memorial", "score": "6-1, 6-0"},
    {"date": "9/9", "team_a": "Brick Memorial", "team_b": "Toms River South", "flight": "3S", "winner": "Toms River South", "score": "7-5, 6-0"},
    {"date": "9/9", "team_a": "Brick Memorial", "team_b": "Toms River South", "flight": "1D", "winner": "Toms River South", "score": "4-6, 6-1, 10-3"},
    {"date": "9/9", "team_a": "Brick Memorial", "team_b": "Toms River South", "flight": "2D", "winner": "Toms River South", "score": "6-2, 6-0"},

    #brick township vs new egypt
    {"date": "9/9", "team_a": "Brick Township", "team_b": "New Egypt", "flight": "1S", "winner": "Brick Township", "score": "6-3, 6-0"},
    {"date": "9/9", "team_a": "Brick Township", "team_b": "New Egypt", "flight": "2S", "winner": "Brick Township", "score": "6-1, 6-1"},
    {"date": "9/9", "team_a": "Brick Township", "team_b": "New Egypt", "flight": "3S", "winner": "Brick Township", "score": "6-1, 6-2"},
    {"date": "9/9", "team_a": "Brick Township", "team_b": "New Egypt", "flight": "1D", "winner": "Brick Township", "score": "6-0, 6-2"},
    {"date": "9/9", "team_a": "Brick Township", "team_b": "New Egypt", "flight": "2D", "winner": "New Egypt", "score": "7-5, 6-4"},

    #brick township vs pinelands
    {"date": "9/10", "team_a": "Brick Township", "team_b": "Pinelands", "flight": "1S", "winner": "Pinelands", "score": "7-6(4), 6-2"},
    {"date": "9/10", "team_a": "Brick Township", "team_b": "Pinelands", "flight": "2S", "winner": "Pinelands", "score": "6-3, 6-4"},
    {"date": "9/10", "team_a": "Brick Township", "team_b": "Pinelands", "flight": "3S", "winner": "Pinelands", "score": "6-0, 6-0"},
    {"date": "9/10", "team_a": "Brick Township", "team_b": "Pinelands", "flight": "1D", "winner": "Pinelands", "score": "6-1, 6-1"},
    {"date": "9/10", "team_a": "Brick Township", "team_b": "Pinelands", "flight": "2D", "winner": "Pinelands", "score": "6-2, 6-1"},

    #brick township vs neptune
    {"date": "9/11", "team_a": "Brick Township", "team_b": "Neptune", "flight": "1S", "winner": "Brick Township", "score": "6-0, 6-0"},
    {"date": "9/11", "team_a": "Brick Township", "team_b": "Neptune", "flight": "2S", "winner": "Brick Township", "score": "6-1, 6-0"},
    {"date": "9/11", "team_a": "Brick Township", "team_b": "Neptune", "flight": "3S", "winner": "Brick Township", "score": "6-1, 6-0"},
    {"date": "9/11", "team_a": "Brick Township", "team_b": "Neptune", "flight": "1D", "winner": "Brick Township", "score": "6-2, 6-0"},
    {"date": "9/11", "team_a": "Brick Township", "team_b": "Neptune", "flight": "2D", "winner": "Brick Township", "score": "6-2, 6-0"}, 

    #lakewoood vs new egypt
    {"date": "9/11", "team_a": "Lakewood", "team_b": "New Egypt", "flight": "1S", "winner": "New Egypt", "score": "6-0, 6-0"},
    {"date": "9/11", "team_a": "Lakewood", "team_b": "New Egypt", "flight": "2S", "winner": "New Egypt", "score": "2-6, 7-6(12), 10-5"},
    {"date": "9/11", "team_a": "Lakewood", "team_b": "New Egypt", "flight": "3S", "winner": "New Egypt", "score": "7-5, 6-3"},
    {"date": "9/11", "team_a": "Lakewood", "team_b": "New Egypt", "flight": "1D", "winner": "New Egypt", "score": "6-1, 6-1"},
    {"date": "9/11", "team_a": "Lakewood", "team_b": "New Egypt", "flight": "2D", "winner": "New Egypt", "score": "6-1, 6-1"}, 

    #toms river south vs central
    {"date": "8/31", "team_a": "Toms River South", "team_b": "Central", "flight": "1S", "winner": "Toms River South", "score": "6-3, 6-0"},
    {"date": "8/31", "team_a": "Toms River South", "team_b": "Central", "flight": "2S", "winner": "Toms River South", "score": "6-3, 6-1"},
    {"date": "8/31", "team_a": "Toms River South", "team_b": "Central", "flight": "3S", "winner": "Toms River South", "score": "6-2, 6-3"},
    {"date": "8/31", "team_a": "Toms River South", "team_b": "Central", "flight": "1D", "winner": "Central", "score": "6-1, 1-6"},
    {"date": "8/31", "team_a": "Toms River South", "team_b": "Central", "flight": "2D", "winner": "Central", "score": "6-2, 6-3"},

    #toms river south vs toms river east
    {"date": "9/3", "team_a": "Toms River South", "team_b": "Toms River East", "flight": "1S", "winner": "Toms River East", "score": "6-0, 6-0"},
    {"date": "9/3", "team_a": "Toms River South", "team_b": "Toms River East", "flight": "2S", "winner": "Toms River East", "score": "6-2, 6-1"},
    {"date": "9/3", "team_a": "Toms River South", "team_b": "Toms River East", "flight": "3S", "winner": "Toms River East", "score": "6-2, 6-0"},
    {"date": "9/3", "team_a": "Toms River South", "team_b": "Toms River East", "flight": "1D", "winner": "Toms River South", "score": "6-2, 1-6, 10-5"},
    {"date": "9/3", "team_a": "Toms River South", "team_b": "Toms River East", "flight": "2D", "winner": "Toms River South", "score": "6-4, 6-2"},

    #new egypt vs pinelands
    {"date": "8/31", "team_a": "New Egypt", "team_b": "Pinelands", "flight": "1S", "winner": "Pinelands", "score": "7-5, 6-3"},
    {"date": "8/31", "team_a": "New Egypt", "team_b": "Pinelands", "flight": "2S", "winner": "Pinelands", "score": "6-2, 6-0"},
    {"date": "8/31", "team_a": "New Egypt", "team_b": "Pinelands", "flight": "3S", "winner": "Pinelands", "score": "6-0, 6-0"},
    {"date": "8/31", "team_a": "New Egypt", "team_b": "Pinelands", "flight": "1D", "winner": "Pinelands", "score": "6-0, 6-0"},
    {"date": "8/31", "team_a": "New Egypt", "team_b": "Pinelands", "flight": "2D", "winner": "Pinelands", "score": "6-0, 6-0"},

    #pt pleasant beach vs central
    {"date": "9/2", "team_a": "Point Pleasant Beach", "team_b": "Central", "flight": "1S", "winner": "Point Pleasant Beach", "score": "6-1, Retired"},
    {"date": "9/2", "team_a": "Point Pleasant Beach", "team_b": "Central", "flight": "2S", "winner": "Point Pleasant Beach", "score": "6-3, 7-5"},
    {"date": "9/2", "team_a": "Point Pleasant Beach", "team_b": "Central", "flight": "3S", "winner": "Central", "score": "6-1, 6-1"},
    {"date": "9/2", "team_a": "Point Pleasant Beach", "team_b": "Central", "flight": "1D", "winner": "Central", "score": "6-0, 6-1"},
    {"date": "9/2", "team_a": "Point Pleasant Beach", "team_b": "Central", "flight": "2D", "winner": "Central", "score": "6-0, 6-1"},

    #lacey vs freehold boro
    {"date": "8/25", "team_a": "Lacey", "team_b": "Freehold Borough", "flight": "1S", "winner": "Freehold Borough", "score": "6-1, 6-0"},
    {"date": "8/25", "team_a": "Lacey", "team_b": "Freehold Borough", "flight": "2S", "winner": "Lacey", "score": "7-6(4), 6-2"},
    {"date": "8/25", "team_a": "Lacey", "team_b": "Freehold Borough", "flight": "3S", "winner": "Freehold Borough", "score": "7-5, 7-6(4)"},
    {"date": "8/25", "team_a": "Lacey", "team_b": "Freehold Borough", "flight": "1D", "winner": "Lacey", "score": "7-6(6), 6-4"},
    {"date": "8/25", "team_a": "Lacey", "team_b": "Freehold Borough", "flight": "2D", "winner": "Lacey", "score": "3-6, 6-2, 14-12"},

    #central vs toms river north
    {"date": "8/27", "team_a": "Central", "team_b": "Toms River North", "flight": "1S", "winner": "Toms River North", "score": "6-1, 6-0"},
    {"date": "8/27", "team_a": "Central", "team_b": "Toms River North", "flight": "2S", "winner": "Toms River North", "score": "6-2, 6-1"},
    {"date": "8/27", "team_a": "Central", "team_b": "Toms River North", "flight": "3S", "winner": "Central", "score": "7-5, 6-2"},
    {"date": "8/27", "team_a": "Central", "team_b": "Toms River North", "flight": "1D", "winner": "Central", "score": "6-0, 6-2"},
    {"date": "8/27", "team_a": "Central", "team_b": "Toms River North", "flight": "2D", "winner": "Central", "score": "6-0, 6-2"},

    #central vs pinelands
    {"date": "9/4", "team_a": "Central", "team_b": "Pinelands", "flight": "1S", "winner": "Central", "score": "6-2, 4-6, 10-8"},
    {"date": "9/4", "team_a": "Central", "team_b": "Pinelands", "flight": "2S", "winner": "Pinelands", "score": "6-0, 6-2"},
    {"date": "9/4", "team_a": "Central", "team_b": "Pinelands", "flight": "3S", "winner": "Pinelands", "score": "6-0, 6-1"},
    {"date": "9/4", "team_a": "Central", "team_b": "Pinelands", "flight": "1D", "winner": "Pinelands", "score": "7-5, 6(7)-7, 10-8"},
    {"date": "9/4", "team_a": "Central", "team_b": "Pinelands", "flight": "2D", "winner": "Pinelands", "score": "3-6, 6-4, 13-11"},

    #matawan vs ocean twp
    {"date": "9/3", "team_a": "Matawan", "team_b": "Ocean Township", "flight": "1S", "winner": "Matawan", "score": "7-5, 6-3"},
    {"date": "9/3", "team_a": "Matawan", "team_b": "Ocean Township", "flight": "2S", "winner": "Ocean Township", "score": "6-3, 6-1"},
    {"date": "9/3", "team_a": "Matawan", "team_b": "Ocean Township", "flight": "3S", "winner": "Ocean Township", "score": "7-6(4), 6-4"},
    {"date": "9/3", "team_a": "Matawan", "team_b": "Ocean Township", "flight": "1D", "winner": "Ocean Township", "score": "6-2, 6-1"},
    {"date": "9/3", "team_a": "Matawan", "team_b": "Ocean Township", "flight": "2D", "winner": "Ocean Township", "score": "6-1, 6-2"},

    #ocean twp vs long branch
    {"date": "9/4", "team_a": "Ocean Township", "team_b": "Long Branch", "flight": "1S", "winner": "Ocean Township", "score": "6-2, 6-0"},
    {"date": "9/4", "team_a": "Ocean Township", "team_b": "Long Branch", "flight": "2S", "winner": "Ocean Township", "score": "6-0, 6-0"},
    {"date": "9/4", "team_a": "Ocean Township", "team_b": "Long Branch", "flight": "3S", "winner": "Ocean Township", "score": "6-0, 6-0"},
    {"date": "9/4", "team_a": "Ocean Township", "team_b": "Long Branch", "flight": "1D", "winner": "Ocean Township", "score": "6-0, 6-0"},
    {"date": "9/4", "team_a": "Ocean Township", "team_b": "Long Branch", "flight": "2D", "winner": "Ocean Township", "score": "6-0, 6-0"},

    #us vs barnegat
    {"date": "8/28", "team_a": "Manchester", "team_b": "Barnegat", "flight": "1S", "winner": "Manchester", "score": "6-0, 6-0"},
    {"date": "8/28", "team_a": "Manchester", "team_b": "Barnegat", "flight": "2S", "winner": "Barnegat", "score": "6-2, 6-4"},
    {"date": "8/28", "team_a": "Manchester", "team_b": "Barnegat", "flight": "3S", "winner": "Manchester", "score": "6-1, 6-0"},
    {"date": "8/28", "team_a": "Manchester", "team_b": "Barnegat", "flight": "1D", "winner": "Barnegat", "score": "3-6, 7-5, 12-10"},
    {"date": "8/28", "team_a": "Manchester", "team_b": "Barnegat", "flight": "2D", "winner": "Manchester", "score": "6-1, 6-1"},

    #us vs neptune
    {"date": "9/4", "team_a": "Manchester", "team_b": "Neptune", "flight": "1S", "winner": "Manchester", "score": "6-0, 6-0"},
    {"date": "9/4", "team_a": "Manchester", "team_b": "Neptune", "flight": "2S", "winner": "Manchester", "score": "6-0, 6-1"},
    {"date": "9/4", "team_a": "Manchester", "team_b": "Neptune", "flight": "3S", "winner": "Manchester", "score": "6-0, 6-0"},
    {"date": "9/4", "team_a": "Manchester", "team_b": "Neptune", "flight": "1D", "winner": "Manchester", "score": "6-2, 6-2"},
    {"date": "9/4", "team_a": "Manchester", "team_b": "Neptune", "flight": "2D", "winner": "Manchester", "score": "6-0, 6-2"},

    #us vs brick memorial
    {"date": "9/4", "team_a": "Manchester", "team_b": "Brick Memorial", "flight": "1S", "winner": "Manchester", "score": "6-4, 6-3"},
    {"date": "9/4", "team_a": "Manchester", "team_b": "Brick Memorial", "flight": "2S", "winner": "Manchester", "score": "6-0, 6-1"},
    {"date": "9/4", "team_a": "Manchester", "team_b": "Brick Memorial", "flight": "3S", "winner": "Manchester", "score": "6-1, 6-1"},
    {"date": "9/4", "team_a": "Manchester", "team_b": "Brick Memorial", "flight": "1D", "winner": "Brick Memorial", "score": "6-3, 6-2"},
    {"date": "9/4", "team_a": "Manchester", "team_b": "Brick Memorial", "flight": "2D", "winner": "Brick Memorial", "score": "6-2, 6-3"},
]


df = pd.DataFrame(match_logs)

print("\n--- ALL MATCH RESULTS ---") 
print(df.to_string(index=False)) 

#MATCHES PLAYED PER TEAM 
print("\n--- MATCHES PLAYED PER TEAM (RAW SLOTS) ---") 
print(df["team_a"].value_counts()) 

#ACTUAL DUAL MATCHES PLAYED PER TEAM 
all_teams = pd.concat([df["team_a"], df["team_b"]]) 
print("\n--- ACTUAL DUAL MATCHES PLAYED PER TEAM ---") 
print(all_teams.value_counts()) 

#OVERALL DUAL MATCH STANDINGS 
dual_results = [] 

for (date, team_a, team_b), group in df.groupby(["date", "team_a", "team_b"]): 
    team_a_wins = (group["winner"] == team_a).sum() 
    team_b_wins = (group["winner"] == team_b).sum() 

    if team_a_wins > team_b_wins: dual_results.append({"Winner": team_a, "Loser": team_b}) 
    elif team_b_wins > team_a_wins: dual_results.append({"Winner": team_b, "Loser": team_a}) 

dual_df = pd.DataFrame(dual_results) 

#WINS AND LOSSES PER TEAM 
wins = dual_df["Winner"].value_counts() 
losses = dual_df["Loser"].value_counts() 

unique_teams = all_teams.unique() 
standings = pd.DataFrame(index=unique_teams) 

standings["Wins"] = standings.index.map(wins).fillna(0).astype(int) 
standings["Losses"] = standings.index.map(losses).fillna(0).astype(int) 

total_duals = standings["Wins"] + standings["Losses"] 
standings["Win %"] = np.where( 
    total_duals > 0, (standings["Wins"] / total_duals * 100).round(1), 0.0 
) 

#SORT STANDINGS 
standings = standings.sort_values(by=["Wins", "Win %"], ascending=False) 
print("\n--- TEAM DUAL MATCH STANDINGS ---") 
print(standings.to_string()) 

#WINS BY FLIGHT SLOT 
print("\n--- WINS BY FLIGHT SLOT ---") 
flight_piv = pd.crosstab(df["flight"], df["winner"]) 
print(flight_piv) 
print(f"\nTotal individual player match slots recorded: {len(df)}")

#TIEBREAK MATCHES FILTER 
tiebreak_pattern = r"7-6|\b1[0-9]-\d+\b|\b20-\d+\b" 
tiebreak_matches = df[
    df["score"].str.contains(tiebreak_pattern, regex=True, na=False) 
] 

print("\n--- TIEBREAK MATCHES ---") 
print(tiebreak_matches.to_string(index=False))

division_teams = [
    "Manchester",
    "Neptune",
    "Brick Memorial",
    "Brick Township",
    "Toms River South",
    "New Egypt",
    "Lakewood",
    "Point Pleasant Beach"
]

#ONLY DIVISION TEAMS
df_div = df[df["team_a"].isin(division_teams) | df["team_b"].isin(division_teams)]

#DUAL MATCHES
dual_results_div = []

for (date, team_a, team_b), group in df_div.groupby(["date", "team_a", "team_b"]):
    team_a_wins = (group["winner"] == team_a).sum()
    team_b_wins = (group["winner"] == team_b).sum()

    if team_a_wins > team_b_wins:
        dual_results_div.append({"Winner": team_a, "Loser": team_b})
    elif team_b_wins > team_a_wins:
        dual_results_div.append({"Winner": team_b, "Loser": team_a})

dual_df_div = pd.DataFrame(dual_results_div)

#WINS AND LOSSES
wins_div = dual_df_div["Winner"].value_counts()
losses_div = dual_df_div["Loser"].value_counts()

#STANDINGS TABLE
standings_div = pd.DataFrame(index=division_teams)
standings_div["Wins"] = standings_div.index.map(wins_div).fillna(0).astype(int)
standings_div["Losses"] = standings_div.index.map(losses_div).fillna(0).astype(int)

total_duals = standings_div["Wins"] + standings_div["Losses"]
standings_div["Win %"] = (standings_div["Wins"] / total_duals.replace(0, 1) * 100).round(1)

#SORT
standings_div = standings_div.sort_values(by=["Wins", "Win %"], ascending=False)

print("\n--- DIVISION STANDINGS ---")
print(standings_div.to_string())

#COMPARISON TABLE
manchester = "Manchester"
comparison_rows = []

for team in division_teams:
    if team == manchester:
        continue

    h2h = dual_df_div[
        ((dual_df_div["Winner"] == manchester) & (dual_df_div["Loser"] == team)) |
        ((dual_df_div["Winner"] == team) & (dual_df_div["Loser"] == manchester))
    ]

    if len(h2h) > 0:
        result = "Manchester won" if h2h.iloc[0]["Winner"] == manchester else "Manchester lost"
    else:
        result = "No match yet"

    comparison_rows.append({
        "Opponent": team,
        "Manchester Result": result,
        "Opponent Wins": standings_div.loc[team, "Wins"],
        "Opponent Losses": standings_div.loc[team, "Losses"],
        "Opponent Win %": standings_div.loc[team, "Win %"]
    })

comparison_df = pd.DataFrame(comparison_rows)

print("\n--- MANCHESTER VS DIVISION TEAMS ---")
print(comparison_df.to_string(index=False))