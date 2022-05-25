from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получение всего списка genres"""
        return self.session.query(Genre).all()

    def get_one(self, gid):
        """Получение определенного жанра по id"""
        return self.session.query(Genre).get(gid)

    def create(self, data):
        """Создание нового жанра"""
        genre = Genre(**data)

        self.session.add(genre)
        self.session.commit()

        return genre

    def update(self, data):
        """Обновление жанра по id"""
        gid = data['id']

        genre = self.get_one(gid)
        if genre is None:
            return "Genre not found", 404

        genre.id = data['id']
        genre.name = data['name']

        self.session.add(genre)
        self.session.commit()

    def delete(self, gid):
        """Удаление по id"""
        genre = self.get_one(gid)

        self.session.delete(genre)
        self.session.commit()


