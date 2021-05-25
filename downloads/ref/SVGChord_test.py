import datetime
import sys

import SVGChordV2_2
from SVGChordV2_2 import chord

#
# SVGChordTest.py
#
# (C) 2011 joebrown.org.uk
#
# 13th October 2011 JWB
#
# Generate some SVG-based Guitar Chord diagrams and
# a display page for them. The chords produced are
# also zipped into 3 zip files.
#
# The finished HTML file is named: DisplaySVGChords.html
#
#

# open output file to accept chord svg statements
handle = open("DisplaySVGChords.html", 'w')
if handle == None:
    #die("Failed to open output file")
    print("Failed to open output file")
    exit()
    
handle.write( "<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN>\r\n")
handle.write( "<!DOCTYPE svg PUBLIC '-//W3C//DTD SVG 1.1//EN' 'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>\r\n")
handle.write( "<HTML><HEAD><META HTTP-EQUIV='CONTENT-TYPE' CONTENT='text/html; charset=windows-1252'>\r\n")
handle.write(	"<TITLE>SVG Guitar Chord Diagrams</TITLE>\r\n")
handle.write( "<META NAME='GENERATOR' CONTENT='SVGChordTest.py V1.00  (Win32)'>\r\n")
handle.write(	"<META NAME='AUTHOR' CONTENT='Joe Brown'>\r\n")
now = datetime.datetime.now()
handle.write( "<!-- On UTC: " + now.strftime("%Y-%m-%d %H:%M") + " -->\r\n")
handle.write( "</HEAD><BODY LANG='en-GB' DIR='LTR'>\r\n")

handle.write( "<p><table><caption> <b>Some basic chords in E</b></caption<tbody><tr>")

# some basic chords in E
handle.write( "<td><img src='E_1.svg'/></td>") 
c = chord([0, 2, 2, 1, 0, 0,  0,   0,  'R',   'E',   "First posn E", "E_1.svg"])
c.setscalepercent(200)
c.draw()
handle.write( "<td><img src='Emaj7_1.svg'/></td>") 
c = chord([0, 2, 1, 1, 0, 0,  0,   0,  'R',   'Emaj7',   "First posn Emaj7", "Emaj7_1.svg"])
c.draw()
handle.write( "<td><img src='E7_1.svg'/></td>") 
c = chord([0, 2, 0, 1, 0, 0,  0,   0,  'R',   'E7',   "First posn E7", "E7_1.svg"])
c.draw()
handle.write( "<td><img src='E7_1_2.svg'/></td>") 
c = chord([0, 2, 0, 1, 3, 0,  0,   0,  'R',   'E7',   "First posn (var 2) E7", "E7_1_2.svg"])
c.draw()
handle.write( "<td><img src='Esus4_1.svg'/></td>") 
c = chord([0, 2, 2, 2, 0, 0,  0,   0,  'R',   'Esus4',   "First posn Esus4", "Esus4_1.svg"])
c.draw()
handle.write( "<td><img src='E6_1.svg'/></td>") 
c = chord([0, 2, 2, 1, 2, 0,  0,   0,  'R',   'E6',   "First posn E6", "E6_1.svg"])
c.draw()
handle.write( "<td><img src='E7sus4_1.svg'/></td>") 
c = chord([0, 2, 0, 2, 0, 0,  0,   0,  'R',   'E7sus4',   "First posn E7sus4", "E7sus4_1.svg"])
c.draw()
handle.write( "<td><img src='E9_1.svg'/></td>") 
c = chord([0, 2, 0, 1, 3, 2,  0,   0,  'R',   'E9',   "First posn E9", "E9_1.svg"])
c.draw()
handle.write( "<td><img src='E5pow_1.svg'/></td>") 
c = chord([0, 2, 2, 'x', 'x', 'x', 0,   0,  'R',   'E5',   "First posn E5 power chord", "E5pow_1.svg"])
c.draw()
handle.write( "<td><img src='E5pow_1_L.svg'/></td>") 
c = chord([0, 2, 2, 'x', 'x', 'x', 0,   0,  'L',   'E5 (L)',   "First posn E5 power chord", "E5pow_1_L.svg"])
c.draw()
handle.write( "<td><img src='E11_5.svg'/></td>") 
c = chord([0, 7, 6, 7, 5, 5,  0,   4,  'R',   'E11',   "Fifth posn E11", "E11_5.svg"])
c.setscalepercent(250);
c.draw()
handle.write( "<td><img src='E11_5_L.svg'/></td>") 
c = chord([0, 7, 6, 7, 5, 5,  0,   4,  'L',   'E11 (L)',   "Fifth posn E11 - left-handed", "E11_5_L.svg"])
c.draw()

handle.write( "</tr></tbody></table><BR/><BR></p>\r\n")

handle.write( "<p><table><caption> <b>Some basic chords in A</b></caption<tbody><tr>")

