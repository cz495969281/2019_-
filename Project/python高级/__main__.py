# import __name__
#
# __name__.HaveFun()
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class MyRegexConverter(BaseConverter):

    def __init__(self,url_map,regex):
        super(MyRegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        print("value = %s"%value)
        return int(value) + 10


app.url_map.converters['re'] = MyRegexConverter
@app.route('/<re("\d{3}"):num>')
def index(num):
    print("num = %s" % num)

    return "the num is %s" % num

@app.route('/<re("1[345678]\d{9}"):mobile>')
def get_phone_number(mobile):

    return "the mobile is %s"%mobile

if __name__ == '__main__':
    app.run(debug=True)