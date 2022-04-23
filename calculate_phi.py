import numpy as np

def calculate_phi(lon, lat):
	"""
	Calculate the Compton scatter angle phi which resulted in the specified
	post-scatter interaction location (Galactic lon psi, Galactic lat xi).

	Parameters
	_________
	lon : float
	      Galactic longitude in degrees.
	lat : float
	      Galactic latitude in degrees.

	Returns
	_______
	phi_deg
              Compton scatter angle in degrees.
	"""

	compt_scatt_z = 25
	origin = [0, 0]
	dist = np.sqrt( (lon - origin[0])**2 + (lat - origin[1])**2 )
	phi = np.arctan(dist/compt_scatt_z)
	phi_deg = np.rad2deg(phi)

	return phi_deg
