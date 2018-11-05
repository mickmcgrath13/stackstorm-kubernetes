from os import sys, path
if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from sensor_base import SensorBase


class watchSettingsV1alpha1PodPresetListForAllNamespaces(SensorBase):

    def __init__(
            self,
            sensor_service,
            config=None,
            extension="/apis/settings.k8s.io/v1alpha1/watch/podpresets",
            trigger_ref="kubernetes.podpresets"):
        super(
            watchSettingsV1alpha1PodPresetListForAllNamespaces,
            self).__init__(
            sensor_service=sensor_service,
            config=config,
            extension=extension,
            trigger_ref=trigger_ref)
