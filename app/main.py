from app.routes.api.v1.api_recepcion import app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)