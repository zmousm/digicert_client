from ..queries import Query
from ..responses.v2 import User, Organization, Organizations, Domain, Domains


class V2Query(Query):
    _base_path = '/services/v2'

    def __init__(self, customer_api_key, **kwargs):
        super(V2Query, self).__init__(customer_api_key=customer_api_key, customer_name=None, **kwargs)
        self.set_header('X-DC-DEVKEY', customer_api_key)
        self.set_header('Content-Type', 'application/json')

    def get_method(self):
        return 'GET'

    def _is_failure_response(self, response):
        return 'errors' in response


class OrderDetailsQuery(V2Query):
    def __init__(self, customer_api_key, **kwargs):
        super(OrderDetailsQuery, self).__init__(customer_api_key=customer_api_key, **kwargs)


class RetrieveCertificateQuery(V2Query):
    def __init__(self, customer_api_key, **kwargs):
        super(RetrieveCertificateQuery, self).__init__(customer_api_key=customer_api_key, **kwargs)


class MyUserQuery(V2Query):
    def __init__(self, customer_api_key):
        super(MyUserQuery, self).__init__(customer_api_key=customer_api_key)

    def get_path(self):
        return '%s/user/me' % self._base_path

    def _subprocess_response(self, status, reason, response):
        return User(**response)


class OrganizationByContainerIdQuery(V2Query):
    def __init__(self, customer_api_key, container_id):
        super(OrganizationByContainerIdQuery, self).__init__(customer_api_key=customer_api_key)
        self.container_id = container_id

    def get_path(self):
        return '%s/organization?container_id=%s' % (self._base_path, self.container_id)

    def _subprocess_response(self, status, reason, response):
        orgs = []
        for entry in response['organizations']:
            orgs.append(Organization(**entry))
        return Organizations(orgs)


class DomainByContainerIdQuery(V2Query):
    def __init__(self, customer_api_key, container_id):
        super(DomainByContainerIdQuery, self).__init__(customer_api_key=customer_api_key)
        self.container_id = container_id

    def get_path(self):
        return '%s/domain?container_id=%s' % (self._base_path, self.container_id)

    def _subprocess_response(self, status, reason, response):
        domains = []
        for entry in response['domains']:
            domains.append(Domain(**entry))
        return Domains(domains)

if __name__ == '__main__':
    pass