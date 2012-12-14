import json
from django.http import HttpResponse

def render_json(obj):
    return HttpResponse(json.dumps(obj), mimetype='application/json')