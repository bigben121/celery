import os
from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL"))
logger = get_task_logger(__name__)


app.conf["broker_transport_options"] = {'fanout_prefix': True,
                                                'fanout_patterns': True,
                                                'max_connections': 2,
                                                'socket_keepalive': True},
app.conf["broker_pool_limit"] = 2

@app.task
def add(x, y):
    logger.info(f'Adding {x} + {y}')
    return x + y
