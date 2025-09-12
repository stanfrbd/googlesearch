import base64


def get_useragent():
    parts = ["TW96aWxsYS80LjA=", "IChQU1AgKFBsYXlTdGF0aW9uIFBvcnRhYmxlKTs=", "IDIuMDAp"]
    decoded = "".join(map(lambda x: base64.b64decode(x).decode("utf-8"), parts))
    return "".join(decoded[i] for i in range(len(decoded)))
