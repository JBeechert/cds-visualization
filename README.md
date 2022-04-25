# cds-visualization
Visualize the Compton Data Space (CDS)

## What is the CDS?

The Compton Data Space (CDS) is a data space developed specifically for Compton telescopes which parameterizes photon interactions by their scattering angles. 
The CDS was first conceptualized by the COMPTEL collaboration as the "COMPTEL Data Space" and is more broadly used today in several Compton telescope experiments as the "Compton Data Space." 

The CDS is spanned by three parameters which specify the observed Compton scattering process as well as the measured changed state of the incident gamma-ray: the Compton scattering angle describes the former and the latter is given by the polar and azimuthal directions of the scattered gamma-ray in Galactic coordinates. These three parameters describe the arrival direction of the gamma-ray. 

Each incident photon is uniquely defined by these three parameters in the CDS. In contrast to the degenerate image space of Compton telescopes with overlapping circles projected on the sky, the CDS is a well-defined and powerful space for disciminatory analyses which do not require imaging. 

The Jupyter notebook "cds-vis.ipynb" is designed to help users explore the CDS and understand how the scattering angles map to this useful data space. Users can 
interact with figures via ```matplotlib``` and ```plotly``` by changing scattering angles. The ```plotly``` figure can be opened in a new browser tab with ```dash``` and be saved as an HTML file for later use. The ```plotly``` figure depends on scattering angles stored in a ```pandas``` database, which is generated in the notebook. 

The notebook also executes checks of the functions which calculate scatter point locations and the Compton scattering angle with ```pytest```.

Future revisions of this notebook will include visualizations of the response matrix of the Compton Spectrometer and Imager (COSI). This is important for understanding how Compton imaging works. 
For now, an explanation of imaging procedures is provided in words. 
