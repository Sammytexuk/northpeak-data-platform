import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session", autouse=True)
def spark():
    session = (
        SparkSession.builder.master("local[1]")
        .appName("ci-tests")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )
    yield session
    session.stop()
