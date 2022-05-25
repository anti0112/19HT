class GenreService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def delete(self, gid):
        self.dao.delete(gid)
