import sys

from src.logger import logging


def error_message_detail(error, error_details: sys):
    _,_, exc_tab = error_details.exc_info()
    file_name = exc_tab.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number[{1}] error message [{2}]".format(file_name, exc_tab.tb_lineno, str(error))

    return error_message




class GhanaNewsClassifierException(Exception):
    def __init__(self, error, error_details: sys):
        self.error_message = error_message_detail(
            error=error,
            error_details=error_details
        )

        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message




if __name__=='__main__':
    try:
        logging.info('This is message begginng')
        a =1/1
        print("THe shit is ", a)
    except Exception as e:
        raise GhanaNewsClassifierException(e, sys)