# Data Structures Practrices with Python #

## Lack:  ##

1. Threaded Binary Tree

## Coming: ##

1. Graph
2. Hash
3. Heap

## Notes: ##

### Matrix 矩陣的儲存方法 ###

有一個4x4矩陣matrix是這樣：<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0123行<br>
&nbsp;&nbsp;0&nbsp;&nbsp;0111<br>
&nbsp;&nbsp;1&nbsp;&nbsp;1010<br>
&nbsp;&nbsp;2&nbsp;&nbsp;1101<br>
&nbsp;&nbsp;3&nbsp;&nbsp;1010<br>
&nbsp;&nbsp;列<br><br>
則：
1. 對這個matrix而言，matrix[2][3] = 1 (也就是第2列第3行)
2. 若用陣列的儲存方式是這樣：matrix_list = [ [0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0] ]，而第2列第3行用陣列的表示是matrix_list[2][3]
3. 要對矩陣新增一行的話，就等於是對matrix_list這個二維陣列面的每個陣列append()一個值，因此搭配迴圈做增加: for row in matrix_list: row.append(值)
4. 要對矩陣新增一列的話，就等於是對matrix_list這個二維陣列新增一個element，而這個element是一個陣列，matrix_list.append([值] * len(matrix_list[0]))
