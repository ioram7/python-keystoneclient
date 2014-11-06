from keystoneclient import base
from keystoneclient import utils

class VoBlacklist(base.Resource):

    pass

class VoBlacklistManager(base.CrudManager):
    """Manager class for manipulating VO Blacklists."""

    resource_class = VoBlacklist
    collection_key = 'vo_blacklist'
    key            = 'vo_blacklist'
    base_url       = 'OS-FEDERATION'
    url_key        = 'blacklist'


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
        print "Entity ID: %s" % entity_id
        print url
        return url

            
    def list(self, **kwargs):
        """List blacklisted users for all VO roles.

        Utilize Keystone URI:
        GET /OS-FEDERATION/vo_blacklist

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoBlacklistManager, self).list(**kwargs)
        

    def get(self, vo_role, **kwargs):
        """List blacklisted users for a VO roles.

        Utilize Keystone URI:
        GET /OS-FEDERATION/vo_roles/{vo_role_id}/blacklist

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoBlacklistManager, self).list(
            vo_role_id=base.getid(vo_role),
            **kwargs)

    def delete(self, vo_role, vo_blacklist_entry):
        """Delete VO role membership request.

        Utilize Keystone URI:
        DELETE DELETE /OS-FEDERATION/vo_roles/{vo_role_id}/requests/{vo_request_id}

        """
        return super(VoBlacklistManager, self).delete(
            vo_role_id=base.getid(vo_role),      
            vo_blacklist_id=base.getid(vo_blacklist_entry)
        )
