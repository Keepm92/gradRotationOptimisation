import random

def collectNames():
    """Collect the names of the graduates"""
    quitString = ""
    names = []
    while quitString != "no" and quitString != "n":
        quitString = raw_input("Enter student name (type n to quit):")
        if quitString != "no" and quitString != "n":
            names.append(quitString)
        
    return names
    
def setPreferences(graduates,preferences):
    """Assigned preferences 1-3 for each graduate"""
    for grad in graduates:
        inputCheck = True
        inputText = ""
        while (inputCheck):
            inputText = raw_input("What is "+graduates[grad].name+"'s first preference? ")
            if inputText in preferences:
                graduates[grad].pref1 = inputText
                inputCheck = False
            else:
                print "Preference not available. Please select one of; " + str(preferences)
                inputCheck = True
                
        inputCheck = True
        while (inputCheck):
            inputText = raw_input("What is "+graduates[grad].name+"'s second preference? ")
            if inputText in preferences:
                graduates[grad].pref2 = inputText
                inputCheck = False
            else:
                print "Preference not available. Please select one of; " + str(preferences)
                inputCheck = True
                
        inputCheck = True
        while (inputCheck):
            inputText = raw_input("What is "+graduates[grad].name+"'s third preference? ")
            if inputText in preferences:
                graduates[grad].pref3 = inputText
                inputCheck = False
            else:
                print "Preference not available. Please select one of; " + str(preferences)
                inputCheck = True
    return graduates

def setRank(graduates):
    for grad in graduates:
        print "What rank should " + graduates[grad].name + " be given?"
        graduates[grad].rank = input("Enter a rank integer? ")
    return graduates
    
def assignGrads(graduates, gradObj, preferences):
    assignedGrads = {}
    allocated = ["a","c"];
    print graduates
    remainder = len(graduates)
    while (remainder > 0):
        gradSelector = random.randrange(len(graduates))
        currentGrad = gradObj[graduates[gradSelector]]
        print currentGrad.name
        
        if currentGrad.pref1 not in allocated:
            allocated.append(currentGrad.pref1)
            assignedGrads[currentGrad.name] = currentGrad.pref1
        elif currentGrad.pref2 not in allocated:
            allocated.append(currentGrad.pref2)
            assignedGrads[currentGrad.name] = currentGrad.pref2
        elif currentGrad.pref3 not in allocated:
            allocated.append(currentGrad.pref3)
            assignedGrads[currentGrad.name] = currentGrad.pref3
        else:
           print currentGrad.name + " is on cafe rotation."
        
        graduates.remove(str(graduates[gradSelector]))
        remainder = len(graduates)
        
    print allocated
    print assignedGrads
    return