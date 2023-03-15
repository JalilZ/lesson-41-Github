from flask import Flask
api = Flask(__name__)  # create application


@api.route('/')
def hello():
    return '<p style="background-color: bisque;">Hello, World!</p>'


if __name__ == '__main__':
   api.run(debug=True)
