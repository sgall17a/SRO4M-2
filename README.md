# SRO4M-2
Simple serial based Micropython library for SR04M-2 waterproof ultrasonic distance sensor.

This work was based on a great post below:
https://wolles-elektronikkiste.de/hc-sr04-und-jsn-sr04t-2-0-abstandssensoren

I tried to simply re-write the C code above but it did not work.  So I simplified it even further and made it more "pythonic" or at least "Micropythonic"
I am now getting sensible results but it is still very much a work in progress.


I am new to this sensor. 
Mine is a cheap one from Aliexpress.  It has a single sensor which is attached to a board.  Similar ultrasonis have two sensors but this is for the single one.

I think there have been some variants to this device and maybe -2 suffix indicates a new variant.

Following th work from the link above I soldered a 4K7 resistor to the jumper near the electrolytic capacitors.  This puts it into continuous serial mode.

I think in the serial mode the speed of sound factor is calculated on the board. I have not properly tested it yet but the results seem to a reasonable estimated of distance in millimetres.

When I hold the sensor by hand the values jump around but seem to settle down to reasonable values.

I think in a real use case you will need to test for aberrant values and ignore them.

I plan to use to measure the depth of water in a rain water tank so that might be quite stable once I set it up.





