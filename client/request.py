import time
from datetime import datetime, timedelta

from client.response import Response
from config import REQUEST_TIMEOUT, DELAY_BETWEEN_RETRIES

errorResponse = Response(500, [], "Call exception")


def call(call_function):
    def _wrapper(*args, **kwargs):
        start = datetime.now()
        while True:
            if datetime.now() - start >= timedelta(seconds=REQUEST_TIMEOUT):
                return errorResponse

            try:
                result = call_function(*args, **kwargs)
                return result

            except Exception as e:
                # print(f"Call error")
                time.sleep(DELAY_BETWEEN_RETRIES)

    return _wrapper
