from dao.director import DirectorDAO

class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_all(self):
        return self.director_dao.get_all()

    def get_one(self, did: int):
        return self.director_dao.get_one(did)

    def create(self, data):
        return self.director_dao.create(data)

    def updata(self, data):
        self.director_dao = self.director_dao.update(data)
        return self.director_dao

    def delete(self, id):
        self.director_dao.delete(id)