import os
import html
import logging
from modules.Storage import Storage
from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)


def run_app():
    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist'))
    app = Flask(__name__, static_folder=static_folder, static_url_path='/static')
    storage = Storage()

    @app.route("/")
    def root():
        return app.send_static_file("index.html")

    @app.route("/storage/streets", methods=["GET"])
    def get_street_names():
        return jsonify(storage.get_street_names())

    @app.route("/storage/street/<street_name>/latest", methods=["GET"])
    def get_street_latest_data(street_name):
        return jsonify(storage.get_street(street_name))

    @app.route("/storage/add_latest_date", methods=["POST"])
    def add_today():
        return jsonify(storage.add_today())

    @app.route("/storage/street/<street_name>/house/<house>/set/<date>/<data_type>/<data>", methods=["PUT"])
    def update_data(street_name, house, date, data_type, data):
        return jsonify(storage.update_data(street_name, house, date, data_type, data))

    @app.errorhandler(500)
    def internal_error(error):
        err_template = '<h1>An error has occurred</h1><br/> Some additional info:<br/><pre>%s</pre>'
        err_escaped = html.escape(str(error))
        response_html = err_template % err_escaped
        return response_html, 500

    return app


app = run_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 600
if __name__ == '__main__':
    @app.before_request
    def option_autoreply():
        """ Always reply 200 on OPTIONS request """

        if request.method == 'OPTIONS':
            resp = app.make_default_options_response()

            headers = None
            if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
                headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']

            h = resp.headers

            # Allow the origin which made the XHR
            h['Access-Control-Allow-Origin'] = request.headers['Origin']
            # Allow the actual method
            h['Access-Control-Allow-Methods'] = request.headers['Access-Control-Request-Method']
            # Allow for 10 seconds
            h['Access-Control-Max-Age'] = "10"

            # We also keep current headers
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers

            return resp

    @app.after_request
    def set_allow_origin(resp):
        """ Set origin for GET, POST, PUT, DELETE requests """

        h = resp.headers

        # Allow crossdomain for other HTTP Verbs
        if request.method != 'OPTIONS' and 'Origin' in request.headers:
            h['Access-Control-Allow-Origin'] = request.headers['Origin']

        return resp

    app.run(host="0.0.0.0", threaded=True)
