from __future__ import print_function
from __future__ import division
# Authors:
#     Loic Gouarin <loic.gouarin@math.u-psud.fr>
#     Benjamin Graille <benjamin.graille@math.u-psud.fr>
#
# License: BSD 3 clause

"""
Example of a two velocities scheme for the advection equation in 1D
"""
import sympy as sp
import pyLBM
u, X = sp.symbols('u, X')
d = {
    'dim':1,
    'scheme_velocity':1.,
    'schemes':[
        {
            'velocities': [1, 2],
            'conserved_moments':u,
            'polynomials': [1, X],
            'equilibrium': [u, .5*u],
            'relaxation_parameters': [0., 1.9],
        },
    ],
}
s = pyLBM.Scheme(d)
print(s)
print(s.generator.code)
