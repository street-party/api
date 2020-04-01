from src.api.paths.v1.service import response


def get():
    return response.make(False, response=dict(ok=True)), 200
