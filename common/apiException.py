class APIException(Exception):
    def __init__(self, message, code, status=200):
        Exception.__init__(self)
        self.message = message
        self.code = code
        self.status = status

    def to_dict(self):
        result = {
            'message': self.message,
            'code': self.code
        }
        return result
