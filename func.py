
def wash(dry, water=8):
    print ('加水', water, '分滿')
    print ('加洗衣精')
    print ('旋轉')
    if dry:
  	   print('烘衣')

wash(True, 8)
wash(False, 6)
#wash(water=10) #可以只指定某一個參數的值

def add(x, y):
 	return x+y
result = add(3, 4) #沒有指定哪一個參數就是依照順序
print(result)

#return可以把function的執行結果存下來

def average(numbers):
	return sum(numbers) / len(numbers)	#有return才有值可以回傳
print (average([1, 2, 3]))

