.. _installation:

================
Install AutoCNet
================


Download and setup:
-------------------
(**While these steps are not necessary, it is highly recommended that you follow them.**)

Begin by accessing the Anaconda download website at:

- https://www.continuum.io/downloads.

Choose the appropriate version for your system, this will be the linux version if you are on Fedora. Next, follow the instructions on Anacondas website for installation onto your system.

After the installer has finished, it will ask to prepend the path to your .bashrc file. You'll want to say yes as this is necessary for the rest of the installation process.
If you don't you will need to access your .bashrc file and add:

- export PATH="(path to anaconda file)/anaconda3/bin:$PATH"

Replacing the (path to anaconda) with the appropriate directory sequence that points to the anaconda3 file.

Next, create and activate a new conda environment using these commands::

    $conda create --name enter environment name
    $source activate environment name

After that finishes you'll have the base setup for a new Anaconda environment that can contain AutoCnet.

Installing AutoCnet:
--------------------
To start enter::

    $ placeholder command

This command accesses a binstar that holds the Autocnet package along with all of the other packages that AutoCnet uses.

When it finishes downloading, you have installed AutoCnet and setup your anaconda environment.