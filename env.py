from os import environ

environ['MONGO_DB_PATH'] = "mmongodb://bornfire:project3@cluster0-shard-00-00.nvora.mongodb.net:27017,cluster0-shard-00-01.nvora.mongodb.net:27017,cluster0-shard-00-02.nvora.mongodb.net:27017/Bornfire?ssl=true&replicaSet=atlas-10s4ho-shard-0&authSource=admin&retryWrites=true&w=majority"
environ['SECRET_KEY'] = "super secret key"