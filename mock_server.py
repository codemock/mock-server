from flask import Flask, request
import os
import json

app = Flask(__name__)
default_code = 200
filename = os.environ.get('mock-file-data','output.json')
with open(filename, 'r') as f:
    url_output_map = json.load(f)

def base_response_to_request():
    key = "/" + request.base_url.lstrip(request.host_url)
    output_list = url_output_map[key].get(request.method)
    for output in output_list:
        query = output.get('query_string',{})
        status_code = output.get('status_code', default_code)
        args = request.args
        if all(args.get(key)==value for key,value in query.items()):
            return output.get('response'), status_code
    return 'failed'


def bootstrap(app):
    for url in url_output_map:
        app.add_url_rule(url, url, base_response_to_request)

bootstrap(app)

if __name__=='__main__':
	app.run()
