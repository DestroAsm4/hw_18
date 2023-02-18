from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service
from dao.model.movies import MovieSchema

movies_ns = Namespace('movies')

@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year,
        }
        movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(movies)
        return result, 200

@movies_ns.route('/location/')
class MovieViewPost(Resource):

    def post(self):
        data = request.json
        movie_service.create(data)
        return "", 201

@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_by_id(mid)
        movie_data = MovieSchema().dump(movie)
        return movie_data, 200

    def put(self, mid):
        data = request.json
        data['id'] = mid
        movie_service.updata(data)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
