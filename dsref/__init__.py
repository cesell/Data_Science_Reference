import logging

logging.basicConfig(filename='dsref.log', filemode='w',
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s',
                    level=logging.DEBUG)

logging.info('Log Started')