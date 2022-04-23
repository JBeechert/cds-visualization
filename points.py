def points(lon, lat):
    """
    Define x, y, z coordinates of the first, second, and third interactions 
    in the matplotlib recreation of Figure 3 in Zoglauer et al. 2021.
    
    The first index is the photon origin.
    The second index is the Compton scatter location.
    The third index is the post-scatter location.
    
    Parameters
    ----------
    lon : float
          Galactic longitude in degrees.
    lat : float
          Galactic latitude in degrees.
         
    Returns
    -------
    x, y, z
        Each is an array of floats encoding the scatter locations.
    
    """
    x = [0, 0, lon]
    y = [0, 0, lat]
    z = [55, 25, 0]
    
    return x, y, z
