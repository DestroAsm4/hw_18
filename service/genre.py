from dao.genre import GenreDAO

class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all(self):
        return self.genre_dao.get_all()

    def get_one(self, id):
        return self.genre_dao.get_one(id)

    def create(self, data):
        return self.genre_dao.create(data)

    def update(self, data):
        self.genre_dao.update(data)
        return self.genre_dao

    def delete(self, id):
        self.genre_dao.delete(id)