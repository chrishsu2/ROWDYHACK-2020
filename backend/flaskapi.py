from flask import Flask, json

data = #python object

api = Flask(__name__)

@api.route('/data', methods=['GET'])
def get_data():
  return json.dumps(data)

@api.route('/data', methods=['POST'])
def post_data():
  return json.dumps({"success": True}), 201

if __name__ == '__main__':
    api.run()
