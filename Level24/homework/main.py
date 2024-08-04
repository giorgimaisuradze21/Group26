# def manual_len(listnn1):
#     summ1=0
#     for i in listnn1:
#         if i > summ1:
#          summ1=i
#     return summ1
# print(manual_len([1,2,3,4,5]))     



def manual_min(listnn1):
   summ1=listnn1[1]
   for i in listnn1:
       if i > summ1:
         summ1=i
         return summ1       
print(manual_min([90,30,21]))   