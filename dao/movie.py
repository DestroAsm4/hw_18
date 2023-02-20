from dao.model.movies import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session
        self.model = Movie

    def get_all(self, filters):
        if filters['director_id']:
            return self.session.query(self.model).filter(
                self.model.director_id == filters['director_id']
            ).all()
        elif filters['genre_id']:
            return self.session.query(self.model).filter(
                self.model.genre_id == filters['genre_id']
            ).all()
        elif filters['year']:
            return self.session.query(self.model).filter(
                self.model.year == filters['year']
            ).all()
        return self.session.query(self.model).all()

    def get_by_id(self, id):
        return self.session.query(self.model).get(id)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data):
        id = data.pop('id')
        movie = self.get_by_id(id)

        for field_name, field_value in data.items():
            setattr(movie, field_name, field_value)

        self.session.add(movie)
        self.session.commit()

    def delete(self, id):
        movie = self.session.query(self.model).get(id)
        self.session.delete(movie)
        self.session.commit()

