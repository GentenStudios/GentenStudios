from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    modules = db.relationship('Module', back_populates='owner', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<id {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


class Module(db.Model):
    __tablename__ = 'modules'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner = db.relationship('User', back_populates='modules')
    name = db.Column(db.String(), nullable=False)
    source = db.Column(db.String(), nullable=False)

    def __init__(self, name, source):
        self.name = name
        self.source = source

    def __repr__(self):
        return f'<id {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'source': self.source,
            'owner': self.owner.username,
        }


# class TagCategory(db.Model):
#     __tablename__ = 'tag_categories'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(), unique=True, nullable=False)
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return '<id ()>'.format(self.id)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name
#         }
#
#
# class Tag(db.Model):
#     __tablename__ = 'tags'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     category = db.Column(db.Model(TagCategory))
#
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category
#
#     def __repr__(self):
#         return '<id ()>'.format(self.id)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'category': self.category
#         }
#
#
# class ModuleTag(db.Model):
#     __tablename__ = 'module_tags'
#
#     id = db.Column(db.Integer, primary_key=True)
#     module = db.Column(db.Model(Module))
#     category = db.Column(db.Model(TagCategory))
#
#     def __init__(self, module, category):
#         self.module = module
#         self.category = category
#
#     def __repr__(self):
#         return '<id ()>'.format(self.id)
