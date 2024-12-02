#!/usr/bin/env -S bash -e
# GMT modern mode bash template
# Date:    2024-11-25T18:48:10
# User:    suphakornpoobua
# Purpose: Purpose of this script
set -e
export GMT_SESSION_NAME=11	

range="-126/-123.5/44/45"
proj="M12c" 
wet="153/204/255"

gmt makecpt -Cdem2 -T-100/6000/100 -Z -D > topo.cat
gmt begin Oregon png
	gmt set FORMAT_GEO_MAP ddd.x
	gmt basemap -J$proj -R$range -Ba1f0.5 -BWeSn
	gmt grdimage @earth_relief_01s -I+d

	# Add colorbar to the TR and shift to the right by 2 cm
	# Set color width to be 6 cm
	gmt colorbar -DjTR+o-1c/0c+w6c+ml -Ba500+l"Earth relief (m)"

	# Plot the benchmark location with a red inverted triangle and label
	echo "-124.9670 44.3666" | gmt plot -Si0.3c -Gred -W0.5p,black -N
	echo "-124.9670 44.3666 O4 benchmark" | gmt text -F+f8p,Helvetica-Bold,black+jLB -Dj0.2c/0.2c

gmt end show
