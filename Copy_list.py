# copy 
data1 = [ 1,2,3,4 ]
data2 = [ "a","b","c" ]
datalist1 = data1
print( f"Data1 = {data1}")
print( f"dataList1 = {datalist1}")
data1[ -1 ]= 100
print( f"Data1 UPDATED= {data1}")
print( f"dataList1 UPDATED= {datalist1}")
print( f"Memory Address data1 = { hex( id(data1) ) }")
print( f"Memory Address dataList1 = { hex( id(datalist1))}")

print("-"*15)
datalist2 = data2.copy()
print( f"Memory Address data2 = { hex( id(data2) ) }")
print( f"Memory Address dataList2 = { hex( id(datalist2))}")
data2[ 0 ] = "xyz"
print( f"data2 UPDATED= {data2}")
print( f"dataList2 UPDATED= {datalist2}")

print("-"*15, "Nested List")
data1 = [ "I", "G", "S" ]
data2 = [ 10, 11, 12 ]
datalist = [ data1, "x", "y", "z", data2 ]
print( f"datalist = {datalist}")
print( f"datalist[0] = { datalist[0] }")
print( f"datalist[0][1] = { datalist[0][1] }")
datalist_copy = datalist.copy()
print( f"Memory Address datalist={hex(id(datalist))}" )
print( f"Memory Address datalis_copy={hex(id(datalist_copy))}" )
datalist[ -1 ][ -1 ] = 100
print( f"datalist UPDATED= {datalist}")
print( f"datalist_copy UPDATED= {datalist_copy}")

print("-"*15, "DeepCopy")
from copy import deepcopy
datals = deepcopy( datalist)
print( f"datalist = {datalist}")
print( f"datals = {datals}")
datalist[ -1 ][ 0 ] = 777
print( f"datalist UPDATED= {datalist}")
print( f"datals UPDATED= {datals}")