
class BaseHandler:
    def __init__(self):
        self.is_initialized = False

    def initialize(self):
        self.is_initialized = True

    def preprocess(self, data):
        return data

    def inference(self, data):
        return data

    def postprocess(self, data):
        return data

    def handle(self, data):

        data = self.preprocess(data)
        data = self.inference(data)
        data = self.postprocess(data)

        return data

    def __call__(self, data):
        return self.handle(data)
