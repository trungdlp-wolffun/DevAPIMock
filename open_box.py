from mitmproxy import ctx
from mitmproxy import http
import json

def response(flow: http.HTTPFlow) -> None:
    print(flow.request.pretty_url)
    if flow.request.pretty_url.endswith("/rivals-box/view-box?boxType=3"):
        data = json.loads(flow.response.get_text())

        if (len(data["data"]["items"]) > 0):
            data["data"]["items"][0]["data"]["kind"] = 5
            data["data"]["items"][0]["data"]["type"] = 201
            data["data"]["items"][0]["kind"] = 5

        flow.response.text = json.dumps(data)