from keystoneclient import base
from keystoneclient import utils

class VoRole(base.Resource):
    pass

class VoRolesManager(base.CrudManager):
    """Manager class for manipulating VO Roles."""

    resource_class = VoRole
    collection_key = 'vo_roles'
    key            = 'vo_role'
    base_url       = 'OS-FEDERATION'



    def create(self, vo_name, vo_role_name, pin, description="", enabled=False, automatic_join=False, **kwargs):
        """Create Role object.

        Utilize Keystone URI:
        PUT /OS-FEDERATION/vo_roles

        """
        return super(VoRolesManager, self).create(
            automatic_join=automatic_join,
            description=description,         
            enabled=enabled,
            pin=pin,
            vo_name=vo_name,
            vo_role=vo_role_name,
            vo_is_domain=True,
            **kwargs)

    def list_all(self, **kwargs):
        """List all VO Roles.

        Utilize Keystone URI:
        GET /OS-FEDERATION/vo_roles/all

        """
        return super(VoRolesManager, self).list(**kwargs)
            
    def get(self, vo_role):
        """Fetch Identity Provider object

        Utilize Keystone URI:
        GET /OS-FEDERATION/vo_roles/{vo_role_id}

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoRolesManager, self).get(
            vo_role_id= base.getid(vo_role))
            

    def list(self, **kwargs):
        """List all VO Roles.

        Utilize Keystone URI:
        GET /OS-FEDERATION/vo_roles

        """
	#Ioram 31/10/2014
	#print "IORAM VoRoles.List"
        return super(VoRolesManager, self).list(**kwargs)

    def update(self, vo_role,
                     automatic_join=None,
                     description=None,
                     enabled=None,
                     pin=None,
                     vo_is_domain=None,
                     vo_name=None,
                     vo_role_name=None,
                     **kwargs):
        """Update VO role.

        Utilize Keystone URI:
        PATCH /OS-FEDERATION/vo_roles/{vo_role_id}

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoRolesManager, self).update(
            vo_role_id=base.getid(vo_role),
            vo_role = vo_role_name,
            vo_name = vo_name,
            description=description,
            pin=pin,
            enabled=enabled,
            automatic_join=automatic_join,
             **kwargs)

    def delete(self, vo_role):
        """Delete VO role.

        Utilize Keystone URI:
        DELETE DELETE /OS-FEDERATION/vo_roles/{vo_role_id}

        :param vo_role: an object with vo_role_id
                                  stored inside.

        """
        return super(VoRolesManager, self).delete(
            vo_role_id=base.getid(vo_role))
