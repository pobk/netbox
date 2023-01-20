from distutils.util import strtobool
from django.db.models import CharField, Lookup


class Empty(Lookup):
    """
    Filter on whether a string is empty.
    """
    lookup_name = 'empty'

    def convert_parm_to_bool(self, param):
        try:
            ret = str(strtobool(param))
        except ValueError:
            ret = "false"

        return ret

    def as_sql(self, qn, connection):
        lhs, lhs_params = self.process_lhs(qn, connection)
        rhs, rhs_params = self.process_rhs(qn, connection)
        rhs_params = [str(self.convert_parm_to_bool(param)) for param in rhs_params]
        params = lhs_params + rhs_params
        s = f'CAST(LENGTH({lhs}) AS BOOLEAN) != {rhs}'
        return (s, params)


CharField.register_lookup(Empty)
