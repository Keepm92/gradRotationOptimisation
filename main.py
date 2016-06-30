# Hello World program in Python
import dataGathering as dg
from graduate import Grad

print "Begin\n"
preferences = ["Dev", "BA" , "Infrastructure"]
graduates = dg.collectNames()
gradObj = {};

for grad in graduates:
    gradObj[grad] = Grad(grad)

gradObj = dg.setRank(gradObj)
gradObj = dg.setPreferences(gradObj)

print gradObj["matt"].pref1
print str(gradObj["matt"].rank)






