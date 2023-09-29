import os
import shutil

import urllib.request
from loguru import logger


def download_file(directory, filename):
    url = f"https://github.com/khanhnamle1994/instacart-orders/raw/master/data/{filename}?download="
    logger.debug(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, os.path.join(directory, filename))


if __name__ == "__main__":
    files = ["order_products__prior.csv", "orders.csv", "products.csv", "aisles.csv", "departments.csv"]
    logger.debug(f"Downloading {len(files)} files")

    shutil.rmtree('../data', ignore_errors=True)
    os.mkdir("../data")
    os.mkdir("../data/raw")

    for file in files:
        download_file(directory="../data/raw", filename=file)
