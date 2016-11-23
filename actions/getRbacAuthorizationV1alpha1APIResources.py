from lib import k8s

from st2actions.runners.pythonrunner import Action

class getRbacAuthorizationV1alpha1APIResources(Action):

    def run(self):

        myk8s = k8s.K8sClient(self.config)

        args = {}

        return (True, myk8s.runAction('getRbacAuthorizationV1alpha1APIResources', **args))