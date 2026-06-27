import logging

logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('system started')
logging.debug('initializing modules')
logging.info('modules initialized successfully')
logging.warning('low disk space')
logging.error('failed to connect to database')
logging.info('system shutdown initiated')