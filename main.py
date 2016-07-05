# Hello World program in Python
import dataGathering as dg
from graduate import Grad

print "Begin\n"
preferences = ["a", "b" , "c"]
graduates = dg.collectNames()
gradObj = {};

for grad in graduates:
    gradObj[grad] = Grad(grad)

#gradObj = dg.setRank(gradObj)
gradObj = dg.setPreferences(gradObj,preferences)


dg.assignGrads(graduates, gradObj, preferences)