# some basic chords in A
handle.write( "<td><img src='A_1.svg'/></td>") 
c = chord([0, 0, 2, 2, 2, 0,  0,   0,  'R',   'A',   "First posn A", "A_1.svg"])
c.draw()
handle.write( "<td><img src='Amaj7_1.svg'/></td>") 
c = chord([0, 0, 2, 2, 2, 4,  0,   0,  'R',   'Amaj7',   "First posn Amaj7", "Amaj7_1.svg"])
c.draw()
handle.write( "<td><img src='A7_1.svg'/></td>") 
c = chord([0, 0, 2, 0, 2, 0,  0,   0,  'R',   'A7',   "First posn A7", "A7_1.svg"])
c.draw()
handle.write( "<td><img src='A7_1_2.svg'/></td>") 
c = chord([0, 0, 2, 2, 2, 3,  0,   0,  'R',   'A7',   "First posn (var 2) A7", "A7_1_2.svg"])
c.draw()
handle.write( "<td><img src='Asus4_1.svg'/></td>") 
c = chord([0, 0, 2, 2, 3, 0,  0,   0,  'R',   'Asus4',   "First posn Asus4", "Asus4_1.svg"])
c.draw()
handle.write( "<td><img src='A6_1.svg'/></td>") 
c = chord([0, 0, 2, 2, 2, 2,  0,   0,  'R',   'A6',   "First posn A6", "A6_1.svg"])
c.draw()
handle.write( "<td><img src='A7sus4_1.svg'/></td>") 
c = chord(['X', 0, 2, 0, 3, 0,  0,   0,  'R',   'A7sus4',   "First posn A7sus4", "A7sus4_1.svg"])
c.draw()
handle.write( "<td><img src='A9_1.svg'/></td>") 
c = chord(['X', 0, 2, 4, 2, 3,  0,   0,  'R',   'A9',   "First posn A9", "A9_1.svg"])
c.draw()
handle.write( "<td><img src='A5pow_1.svg'/></td>") 
c = chord(['X', 0, 2, 2, 'x', 'x', 0,   0,  'R',   'A5',   "First posn A5 power chord", "A5pow_1.svg"])
c.draw()
handle.write( "<td><img src='A5pow_1_L.svg'/></td>") 
c = chord(['X', 0, 2, 2, 'x', 'x', 0,   0,  'L',   'A5 (L)',   "First posn A5 power chord", "A5pow_1_L.svg"])
c.draw()
handle.write( "<td><img src='A11.svg'/></td>") 
c = chord([5, 4, 5, 'X', 3, 'X',  0,   0,  'R',   'A11',   "A11", "A11.svg"])
c.draw()
handle.write( "<td><img src='A11_L.svg'/></td>") 
c = chord([5, 4, 5, 'X', 3, 'X',  0,   0,  'L',   'A11 (L)',   "A11 - left-handed", "A11_L.svg"])
c.draw()


handle.write( "</tr></tbody></table><BR/><BR></p>\r\n")

# miscellany

handle.write( "<p><table><caption> <b>A miscellany displaying the versatility of the generator</b></caption<tbody><tr>")
handle.write( "<td><img src='F_1.svg'/></td>") 
c = chord([1, 3, 3, 2, 1, 1,  0,   0,  'R',   'F',   "F first position (usually barre chord)", "F_1.svg"])
c.draw()
handle.write( "<td><img src='G_1.svg'/></td>") 
c = chord([3, 5, 5, 4, 3, 3,  0,   0,  'R',   'G',   "G barre chord", "G_1.svg"])
c.setscalepercent(175);
c.draw()
handle.write( "<td><img src='A_2.svg'/></td>") 
c = chord([5, 7, 7, 6, 5, 5,  0,   0,  'R',   'A',   "A barre chord", "A_2.svg"])
c.draw()
handle.write( "<td><img src='A_2_C2.svg'/></td>") 
c = chord([5, 7, 7, 6, 5, 5,  2,   0,  'R',   'A',   "A barre chord", "A_2_C2.svg"])
c.draw()
handle.write( "<td><img src='B_1.svg'/></td>") 
c = chord([7, 9, 9, 8, 7, 7,  0,   0,  'R',   'B',   "B barre chord", "B_1.svg"])
c.draw()
handle.write( "<td><img src='B_1_cut6.svg'/></td>") 
c = chord([7, 9, 9, 8, 7, 7,  0,   6,  'R',   'B',   "B barre chord", "B_1_cut6.svg"])
c.setscalepercent(80);
c.draw()
handle.write( "<td><img src='B_2.svg'/></td>") 
c = chord(['X', 'X', 4, 4, 4, 7,  0,   3,  'R',   'B',   "Partial B", "B_2.svg"])
c.draw()
handle.write( "<td><img src='E2_14_C.svg'/></td>") 
c = chord([0, 0, 0, 14, 0, 14, 2,   12,  'R',   'E_joni',   "For 'Chelsea Morning' by Joni Mitchell. Tune guitar DADF#AD", "E2_14_C.svg"])
c.draw()

handle.write( "<td><img src='E2_14.svg'/></td>") 
c = chord([0, 0, 0, 14, 0, 14, 2,   0,  'R',   'E_joni',   "For 'Chelsea Morning' by Joni Mitchell. Tune guitar DADF#AD", "E2_14.svg"])
c.setscalepercent(500);
c.setchordtitlecolour('black');
c.draw()

handle.write( "</tr></tbody></table><BR/><BR></p>\r\n")

handle.write( "<BR/>The above SVG Chord files are available in 3 zip files as follows:<BR/>\r\n")

handle.write("<a href='SVGChordsinA.zip'>SVG Chords in A</a><BR/>\r\n")
handle.write( "<a href='SVGChordsinE.zip'>SVG Chords in E</a><BR/>\r\n")
handle.write( "<a href='SVGChordsMisc.zip'>Misc SVG Chords</a><BR/>\r\n")

handle.write( "</BODY></HTML>\r\n")
handle.close()


##=================================================================================================================================================

## "And Moses came back from the desert after 40 days, and 40 nights, And his wife said 'Moses, I am with child. What steps are you going to take?"
## "And Moses replied: 'Great big bloody ones, back to the Desert!'" (source: The Pitman's Bible)

##=================================================================================================================================================

