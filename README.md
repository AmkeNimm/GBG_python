# GBG_python
The program plot.py will gnerate a colormap plot of time-resolved scattering data both in q-space and R-space.

Input file is a matlab file, containing q ('q'), delay time ('Delay') and the scattering data ('AllTTDelay') saved in according fields.

Data file is defined by filepath and filename. Example file is found in this directory.

* Input
    * H20_long.mat: example experimental data
				* q: q-range
				* Delay: timepoints
				* AllTTDelay: difference scattering data
				
* necessary packages:
		* numpy
		* matlab.engine
		* matplotlib
		* scipy
             
         
