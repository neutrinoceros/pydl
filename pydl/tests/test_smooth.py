# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
#
def test_smooth():
    from ..smooth import smooth
    from numpy import arange, array, sin
    #
    # Test smooth function
    #
    x = 8.0*arange(100)/100.0 - 4.0
    noise = array([2.30610, -0.606922, -0.495611, 0.319969, -0.852573,
        -0.718530, -0.822457, -0.914747, -2.06190, -0.367282,
        -1.07346, 0.333589, -0.171405, 1.29557, 1.04241,
        0.745161, 1.12171, -1.68132,     1.33361,      1.09108,
        1.16230,    -0.663734,     0.819509,   -0.0675587,
        -1.30818,      1.65162,      1.54414,    -0.801843,      1.55333,
        -0.0529722,    -0.535589,     0.424731,     -1.01041,      1.78723,
        0.625269,    -0.770034,
        0.837806,    -1.29704,      1.84804,     0.331175,   -0.0432724,
        0.430578,     0.785313,    -0.243586,    -0.874319,     -1.18494,
        0.204993,    -0.620158,
        1.51457,      1.12941,     0.776386,      2.25176,      1.75678,
        0.327156,     0.530501,     0.648502,    0.0279251,    -0.395409,
        -0.341345,     0.339561,
        0.414343,    -0.513183,      1.23809,     -1.44090,     -1.94348,
        -0.443420,     0.483545,    -0.408526,   -0.0689184,    -0.568676,
        1.89727,     -1.54532,
        1.16730,     0.898135,     -1.21551,    -0.525567,   -0.0766497,
        1.47355,    -0.735265,     0.772411,     0.143568,    0.0425026,
        1.27208,     0.499760,
        0.718399,     0.577398,      1.79356,    -0.237896,     -1.87300,
        1.95981,   -0.0884865,    -0.872654,     0.133105,     -1.24190,
        0.465836,    -0.210268,
        0.675163,     -1.54661,    -0.993406,   -0.0257759])
    y = sin(x) + 0.1*noise
    s = smooth(y,5)
    assert s.shape == (100,)
    s_edge = smooth(y,5,True)
    assert s_edge.shape == (100,)
    s_w = smooth(y,1)
    assert (s_w == y).all()
