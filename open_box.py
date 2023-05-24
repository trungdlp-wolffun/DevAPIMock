from mitmproxy import ctx
from mitmproxy import http
import json

def response(flow: http.HTTPFlow) -> None:
    print(flow.request.pretty_url)
    if flow.request.pretty_url.endswith("/rivals-box/view-box"):
        data = json.loads(flow.response.get_text())

        if (len(data["data"]) >= 2):
            data["data"][1]["data"]["type"] = 12000031

        flow.response.text = json.dumps(data)