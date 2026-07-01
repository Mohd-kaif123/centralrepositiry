import logging

'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('root:Application Started')
'''
'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('Root: Application started')
logging.info('Root: Loading Data')
logging.info('Root: Program Finished')
logging.warning('root: Disk usage is High')
logging.error('root: Application Crashed')
'''
'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(levelname)s:%(message)s:%(name)s'
)
name =input("Enter Name:")
logging.info(f"User {name} Logged IN ")
'''
'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
   format='%(asctime)s - %(levelname)s - %(message)s'
)
def backup():
    logging.info("Backup  started")
    logging.info("Backup completed")
backup()
'''