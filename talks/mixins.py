from django.core.exceptions import PermissionDenied

class EditOwnTalksMixin():
    def get_object(self, *args, **kwargs):
        obj = super(EditOwnTalksMixin, self).get_object(*args, **kwargs)
        if obj.author == self.request.user:
            return obj
        else:
            raise PermissionDenied
