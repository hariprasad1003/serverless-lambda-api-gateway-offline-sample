import json

def get_greeting(event, context):
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

def post_greeting(event, context):
    try:

        body = event["body"]

        return dict(
            statusCode=200,
            body=f"{body}"
        )
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )