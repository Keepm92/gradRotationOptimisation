def collectNames():
    """Collect the names of the graduates"""
    quitString = ""
    names = []
    while quitString != "no" and quitString != "n":
        quitString = raw_input("Enter student name (type n to quit):")
        if quitString != "no" and quitString != "n":
            names.append(quitString)
        
    return names
    
def setPreferences(graduates):
    """Assigned preferences 1-3 for each graduate"""
    for grad in graduates:
        graduates[grad].pref1 = raw_input("What is "+graduates[grad].name+"'s first preference? ")
        graduates[grad].pref2 = raw_input("What is "+graduates[grad].name+"'s second preference? ")
        graduates[grad].pref3 = raw_input("What is "+graduates[grad].name+"'s third preference? ")
    return graduates

def setRank(graduates):
    for grad in graduates:
        print "What rank should " + graduates[grad].name + " be given?"
        graduates[grad].rank = input("Enter a rank integer? ")
    return graduates