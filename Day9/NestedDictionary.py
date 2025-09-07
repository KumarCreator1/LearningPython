#   {
#     key: [list]
#     key2: {dictionary}
#   }


capital = {
    "france":"paris",
    "germany":"berlin",
}

#nesting a list
travel_log= {
    "france": ["paris","Lille","Dijon"],
    "germany": {"stuttgart","berlin"},
}

#print lille
print(travel_log["france"][1]) # accesing
print(travel_log["germany"])

nested_list=["A","B","C",["D","E"]]
print(nested_list[3][0])   # acess 2D list
    
travel_log= {
    "france": {
        "city_visited":["Parish","Lille","Dijon"],
        "no._of_visits":12
    },

    "germany": {
        "city_visited":["berlin","hamburg","stuttgart"],
        "total_visits":5
    },
}

#how to acces stuttgart
print(travel_log["germany"]["city_visited"][2])
