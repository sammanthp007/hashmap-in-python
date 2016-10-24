class HashMap(object):
	# constructor(size): return an instance of the class with pre-allocated space for the given number of objects.
	def __init__(self, max_num_of_items):
		self.num_of_items = max_num_of_items
		if self.num_of_items <= 0:
			self.bucket_size = 0
		elif self.num_of_items == 1:
			self.bucket_size = 1
		elif self.num_of_items < 10:
			self.bucket_size = 2
		elif self.num_of_items < 100:
			self.bucket_size = self.num_of_items // 5
		else:
			self.bucket_size = self.num_of_items // 10 + 1
		self.hash_table = self.make_hashtable(self.bucket_size)

	def make_hashtable(self, bucket_size):
		hash_table = []
		for buckets in range(bucket_size):
			hash_table.append([])
		return hash_table

	def hash_string(self, string):
		hash_number = 0
		for i in string:
			hash_number += ord(i)
		return hash_number % self.bucket_size

	def hash_table_get_bucket(self, key):
		return self.hash_table[self.hash_string(key)]

	# boolean set(key, value): stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
	def set(self, key, value):
		if len(self.hash_table) <= self.num_of_items:
			bucket = self.hash_table_get_bucket(key)
			for item in bucket:
				if item[0] == key:
					bucket.remove(item)
			bucket.append([key, value])
			return True
		return False

	# get(key): return the value associated with the given key, or null if no value is set.
	def get(self, key):
		bucket = self.hash_table_get_bucket(key)
		for k, v in bucket:
			if k == key:
				return v
		return None

	# delete(key): delete the value associated with the given key, returning the value on success or null if the key has no value.
	def delete(self, key):
		bucket = self.hash_table_get_bucket(key)
		for item in bucket:
			if item[0] == key:
				value = item[1]
				bucket.remove(item)
				return item[1]
		return None

	# float load(): return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.
	def load(self):
		items = 0
		for buckets in self.hash_table:
			for keys in buckets:
				items += 1
		return (items / self.num_of_items)

	def show_table(self):
		print (self.hash_table)