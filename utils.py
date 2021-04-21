

def require(expression: bool, error_msg: str):
    if not expression:
        raise ValueError(error_msg)
