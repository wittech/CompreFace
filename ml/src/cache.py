"""
This file should contain all objects that are cached in-memory between requests
"""
from src.constants import ENV
from src.services.utils.pyutils import run_once, run_once_fork_safe


@run_once
def get_scanner():
    from src.services.facescan.scanner.facescanners import FaceScanners
    return FaceScanners.Facenet2018()


@run_once_fork_safe  # Because PyMongo is not fork-safe
def get_storage():
    from src.services.storage.mongo_storage import MongoStorage
    return MongoStorage(ENV.MONGODB_HOST, ENV.MONGODB_PORT)


@run_once_fork_safe  # General precaution against multiprocessing issues
def get_training_task_manager():
    from src.services.async_task_manager.async_task_manager import AsyncTaskManager
    from src.services.train_classifier import train_and_save_classifier_async
    return AsyncTaskManager(train_and_save_classifier_async)
