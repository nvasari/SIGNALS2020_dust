# SIGNALS 2020 lectures: Dust in the ISM.
17th August, 2020

To get set up, clone this repository:

	git clone https://github.com/nvasari/SIGNALS2020_dust.git

In [CANFAR](https://signals.canfar.net/) or your machine, copy the notebooks so that you do not
lose your work when you pull the new notebooks from github:

	mkdir $HOME/dust_notebooks
	cd $HOME/dust_notebooks
	cp $HOME/SIGNALS2020_dust/*.ipynb .
	ln -s $HOME/SIGNALS2020_dust/example_data .
	ln -s $HOME/SIGNALS2020_dust/natastro .

These notebooks are still being updated. So far only the standard
python libraries are being used (astropy, matplotlib, numpy). If you
are a python3 user chances are they are already installed, but please
make sure they are working. If working from CANFAR, there is no need
to worry.

To update with the newest versions of these files, do

	cd $HOME/SIGNALS2020_dust
	git pull

And copy the new notebooks to your workspace:

	cd $HOME/dust_notebooks
	cp $HOME/SIGNALS2020_dust/*.ipynb .

