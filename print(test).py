#
# Test file
#
from robol import worker
from read_file import read_file
from missing import missing_power
from handover import handover_a
from avg import avg

conf = {
'target' : -75.0,
'hister' : 3.0,
'maxDec' : 4.0,
'maxInc' : 8.0,
'maxDecHist' : 1.0,
'maxIncHist' : 1.0
}

#print("Testing worker:")
#print(worker((-68.66,1.4),conf))
#print("-"*30)
print("Testing missing:")
print('testing', missing_power([-50, -60, -80, 'missing'], 1, 0))
print("Expected result ([-50,-60,-80,-80],1)", '\n')
print('testing', missing_power([-50, -60, -80, -50], 2, 5))
print("Expected result ([-50,-60,-80,-50],0)", '\n')
print('testing', missing_power([-50, -60, -80, 'missing'], 2, 1))
print("Expected result ([-50,-60,-80,-80],2)", '\n')
print('testing', missing_power([-50, -60, -80, -50], 2, 2))
print("Expected result ([-50,-60,-80,-50],0)", '\n')
print("-"*30)
print("Testing handover:")
print(handover_a(['DL', 'NO', 'MAsdsa', '-60', '3'], (-50, 1), 7, -58))
print(handover_a(['DL', 'S0', 'MAsdsa', '-60', '3'], (-50, 2), 7, -58))
print("-"*30)
print("Testing avg:")
# !!!test
print('testing', avg([-66, -78, -63, -75], [1, 2, 1, 2]))
print("Expected result (-71.6, 1.67)", '\n')
print('testing', avg([50, -78, -63, 60], [1, -2, 1, -5]))
print("Expected result (8.13, -2.60)", '\n')
print('testing', avg([-66.224, -78.55, -63.22, -75], [1.55, 6, 1.33, 2]))
print("Expected result (-71.75, 2.32)", '\n')
print('testing', avg([-66, -78, -63, -75, -55, -69], [1, 2, 1, 2, 3, 4]))
print("Expected result (-66.06, 3.19)", '\n')
print('testing', avg([], []))
print("Expected result (0, 0)", '\n')
print("-"*30)
