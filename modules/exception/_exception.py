import sys


def get_message_details(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_frame.f_lineno
    message = str(error)
    error_message = (
        f"""Error occured in python script [{file_name}] line number [{line_number}] error message [{message}]"""
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = get_message_details(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message
