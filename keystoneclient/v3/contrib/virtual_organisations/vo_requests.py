from keystoneclient import base
from keystoneclient import utils

class VoRequest(base.Resource):

    pass

class VoRequestsManager(base.CrudManager):
    """Manager class for manipulating VO Roles."""

    resource_class = VoRequest
    collection_key = 'vo_requests'
    key            = 'vo_request'
    url_key        = 'requests'
    base_url       = 'OS-FEDERATION'


    def build_url(self, dict_args_in_out=None):
        """Build URL for VO memberships."""

        if dict_args_in_out is None:
            dict_args_in_out = {}

        vo_role_id = dict_args_in_out.pop('vo_role_id',
                                                    None)

        if vo_role_id:
            base_url = '/vo_roles/'.join([self.base_url, vo_role_id])
        else:
            base_url = self.base_url

        dict_args_in_out.setdefault('base_url', base_url)
        
        url = dict_args_in_out.pop('base_url', None) or self.base_url or ''
        url += '/%s' % self.url_key

        # do we have a specific entity?
        entity_id = dict_args_in_out.pop('%s_id' % self.key, None)
        if entity_id is not None:
            url += '/%s' % entity_id

        return url
            
    def approve(self, vo_role, vo_request):
        """Approve VO role membership user request

        Utilize Keystone URI:
        GET /OS-FEDERATION/vo_roles/{vo_role_id}

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoRequestsManager, self).head(
            vo_role_id=base.getid(vo_role),
            vo_request_id= base.getid(vo_request)
        )
            
    def list(self, vo_role, **kwargs):
        """List VO role membership user requests.

        Utilize Keystone URI:
        GET GET /OS-FEDERATION/vo_roles/{vo_role_id}/requests

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoRequestsManager, self).list(
            vo_role_id=base.getid(vo_role),
            **kwargs)
        
    def delete(self, vo_role, vo_request):
        """Delete VO role membership request.

        Utilize Keystone URI:
        DELETE DELETE /OS-FEDERATION/vo_roles/{vo_role_id}/requests/{vo_request_id}

        """
        return super(IdentityProviderManager, self).delete(
            vo_role_id=base.getid(vo_role),
            vo_request_id=base.getid(vo_request)
        )
