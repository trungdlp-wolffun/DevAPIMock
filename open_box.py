from mitmproxy import ctx
from mitmproxy import http
import json

def response(flow: http.HTTPFlow) -> None:
    print(flow.request.pretty_url)
    if flow.request.pretty_url.endswith("/rivals-box/view-box"):
        data = json.loads(flow.response.get_text())

        if (len(data["data"]) >= 1):
            data["data"][0]["data"]["kind"] = 5
            data["data"][0]["data"]["type"] = 500

        flow.response.text = json.dumps(data)