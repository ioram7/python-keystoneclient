from keystoneclient import base
from keystoneclient import utils

class VoMember(base.Resource):

    pass

class VoMembersManager(base.CrudManager):
    """Manager class for manipulating VO Roles."""

    resource_class = VoMember
    collection_key = 'users'
    key            = 'user'
    base_url       = 'OS-FEDERATION'


    def build_url(self, dict_args_in_out=None):
        """Build URL for VO memberships."""

        if dict_args_in_out is None:
            dict_args_in_out = {}

        vo_role_id = dict_args_in_out.pop('vo_role_id',
                                                    None)

        idp_id = dict_args_in_out.pop('idp_id', None)
        if vo_role_id:
            base_url = '/vo_roles/'.join([self.base_url, vo_role_id])
        else:
            base_url = self.base_url

        if idp_id:
            base_url += "/identity_providers/" + idp_id

        dict_args_in_out.setdefault('base_url', base_url)
        return super(VoMembersManager, self).build_url(dict_args_in_out)
    
    def build_base_url(self, vo_role):
        return self.base_url + '/%s' % base.getid(vo_role)
    
    def join(self, vo_name, pin, vo_role, **kwargs):
        """Join a VO Role.

        Utilize Keystone URI:
        POST /OS-FEDERATION/vo_members

        """
        url = "/OS-FEDERATION/vo_users"
        return super(VoMembersManager, self)._put(
            url,
            {
                "vo_request": {
                    "secret" : pin,
                    "vo_name" : vo_name,         
                    "vo_role" : vo_role,
                }
            },
            "vo_request")
        
    def get(self, vo_role, member_id):
        """List members with a VO role

        Utilize Keystone URI:
        GET /OS-FEDERATION/vo_roles/{vo_role_id}/members/{member_id}

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """

        return super(VoMembersManager, self).get(
            vo_role_id= base.getid(vo_role),
            member_id=base.getid(member_id),
            )

    def check(self, vo_role):
        """Check Virtual Organisation Membership

        Utilize Keystone URI:
        GET /OS-FEDERATION/vo_roles/{vo_role_id}/users

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        url = "/OS-FEDERATION/vo_roles/" + base.getid(vo_role) + "/users"
        return super(VoMembersManager, self)._get(
            url,
            "vo_request"
            )
            
    def list(self, vo_role, **kwargs):
        """List members with a VO role.

        Utilize Keystone URI:
        GET /OS-FEDERATION/vo_roles/{vo_role_id}/members

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoMembersManager, self).list(
            vo_role_id=base.getid(vo_role),
            **kwargs)
        
    def update(self, vo_role,
                     member,
                     idp,
                     new_vo_role,
                     **kwargs):
        """Switch VO roles for a user.

        Utilize Keystone URI:
        PATCH /OS-FEDERATION/vo_roles/{vo_role_id}/members/{user-id}/identity_providers/{idp_id}

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoMembersManager, self)._update(
            self.build_url(
                vo_role_id = base.getid(vo_role),
                member_id=base.getid(member),
                idp_id=base.getid(idp)
            ),
            {"new_vo_role_id" :base.getid(new_vo_role)},
            self.key,
            method='PATCH'
            **kwargs)

    def delete(self, vo_role, member, idp):
        """Remove VO role from user.

        Utilize Keystone URI:
        DELETE /OS-FEDERATION/vo_roles/{vo_role_id}/members/{user-id}/identity_providers/{idp_id}

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoMembersManager, self).delete(
            member_id=base.getid(member),
            idp_id=base.getid(idp),
            vo_role_id=base.getid(vo_role)
        )

    def resign(self, vo_role, member):
        """Resign from a VO Role.

        Utilize Keystone URI:
        DELETE /OS-FEDERATION/vo_members

        :param identity_provider: an object with identity_provider_id
                                  stored inside.

        """
        return super(VoMembersManager, self).delete(
            member_id=base.getid(member),
            base_url=self.build_base_url(vo_role))
