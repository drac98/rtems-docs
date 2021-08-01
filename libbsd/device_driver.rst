.. SPDX-License-Identifier: CC-BY-SA-4.0

Device Driver
#################

Introduction
============

USB
===

USB Template
------------

USB Template driver is initialized based on the value of `hw.usb.template` 
sysctl variable. To set the variable use the `sysctlbyname` system call 
as follows in your application,

  .. code-block:: c
		
		int template = 1;
		sysctlbyname("hw.usb.template", NULL, NULL, &template, sizeof(template));

You can set the variable at runtime using the shell with the syctl utility.

  .. code-block:: shell
		
		sysctl hw.usb.template=1
		
NOTE: Template 1 is the CDC Ethernet.
