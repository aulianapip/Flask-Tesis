from pymongo import MongoClient

class DBModel:
	client = MongoClient()

# **********************************Login********************************************

	def find_user(self, database, collection, find):
		db = self.client[database]
		result= db[collection].find_one({'user':find})
		return result

	def insert_user(self, database, collection, document):
		db = self.client[database]
		results = db[collection].insert(document)
		return results


# **********************************Upload********************************************
	def insert_cleaning_data(self, database, collection, documents):
		db = self.client[database]
		db[collection].drop()
		results = db[collection].insert_many(documents.to_dict('records'))
		return results.inserted_ids

	def insert_header(self, database, collection, documents):
		db = self.client[database]
		db[collection].drop()
		results = db[collection].insert(documents)
		return results

	def get_data_all(self, database, collection):
		db = self.client[database]
		cursor = db[collection].find({},{"_id":0})
		return cursor

# **********************************Text Mining********************************************
	def insert_tokenisasi(self, database, collection, documents):
		db = self.client[database]
		db[collection].drop()
		results = db[collection].insert_many(documents.to_dict('records'))
		return results.inserted_ids

	def insert_filtering(self, database, collection, documents):
		db = self.client[database]
		db[collection].drop()
		results = db[collection].insert_many(documents.to_dict('records'))
		return results.inserted_ids

	def insert_stemming(self, database, collection, documents):
		db = self.client[database]
		db[collection].drop()
		results = db[collection].insert_many(documents.to_dict('records'))
		return results.inserted_ids

	def insert_euclidean(self, database, collection, documents):
		db = self.client[database]
		db[collection].drop()
		results = db[collection].insert_many(documents.to_dict('records'))
		return results.inserted_ids

	def insert_hasil(self, database, collection, judul, cluster):
		db = self.client[database]
		results = db[collection].insert({"Judul":judul, "Cluster":cluster})
		return results
#*******************************Nyimpan Hasil**************************************
	def insert_file(self, database, collection, file, sheet):
		db = self.client[database]
		results = db[collection].insert({"Nama File": file, "Sheet": sheet})
		return results

	def get_file_desc(self, database, collection):
		db = self.client[database]
		cursor = db[collection].find({},{"Sheet":1, "_id":0}).sort([('_id', -1)]).limit(1)
		return cursor

	def get_file_desc2(self, database, collection):
		db = self.client[database]
		cursor = db[collection].find({}, {"Nama File": 1, "_id": 0}).sort([('_id', -1)]).limit(1)
		return cursor

	def get_sheet(self, database, collection):
		db = self.client[database]
		cursor = db[collection].find({},{"Sheet":1, "_id":0})
		return cursor

	def get_nclust(self, database, collection):
		db = self.client[database]
		cursor = db[collection].find({},{"Jumlah Cluster":1, "_id":0})
		return cursor

	def find_group(self, database, collection, n):
		db = self.client[database]
		cursor = db[collection].find({"Cluster":n},{"Judul":1,"_id":0}).distinct("Judul")
		return cursor
#----------------------------------nyimpan dengan nama sheet baru jika sama-----------------------------------------
	def update_file1(self, database, collection, f, s, k):
		db = self.client[database]
		result = db[collection].update({"Nama File":f}, {"$set":{"Sheet":s, "Jumlah Cluster":k}})
		return result

	def update_file(self, database, collection, f, s, k):
		db = self.client[database]
		result = db[collection].update({"Nama File":f, "Sheet":s}, {"$set":{"Sheet":s, "Jumlah Cluster":k}})
		return result

	def delete_same(self, database, collection, f, s):
		db = self.client[database]
		result = db[collection].delete_one({"Nama File":f, "Sheet":s})
		return result

	def find_file(self, database, collection, f, s):
		db = self.client[database]
		if (db[collection].find({"Nama File":f, "Sheet":s}).count() == 0):
			return False
		else:
			return True

	def find_collection(self, database, collection):
		db = self.client[database]
		if (db[collection].find({}).count() == 0):
			return False
		else:
			return True

	def delete_collection(self, database, collection):
		db = self.client[database]
		result = db[collection].drop()
		return result

	def find_sheet(self, database, collection, s):
		db = self.client[database]
		if (db[collection].find({"Sheet":s}).count() >= 2):
			return True
		else:
			return False

	def count_sheet(self, database, collection, s):
		db = self.client[database]
		result = db[collection].find({"Sheet": s}).count()
		return result