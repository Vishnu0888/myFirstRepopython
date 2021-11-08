import pytest

from LogBase import TestLogBase


@pytest.mark.usefixtures("dataset")
class Testdataset(TestLogBase):

    def test_dataset(self, dataset):
        log = self.get_log()
        log.info(dataset[0])
        log.info(dataset[1])
        #print(dataset[0])
        #print(dataset[1])

