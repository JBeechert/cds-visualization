import numpy as np
from calculate_phi import calculate_phi
from points import points

def test_phi_real():
	phis = []
	lons = np.arange(-180, 180+1, 1)
	lats = np.arange(-90, 90+1, 1)

	for lon in lons:
    		for lat in lats:
        		phis.append(calculate_phi(lon, lat))

	assert np.isreal(np.array(phis).all())


def test_phi_range():
	phis = []
	lons = np.arange(-180, 180+1, 1)
	lats = np.arange(-90, 90+1, 1)

	for lon in lons:
    		for lat in lats:
        		phis.append(calculate_phi(lon, lat))

	assert np.abs(np.array(phis).all()) <= 360.


def test_points():
	lon = 25
	lat = 25
	x, y, z = points(lon, lat)

	assert isinstance(x, list)
