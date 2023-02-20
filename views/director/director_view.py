from flask_restx import Resource, Namespace
from flask import request

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        director = director_service.get_all()
        result = DirectorSchema(many=True).dump(director)
        return result, 200

@director_ns.route('/location/')
class DirectorsView(Resource):

    def post(self):
        data = request.json
        director_service.create(data)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did: int):
        director = director_service.get_one(did)
        result = DirectorSchema().dump(director)
        return result, 200

    def put(self, did):
        data = request.json
        data['id'] = did
        director_service.update(data)
        return '', 204

    def delete(self, did):
        director_service.delete(did)