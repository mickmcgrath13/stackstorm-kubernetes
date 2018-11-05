from os import sys, path
if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from sensor_base import SensorBase


class watchCoreV1NodeList(SensorBase):

    def __init__(
            self,
            sensor_service,
            config=None,
            extension="/api/v1/watch/nodes",
            trigger_ref="kubernetes.nodes"):
        super(
            watchCoreV1NodeList,
            self).__init__(
            sensor_service=sensor_service,
            config=config,
            extension=extension,
            trigger_ref=trigger_ref)
