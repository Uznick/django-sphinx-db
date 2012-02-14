
# TODO: make database name configurable.
class SphinxRouter(object):
    """
    Routes database operations for Sphinx model to the sphinx database connection.
    """
    def db_for_read(self, model, **kwargs):
        from django_sphinx.backend.models import SphinxModel
        if issubclass(model, SphinxModel):
            return 'sphinx'

    def db_for_write(self, model, **kwargs):
        from django_sphinx.backend.models import SphinxModel
        if issubclass(model, SphinxModel):
            return 'sphinx'

    def allow_relation(self, obj1, obj2, **kwargs):
        # Allow all relations...
        return True