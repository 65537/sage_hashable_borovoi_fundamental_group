"""
Base for Classical Matrix Groups with GAP
"""

from sage.groups.matrix_gps.matrix_group_gap import MatrixGroup_gap
from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic

class NamedMatrixGroup_gap(NamedMatrixGroup_generic, MatrixGroup_gap):

    def __init__(self, degree, base_ring, special, sage_name, latex_string,
                 gap_command_string, category=None):
        """
        Base class for "named" matrix groups using LibGAP

        INPUT:

        - ``degree`` -- integer. The degree (number of rows/columns of
          matrices).

        - ``base_ring`` -- ring. The base ring of the matrices.

        - ``special`` -- boolean. Whether the matrix group is special,
          that is, elements have determinant one.

        - ``latex_string`` -- string. The latex representation.

        - ``gap_command_string`` -- string. The GAP command to construct
          the matrix group.

        EXAMPLES::

            sage: G = GL(2, GF(3))
            sage: from sage.groups.matrix_gps.named_group_gap import NamedMatrixGroup_gap
            sage: isinstance(G, NamedMatrixGroup_gap)
            True
        """
        from sage.libs.gap.libgap import libgap
        group = libgap.eval(gap_command_string)
        MatrixGroup_gap.__init__(self, degree, base_ring, group,
                                 category=category)
        self._special = special
        self._gap_string = gap_command_string
        self._name_string = sage_name
        self._latex_string = latex_string
