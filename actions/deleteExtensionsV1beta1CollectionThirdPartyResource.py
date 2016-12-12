from lib import k8s

from st2actions.runners.pythonrunner import Action


class deleteExtensionsV1beta1CollectionThirdPartyResource(Action):

    def run(
            self,
            config_override=None,
            fieldSelector=None,
            labelSelector=None,
            resourceVersion=None,
            timeoutSeconds=None,
            watch=None,
            pretty=None):

        myk8s = k8s.K8sClient(self.config)

        args = {}
        if config_override is not None:
            args['config_override'] = config_override
        if fieldSelector is not None:
            args['fieldSelector'] = fieldSelector
        if labelSelector is not None:
            args['labelSelector'] = labelSelector
        if resourceVersion is not None:
            args['resourceVersion'] = resourceVersion
        if timeoutSeconds is not None:
            args['timeoutSeconds'] = timeoutSeconds
        if watch is not None:
            args['watch'] = watch
        if pretty is not None:
            args['pretty'] = pretty
        return (True,
                myk8s.runAction('deleteExtensionsV1beta1CollectionThirdPartyResource',
                                **args))
