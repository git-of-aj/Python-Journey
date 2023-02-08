for i in range(5):
  print(('H'*i).rjust(4))
# print H i times in right side after 4 total spaces

'''
prints:
[nothing]  ===> Coz 'H'* 0 == 0 so,nothing prints   0
***H               ==> Width 4 so H at 4 position     1
  HH                    2
 HHH                    3
HHHH                    4
'''
