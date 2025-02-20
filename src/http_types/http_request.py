class HttpRequest:
    def __init__(self, body: dict = None, param: dict = None) -> None:
        self.body = body if body is not None else {}
        self.param = param if param is not None else {}
