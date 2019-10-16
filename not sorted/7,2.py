#Задано текст з латинських літер.
#Скласти програму, яка визначає і виводить на екран такі множини:
#  а)символи – перші входження в текст, зберігаючи при цьому їх вихідний
#        взаємний порядок;
#  б) всі літери, які входять в текст не менше двох разів;
#  в) всі літери, які входять в текст по одному разу. 
import collections

def getUniqueSymbolsByInvokeNum(text, invokeNum):
   d = collections.defaultdict(int)
   for c in text:
       d[c] += 1

   if invokeNum == 1:
      result = []
      for c in d:
         if d[c] == 1:
            result.append(c)
      return result
   elif invokeNum >= 1:
      result = []
      for c in d:
         if d[c] >= invokeNum:
            result.append(c)
      return result
   return list(d)

text = input("Enter your text: ")
print("set: ", getUniqueSymbolsByInvokeNum(text, 0))
print(">2 invokes: ", getUniqueSymbolsByInvokeNum(text, 2))
print("only 1 invoke: ", getUniqueSymbolsByInvokeNum(text, 1))

