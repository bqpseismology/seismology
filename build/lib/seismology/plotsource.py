#! ~/.pyenv/shims/python

import numpy as np
import source as S
import matplotlib.pyplot as plt
import obspy.imaging.beachball as BL
plt.rcParams

# example 1
#
#points = S.sphere(r=5, n=1000)
#fc = S.spherical_to_cartesian(points)

#fig = plt.figure()
#ax = fig.gca(projection='3d')
##ax.set_aspect("equal")
#ax.plot_wireframe(fc[0], fc[1], fc[2], color="r")
#plt.show()


#moment = [1.0,1.0,1.0,0.0,0.0,0.0]
#print(type(moment))
#m = np.array([1.0,1.0,1.0,0.0,0.0,0.0])
#print(type(m))
#full_m = S.mt_full(m)
#decom_m = S.mt_angles(m)
#print(full_m)
#print(decom_m)
#ex = S.Aki_Richards(m)
#print(ex.mt)
##S.plot_seismicsourcemodel()
#G, XYZ = ex.radpat()
#print('{} {}' % (G, XYZ))
##ex.plot()

ex = S.SeismicSource([1,2,3,4,5,6])
#ex = S.SeismicSource([0.247,0.356,0.665,-0.418,-0.125,-0.029])
#ex = S.SeismicSource([-0.29,-4.12,4.41,0.858,0.447,1.01])
#ex.Aki_Richards.plot('P')
#ex.Aki_Richards.plot('P','b')
#ex.Aki_Richards.plot('P','q')
#ex.Aki_Richards.plot('P','s')
#ex.Aki_Richards.plot('P','f')
#ex.Aki_Richards.plot('P','p')

#ex.Vavryeuk.plot('P',)
#ex.Vavryeuk.plot('P','b')
#ex.Vavryeuk.plot('P','q')
#ex.Vavryeuk.plot('P','s')
#ex.Vavryeuk.plot('P','f')
ex.Vavryeuk.plot('P','p')
