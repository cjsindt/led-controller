from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<html><body><img src=\"https://wpcdn.us-midwest-1.vip.tn-cloud.net/www.reptilesmagazine.com/content/uploads/data-import/6fd47469/tomato-frog11.jpg\" alt=\"yee-haw\"></img><div><h1>yee-haw</h1></div></body></html>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
