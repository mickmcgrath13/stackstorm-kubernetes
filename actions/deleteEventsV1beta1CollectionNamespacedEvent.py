import json

from lib.k8s import K8sClient


class deleteEventsV1beta1CollectionNamespacedEvent(K8sClient):

    def run(
            self,
            namespace,
            more=None,
            fieldSelector=None,
            includeUninitialized=None,
            labelSelector=None,
            limit=None,
            resourceVersion=None,
            timeoutSeconds=None,
            watch=None,
            pretty=None,
            config_override=None):

        ret = False

        args = {}
        args['config_override'] = {}
        args['pretty'] = ''

        if config_override is not None:
            args['config_override'] = config_override

        if namespace is not None:
            args['namespace'] = namespace
        else:
            return (False, "namespace is a required parameter")
        if more is not None:
            args['continue'] = more
        if fieldSelector is not None:
            args['fieldSelector'] = fieldSelector
        if includeUninitialized is not None:
            args['includeUninitialized'] = includeUninitialized
        if labelSelector is not None:
            args['labelSelector'] = labelSelector
        if limit is not None:
            args['limit'] = limit
        if resourceVersion is not None:
            args['resourceVersion'] = resourceVersion
        if timeoutSeconds is not None:
            args['timeoutSeconds'] = timeoutSeconds
        if watch is not None:
            args['watch'] = watch
        if pretty is not None:
            args['pretty'] = pretty
        if 'body' in args:
            args['data'] = args['body']
        args['headers'] = {'Content-type': u'application/json', 'Accept': u'application/json, application/yaml, application/vnd.kubernetes.protobuf'}  # noqa pylint: disable=line-too-long
        args['url'] = "apis/events.k8s.io/v1beta1/namespaces/{namespace}/events".format(  # noqa pylint: disable=line-too-long
            namespace=namespace)
        args['method'] = "delete"

        self.addArgs(**args)
        self.makeRequest()

        myresp = {}
        myresp['status_code'] = self.resp.status_code
        myresp['data'] = json.loads(self.resp.content.rstrip())

        if myresp['status_code'] >= 200 and myresp['status_code'] <= 299:
            ret = True

        return (ret, myresp)
