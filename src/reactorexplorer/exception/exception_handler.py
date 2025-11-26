import os
import sys

# Custom exception for debugging and traceability
class AppException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = AppException.error_message_detail(error_message, error_detail = error_detail)

    @staticmethod
    def error_message_detail(error: Exception, error_detail = sys):
        """
        error: Exception object raise from module
        error_detail: is sys module contains detail information about system execution information.
        """
        _,_, exc_tb = error_detail.exc_info()
        
        #extracting file name from exception traceback
        file_name = exc_tb.tb_frame.f_code.co_filename

        error_message = f"Error occurred in script: [{file_name}] at line number: [{exc_tb.tb_lineno}] error message: [{str(error)}]"

        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return AppException.__name__.str() + ": " + self.error_message
    