import logging

logging.basicConfig(
    format="%(levelname)s:%(message)s",
    filename="example.log",
    level=logging.DEBUG)
logging.warning("Внимание! Код находится под наблюдением!")
logging.info("Информационное сообщение которое будет в файле")