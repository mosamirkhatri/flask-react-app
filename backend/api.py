from flask import Flask
import time


app = Flask(__name__)

@app.route('/')
def get_current_time():
    """
    docstring
    """
    return {'time': time.time()}



# if __name__ == '__main__':
#     app.run(debug=True)