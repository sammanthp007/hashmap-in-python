from samman_hashmap import HashMap

# Some tests for the program:

# when size of table = 0
table = HashMap(-1)									# test for edge case
table.show_table()
table = HashMap(0)									# test for edge case
table.show_table()

# when size of table = 25
table = HashMap(25)									# test for normal case
table.show_table()
table.set('foo', 'bar')								# test for set() method
table.show_table()
print (table.set('baz', 'stack'))
print (table.get('foo'))							# test for get() method
print (table.delete('foo'))							# test for delete() method
print (table.set('baz1', 'stack1'))
print (table.set('baz2', 'stack2'))
print (table.set('baz3', 'stack3'))
print (table.set('baz', 'replaced'))				# test for collision
table.show_table()
print (table.load())								# test for load() method

# when the size of the table = 101; input being the char value of all number from 1 to 100
table = HashMap(100)
for i in range(1, 101):
	table.set(chr(i), i ** 2)						# test for set() method
print (table.get('b'))								# test for get() method, where key exists
print (table.delete('w'))							# test for delete() method, where the key does not exist
table.show_table()

# results:
"""[]
[]
[[], [], [], [], []]
[[], [], [], [], [['foo', 'bar']]]
True
bar
bar
True
True
True
True
[[], [['baz1', 'stack1']], [['baz2', 'stack2'], ['baz', 'replaced']], [['baz3', 'stack3']], []]
0.16
9604
None
[[['\x0b', 121], ['\x16', 484], ['!', 1089], [',', 1936], ['7', 3025], ['B', 4356], ['M', 5929], ['X', 7744], ['c', 9801]], [['\x01', 1], ['\x0c', 144], ['\x17', 529], ['"', 1156], ['-', 2025], ['8', 3136], ['C', 4489], ['N', 6084], ['Y', 7921], ['d', 10000]], [['\x02', 4], ['\r', 169], ['\x18', 576], ['#', 1225], ['.', 2116], ['9', 3249], ['D', 4624], ['O', 6241], ['Z', 8100]], [['\x03', 9], ['\x0e', 196], ['\x19', 625], ['$', 1296], ['/', 2209], [':', 3364], ['E', 4761], ['P', 6400], ['[', 8281]], [['\x04', 16], ['\x0f', 225], ['\x1a', 676], ['%', 1369], ['0', 2304], [';', 3481], ['F', 4900], ['Q', 6561], ['\\', 8464]], [['\x05', 25], ['\x10', 256], ['\x1b', 729], ['&', 1444], ['1', 2401], ['<', 3600], ['G', 5041], ['R', 6724], [']', 8649]], [['\x06', 36], ['\x11', 289], ['\x1c', 784], ["'", 1521], ['2', 2500], ['=', 3721], ['H', 5184], ['S', 6889], ['^', 8836]], [['\x07', 49], ['\x12', 324], ['\x1d', 841], ['(', 1600], ['3', 2601], ['>', 3844], ['I', 5329], ['T', 7056], ['_', 9025]], [['\x08', 64], ['\x13', 361], ['\x1e', 900], [')', 1681], ['4', 2704], ['?', 3969], ['J', 5476], ['U', 7225], ['`', 9216]], [['\t', 81], ['\x14', 400], ['\x1f', 961], ['*', 1764], ['5', 2809], ['@', 4096], ['K', 5625], ['V', 7396], ['a', 9409]], [['\n', 100], ['\x15', 441], [' ', 1024], ['+', 1849], ['6', 2916], ['A', 4225], ['L', 5776], ['W', 7569], ['b', 9604]]]
"""