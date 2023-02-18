from dao.model.genre import Genre


class GenreDAO:

    def __init__(self, session):
        self.session = session
        self.model = Genre

    def get_one(self, gid):
        return self.session.query(self.model).get(gid)

    def get_all(self):
        return self.session.query(self.model).all()

    def create(self, data):
        genre = self.model(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, data):
        genre = self.get_one(data['id'])
        genre.name = data['name']

        self.session.add(genre)
        self.session.commit()