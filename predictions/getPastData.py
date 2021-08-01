# Only 1 year and 1 term can be inputed at a time.
# Any number of weeks/time periods can be entterred
# There must be an equal number of time periods for each day
# There must be 5 days

def getPastData():
    #Stub

    """
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    term = Column(Integer, nullable=False)
    week = Column(Integer, nullable=False)
    time = Column(String(10), nullable=False)
    jnrcount = Column(Integer, nullable=False)
    snrcount = Column(Integer, nullable=False)
    """

    data = [  [1,1,1,2021,1,1,"8:30",26,59],
            [2,1,1,2021,1,1,"8:35",28,16],
            [3,1,1,2021,1,1,"8:40",28,31],
            [4,1,1,2021,1,1,"8:45",50,53],
            [5,1,1,2021,1,1,"8:50",26,39],
            [6,1,1,2021,1,1,"8:55",58,58],
            [7,1,1,2021,1,2,"8:30",13,30],
            [8,1,1,2021,1,2,"8:35",18,27],
            [9,1,1,2021,1,2,"8:40",11,53],
            [10,1,1,2021,1,2,"8:45",32,14],
            [11,1,1,2021,1,2,"8:50",54,14],
            [12,1,1,2021,1,2,"8:55",35,42],
            [13,1,1,2021,1,3,"8:30",46,47],
            [14,1,1,2021,1,3,"8:35",19,16],
            [15,1,1,2021,1,3,"8:40",20,54],
            [16,1,1,2021,1,3,"8:45",31,46],
            [17,1,1,2021,1,3,"8:50",52,24],
            [18,1,1,2021,1,3,"8:55",15,17],
            [19,1,1,2021,1,4,"8:30",45,49],
            [20,1,1,2021,1,4,"8:35",22,34],
            [21,1,1,2021,1,4,"8:40",44,11],
            [22,1,1,2021,1,4,"8:45",33,29],
            [23,1,1,2021,1,4,"8:50",54,10],
            [24,1,1,2021,1,4,"8:55",31,25],
            [25,1,1,2021,1,5,"8:30",19,37],
            [26,1,1,2021,1,5,"8:35",42,26],
            [27,1,1,2021,1,5,"8:40",24,18],
            [28,1,1,2021,1,5,"8:45",53,41],
            [29,1,1,2021,1,5,"8:50",36,20],
            [30,1,1,2021,1,5,"8:55",35,33],
            [31,2,1,2021,1,1,"8:30",41,36],
            [32,2,1,2021,1,1,"8:35",43,40],
            [33,2,1,2021,1,1,"8:40",11,13],
            [34,2,1,2021,1,1,"8:45",32,32],
            [35,2,1,2021,1,1,"8:50",54,53],
            [36,2,1,2021,1,1,"8:55",17,43],
            [37,2,1,2021,1,2,"8:30",47,60],
            [38,2,1,2021,1,2,"8:35",51,21],
            [39,2,1,2021,1,2,"8:40",11,40],
            [40,2,1,2021,1,2,"8:45",47,54],
            [41,2,1,2021,1,2,"8:50",24,21],
            [42,2,1,2021,1,2,"8:55",19,18],
            [43,2,1,2021,1,3,"8:30",58,56],
            [44,2,1,2021,1,3,"8:35",58,31],
            [45,2,1,2021,1,3,"8:40",27,17],
            [46,2,1,2021,1,3,"8:45",32,12],
            [47,2,1,2021,1,3,"8:50",16,44],
            [48,2,1,2021,1,3,"8:55",23,37],
            [49,2,1,2021,1,4,"8:30",16,17],
            [50,2,1,2021,1,4,"8:35",18,19],
            [51,2,1,2021,1,4,"8:40",16,43],
            [52,2,1,2021,1,4,"8:45",15,58],
            [53,2,1,2021,1,4,"8:50",59,48],
            [54,2,1,2021,1,4,"8:55",54,57],
            [55,2,1,2021,1,5,"8:30",54,26],
            [56,2,1,2021,1,5,"8:35",39,17],
            [57,2,1,2021,1,5,"8:40",53,24],
            [58,2,1,2021,1,5,"8:45",50,27],
            [59,2,1,2021,1,5,"8:50",29,50],
            [60,2,1,2021,1,5,"8:55",54,13],
            [61,3,1,2021,1,1,"8:30",43,48],
            [62,3,1,2021,1,1,"8:35",29,29],
            [63,3,1,2021,1,1,"8:40",59,41],
            [64,3,1,2021,1,1,"8:45",25,32],
            [65,3,1,2021,1,1,"8:50",30,30],
            [66,3,1,2021,1,1,"8:55",35,24],
            [67,3,1,2021,1,2,"8:30",56,20],
            [68,3,1,2021,1,2,"8:35",18,44],
            [69,3,1,2021,1,2,"8:40",12,56],
            [70,3,1,2021,1,2,"8:45",30,35],
            [71,3,1,2021,1,2,"8:50",26,35],
            [72,3,1,2021,1,2,"8:55",33,25],
            [73,3,1,2021,1,3,"8:30",29,18],
            [74,3,1,2021,1,3,"8:35",19,40],
            [75,3,1,2021,1,3,"8:40",44,59],
            [76,3,1,2021,1,3,"8:45",40,35],
            [77,3,1,2021,1,3,"8:50",21,41],
            [78,3,1,2021,1,3,"8:55",38,56],
            [79,3,1,2021,1,4,"8:30",23,44],
            [80,3,1,2021,1,4,"8:35",16,55],
            [81,3,1,2021,1,4,"8:40",22,24],
            [82,3,1,2021,1,4,"8:45",23,24],
            [83,3,1,2021,1,4,"8:50",53,11],
            [84,3,1,2021,1,4,"8:55",38,57],
            [85,3,1,2021,1,5,"8:30",34,10],
            [86,3,1,2021,1,5,"8:35",58,52],
            [87,3,1,2021,1,5,"8:40",39,30],
            [88,3,1,2021,1,5,"8:45",26,31],
            [89,3,1,2021,1,5,"8:50",57,50],
            [90,3,1,2021,1,5,"8:55",48,34],
            [91,4,1,2021,1,1,"8:30",16,37],
            [92,4,1,2021,1,1,"8:35",52,34],
            [93,4,1,2021,1,1,"8:40",25,16],
            [94,4,1,2021,1,1,"8:45",27,36],
            [95,4,1,2021,1,1,"8:50",20,25],
            [96,4,1,2021,1,1,"8:55",59,60],
            [97,4,1,2021,1,2,"8:30",57,50],
            [98,4,1,2021,1,2,"8:35",26,26],
            [99,4,1,2021,1,2,"8:40",44,46],
            [100,4,1,2021,1,2,"8:45",43,18],
            [101,4,1,2021,1,2,"8:50",34,48],
            [102,4,1,2021,1,2,"8:55",23,47],
            [103,4,1,2021,1,3,"8:30",35,51],
            [104,4,1,2021,1,3,"8:35",48,60],
            [105,4,1,2021,1,3,"8:40",45,27],
            [106,4,1,2021,1,3,"8:45",51,39],
            [107,4,1,2021,1,3,"8:50",53,41],
            [108,4,1,2021,1,3,"8:55",53,21],
            [109,4,1,2021,1,4,"8:30",14,29],
            [110,4,1,2021,1,4,"8:35",48,40],
            [111,4,1,2021,1,4,"8:40",54,11],
            [112,4,1,2021,1,4,"8:45",44,30],
            [113,4,1,2021,1,4,"8:50",39,27],
            [114,4,1,2021,1,4,"8:55",12,60],
            [115,4,1,2021,1,5,"8:30",35,49],
            [116,4,1,2021,1,5,"8:35",60,29],
            [117,4,1,2021,1,5,"8:40",35,54],
            [118,4,1,2021,1,5,"8:45",36,25],
            [119,4,1,2021,1,5,"8:50",54,33],
            [120,4,1,2021,1,5,"8:55",23,25],
            [121,5,1,2021,1,1,"8:30",41,53],
            [122,5,1,2021,1,1,"8:35",32,11],
            [123,5,1,2021,1,1,"8:40",35,43],
            [124,5,1,2021,1,1,"8:45",24,49],
            [125,5,1,2021,1,1,"8:50",44,55],
            [126,5,1,2021,1,1,"8:55",24,11],
            [127,5,1,2021,1,2,"8:30",35,31],
            [128,5,1,2021,1,2,"8:35",37,52],
            [129,5,1,2021,1,2,"8:40",41,48],
            [130,5,1,2021,1,2,"8:45",47,28],
            [131,5,1,2021,1,2,"8:50",59,22],
            [132,5,1,2021,1,2,"8:55",39,15],
            [133,5,1,2021,1,3,"8:30",46,53],
            [134,5,1,2021,1,3,"8:35",26,35],
            [135,5,1,2021,1,3,"8:40",60,42],
            [136,5,1,2021,1,3,"8:45",34,40],
            [137,5,1,2021,1,3,"8:50",48,35],
            [138,5,1,2021,1,3,"8:55",26,48],
            [139,5,1,2021,1,4,"8:30",38,19],
            [140,5,1,2021,1,4,"8:35",35,50],
            [141,5,1,2021,1,4,"8:40",19,19],
            [142,5,1,2021,1,4,"8:45",36,14],
            [143,5,1,2021,1,4,"8:50",16,13],
            [144,5,1,2021,1,4,"8:55",49,21],
            [145,5,1,2021,1,5,"8:30",21,20],
            [146,5,1,2021,1,5,"8:35",15,39],
            [147,5,1,2021,1,5,"8:40",37,48],
            [148,5,1,2021,1,5,"8:45",42,34],
            [149,5,1,2021,1,5,"8:50",48,53],
            [150,5,1,2021,1,5,"8:55",29,31]]
    
    return formatData(data)

def formatData(data):
    formatted_data = {  "Year":0,
                        "Term":0,    
                        "Days":{
                            "1":{},
                            "2":{},
                            "3":{},
                            "4":{},
                            "5":{},
                        }   
    }
    
    times = findTimes(data)

    formatted_data["Year"] = data[0][3]
    formatted_data["Term"] = data[0][4]
    formatted_data["Times"] = times
    for i in times:
        for j in range(1,6):
            formatted_data["Days"][str(j)][i]={"Jnr":[],"Snr":[]}
    

    index = 0
    for day in range(1,6):
        while index<len(data) and data[index][1] == day:
            formatted_data["Days"][str(day)][data[index][6]]["Jnr"].append(data[index][7])
            formatted_data["Days"][str(day)][data[index][6]]["Snr"].append(data[index][8])
            index+=1

    return formatted_data



def findTimes(data):
    index = 0
    times = []
    while data[index][1] == 1:
        if data[index][6] not in times:
            times.append(data[index][6])
        index+=1
    return times
    

if __name__ == "__main__":
    print(getPastData())