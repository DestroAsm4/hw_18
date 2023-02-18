from dao.model.director import Director


class DirectorDAO:

    def __init__(self, session):
        self.session = session
        self.model = Director

    def get_one(self, did):
        return self.session.query(self.model).get(did)

    def get_all(self):
        return self.session.query(self.model).all()

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, data):
        director = self.get_one(data['id'])
        director.name = data['name']

        self.session.add(director)
        self.session.commit()
