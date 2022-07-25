"""
Minimum Package Demo
"""
import logging

logging.getLogger().handlers.clear()
logging.basicConfig(
    format='%(asctime)s | %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)


class Demo:
    """
    This class is to show how to setup a package members
    """
    def __init__(self, msg: str):
        """
        This is where class members are initialized
        :param msg: input messaeg to display
        """
        self.message = msg

    def show_message(self) -> None:
        """
        Displaying message in the log console
        :return: None
        """
        logging.info(self.message)
