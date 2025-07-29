# References: 1.2. System Architecture & Implementation Plan
# References: 1.3. Technology Choices & Rationale (Celery & Redis)
from celery import Celery
from app.config import settings

# Initialize the Celery application instance.
# The first argument is the name of the current module.
# The 'broker' argument specifies the URL of the message broker (Redis).
celery = Celery(
    "frank",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL # Using Redis as the result backend as well
)

# Optional: Configure Celery settings. For example, to ensure tasks and results use JSON.
celery.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

@celery.task
def example_task(x, y):
    """
    An example task to demonstrate how background tasks are created.
    This can be removed later.
    """
    return x + y

# This setup allows us to define tasks in other modules and have Celery discover them.
# For example, a task to process a CSV file would be defined in the banking module
# and would be decorated with @celery.task.
