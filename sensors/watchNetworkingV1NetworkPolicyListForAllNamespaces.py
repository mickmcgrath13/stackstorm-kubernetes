from os import sys, path
if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from sensor_base import SensorBase


class watchNetworkingV1NetworkPolicyListForAllNamespaces(SensorBase):

    def __init__(
            self,
            sensor_service,
            config=None,
            extension="/apis/networking.k8s.io/v1/watch/networkpolicies",
            trigger_ref="kubernetes.networkpolicies"):
        super(
            watchNetworkingV1NetworkPolicyListForAllNamespaces,
            self).__init__(
            sensor_service=sensor_service,
            config=config,
            extension=extension,
            trigger_ref=trigger_ref)
