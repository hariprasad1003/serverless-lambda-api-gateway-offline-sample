import json

def hello(event, context):
    try:
        return dict(
            statusCode=200,
            body="Hello World"
        )
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )