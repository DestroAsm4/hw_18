from dao.movie import MovieDAO

class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self, filters):
        return self.movie_dao.get_all(filters)

    def get_by_id(self, id):
        return self.movie_dao.get_by_id(id)

    def create(self, data):
        return self.movie_dao.create(data)

    def update(self, data):
        self.movie_dao.update(data)
        return self.movie_dao

    def delete(self, id):
        self.movie_dao.delete(id)
