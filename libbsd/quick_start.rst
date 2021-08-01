.. COMMENT: Written by Husni Faiz
.. SPDX-License-Identifier: CC-BY-SA-4.0

Quick Start
###########

The LibBSD is a standalone repository and needs to be built
separately.

The repository can be found here: https://git.rtems.org/rtems-libbsd/

Manual LibBSD Build
===================

Pre-requisites:

- Built the tool set for your BSP

- Built and installed RTEMS for your BSP with networking disabled and 
  POSIX API enabled.

The following guide uses the Beagle BSP.

Get the RTEMS LibBSD source

  .. code-block:: shell

        git clone https://git.rtems.org/rtems-libbsd/
        cd rtems-libbsd

Get the RTEMS Waf build systems

  .. code-block:: shell

        git submodule init
        git submodule update rtems_waf

Configure the build.  

  .. code-block:: shell

        ./waf configure --prefix=/path/to/rtems/prefix \
        --rtems-bsps=arm/beagleboneblack \
        --buildset=buildset/default.ini

Build and Install

  .. code-block:: shell
     
        ./waf
        ./waf install
