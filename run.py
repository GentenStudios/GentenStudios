from app import app, db, routes

if __name__ == '__main__':
    routes.init(app, db)
    app.run()
