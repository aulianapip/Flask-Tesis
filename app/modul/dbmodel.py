from pymongo import MongoClient

class DBModel:

	client = MongoClient()

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
		cursor = db[collection].find({})

		return cursor

	def get_data_spe(self, database, collection):
		db = self.client[database]
		cursor = db[collection].find({},{"Judul":1,"_id":0})

		return cursor


	def get_data_cluster(self, database, collection):
		db = self.client[database]
		cursor = db[collection].find({},{"c1":1,"_id":0})

		return cursor

	def get_data_cluster1(self, database, collection):
		db = self.client[database]
		cursor = db[collection].find({},{"c2":1,"_id":0})

		return cursor

	def insert_tokenisasi_data(self, database, collection, documents):
		db = self.client[database]
		db[collection].drop()
		results = db[collection].insert_many(documents.to_dict('records'))

		return results.inserted_ids

	def insert_filtering_data(self, database, collection, documents):
		db = self.client[database]
		db[collection].drop()
		results = db[collection].insert_many(documents.to_dict('records'))

		return results.inserted_ids

	def insert_stemming_data(self, database, collection, documents):
		db = self.client[database]
		db[collection].drop()
		results = db[collection].insert_many(documents.to_dict('records'))

		return results.inserted_ids