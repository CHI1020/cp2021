#
# SVG Chord Diagram generation in Python
#
# (C) 2011,2012 joebrown.org.uk
#
# Loosely based on the excellent 'Draw Guitar Chords using PHP' (a PNG Chord generator) by Tony Pottier,
# and my PHP SVG Chord Generator, this version is for Python, a more-or-less functional replacement for my php code.
#
# The code is '1st cut', and needs re-factoring, but it does work.
#
# V2.10 started 14th October 2011
# 
# - rudimentary set scaling implemented
# - break out some literals
# - allow chord title colour set
# 
# V2.00 Working 11th October 2011
#
# - Until this statement is removed, this class requires extensive re-factoring - however it does work! JWB 11th Oct 2011
#
# - Added leftie support 12th Oct 2011 - see my Blog on the generator for thoughts on childhood warnings such as:
# - 'they never made anything for left-handed folk, Joe.'
#
# - added barre chord indication
#
# - supports 'totem-pole' as well as cut-to-size format diagrams
#
# - comments for extra facilities/functionality are welcome if these are legal, and will not damage sensitive parts of my body.
# 
# - negative remarks from 'elite' programmers? - save your self-aggrandisement for another audience, I'm not blanking interested.
#
# Freely distributable/copyable if acknowledgements given.
# Commercial use prohibited without permission.
#
# History of Python version:
# Completed 1st cut code (straight copy of php version) 19th June 2012 @ 8:12am
# saved as: SVGChordV2_1.py
#
# JWB 19th June 2012 @ 14:52 - version SVGChordV2_2.py
#
# fixed several problems. Now generates all chords correctly
# using SVGChordTest.py
#

import datetime

class chord():

    ##
    # Set scale in percent
    # with 100 being no scaling.
    # 
    # 
    # @param int v
    #
    def setscalepercent(self,v):
        v = float(v)
        if v > 0: 
            self.scale = v
        else: 
            #throw new Exception('Strictly positive integers only')
            print('Strictly positive integers only')
            exit()
    #
    # Set chord name colour
    # with 100 being no scaling.
    # 
    # 
    # @param string v
    #
    def setchordtitlecolour(self,v): 
        if v != "": 
            ChordnameFill = v
        else: 
            #throw new Exception('setchordtitlecolour needs the name of a colour')
            print('setchordtitlecolour needs the name of a colour')
            exit()


    def __init__(self, data):
        # ensure no DERIVED property values are initialised here
        # do in draw() routine instead
        if data != None:
            self.scale = 100 # default percentage scaling = 1

            self.OpenStringIndicatorFontSize = 12
            self.dotradius = 2
            self.OSIYToChordNameY = 7
            self.centrefontonstringX = 2.5
            self.nutlinewidth = 0.5
            self.barrestrokewidth = 1
            self.fretstrokewidth = 0.3   # increase from V2.0
            self.stringstrokewidth = 0.3 # ditto
            self.FretStartCXDiff = 4
            self.OSIYToFirstFretY = 2

            ###########################
            #data = data

            self.barre = "FALSE"
            self.barrepos = 25 # a very high fret posn

            self.CommentChordname =   "\r\n<!-- Chord name -->\r\n"

            # enclosing rectangle for rendering the shape.
            self.width = 80  # this will be scaled
            self.height = 75 # initial value only - totem-pole chords will increase this

            # Chord name co-ordinates
            self.ChordnameX = 10
            self.ChordnameY = 10

            # chord name font etc.
            self.ChordnameFontSize = 12
            self.ChordnameFill = "red"

            self.numFrets = 6 # excluding 'nut' or capoed fret - totem-pole chords will increase this

            self.stringXspacing = 10 #  X distance between each string
            self.fretYspacing = 10 # Y distance between each fret

            self.nutX1 = 5 # top left corner of fretboard (on RH player's guitar)
                
            self.FretStartFill = "black"
            self.FretStartFontSize = 12
            self.FretStartFontStyle = "italic"

            self.numstrings = 6
            self.stuff = data
            self.chord = [] # will hold the six fret positions

            # extract chord !!! 6 strings assumed at present 
            for i in range(self.numstrings):
                # content can be either numeric digits , 'X' or it's lower-case cousin 'x'
                self.chord.append(self.stuff[i]) # the string fret posns are the first six items in the input data
                # ok @ 8:45am print chord   
            # how many strings are there? Currently we deal only with 6 - this test needs to move back up in code when numof strings <> 6 is catered for
            #numstrings = count(chord)
            if self.numstrings != 6: # TODO !!! break out literals
                print("Currently, SGV Chord Generator V2.00 can only cope with 6 strings. I'd complain - bitterly.")
                exit()
            # extract other properties
            self.Capo = self.stuff[6] # need number
            #print(Capo)

            self.Cut = self.stuff[7]  # need a number
            #print(Cut)
            self.hand = self.stuff[8] # Right or Left handed? need R,r.L or l. Nothing else will do man.
            #print(hand)
            if self.hand != 'R' and self.hand != 'r' and self.hand != 'L' and self.hand != 'l':
                print("You must indicate whether the diagram is for a left-handed (L or l), or right-handed (R or r) player. Sorry Ambi's are not catered for.")
                exit()
            self.Chordname = self.stuff[9] # need valid text
            #print(self.Chordname)
            self.Comment = "<!-- " + self.stuff[10] + " -->\r\n" # need valid text
            #print(self.Comment)
            self.Myfile = self.stuff[11] # need valid text
            #print(self.Myfile)
        else: 
            #throw new Exception('Fail: You must provide an array in the constructor')
            print('Fail: You must provide an array in the constructor')
            exit()

    def draw(self):
        if (self.scale != 100):
            # do any necessary scaling
            self.width = self.width * (self.scale / 100) #80
            self.height = self.height * (self.scale / 100) #75 # initial value only - totem-pole chords will increase this


            # chord name font etc.
            self.ChordnameFontSize = self.ChordnameFontSize * (self.scale / 100) # 10
            self.FretStartFontSize = self.FretStartFontSize * (self.scale / 100) #12
            self.dotradius = self.dotradius * (self.scale / 100) 

            self.stringXspacing = self.stringXspacing * (self.scale / 100) #10 #  X distance between each string
            self.fretYspacing = self.fretYspacing * (self.scale / 100) #10 # Y distance between each fret


            self.OpenStringIndicatorFontSize = self.OpenStringIndicatorFontSize * (self.scale / 100)
            self.OSIYToChordNameY = self.OSIYToChordNameY * (self.scale / 100)
            self.centrefontonstringX = self.centrefontonstringX * (self.scale / 100)

            # exceptions for less than 100% scaling
            # for things that otherwise would get very teeny-weeny - or squashed - or bits missing - or missing altogether you get the picture.
            if (self.scale > 100):
                self.nutX1 = 5 * (self.scale / 100) 
                # Chord name co-ordinates
                self.ChordnameX = 10 * (self.scale / 100) 
                self.ChordnameY = 8 * (self.scale / 100) 
                self.nutlinewidth = self.nutlinewidth * (self.scale / 100)
                self.barrestrokewidth = self.barrestrokewidth * (self.scale / 100)
                self.fretstrokewidth = self.fretstrokewidth * (self.scale / 100)
                self.stringstrokewidth = self.stringstrokewidth * (self.scale / 100)
                self.FretStartCXDiff = self.FretStartCXDiff * (self.scale / 100)
            #---------------- end of scaling ---------------------------------
                
        # style for 1st fret/nut - TODO !!! break out literals
        self.nutStyle = "stroke:rgb(0,0,0);stroke-width:nutlinewidth"

        # Co-ords of open/unused strings  characters
        self.OpenStringIndicatorY = self.ChordnameY + self.OSIYToChordNameY

        self.fretFirstY = self.OpenStringIndicatorY + self.OSIYToFirstFretY
        
        self.nutY1 = self.fretFirstY

        # top right corner of fretboard (on RH player's guitar)
        self.nutX2 = self.nutX1 + ((self.numstrings - 1) * self.stringXspacing)
        #derived nutY2
        self.nutY2 = self.nutY1

        # for fret string info posn.
        self.FretStartX = self.nutX2 + 5 # !!!!!
        self.FretStartY = self.fretFirstY + 2 # !!!

        #self.nutY1 = self.fretFirstY

        # !!! Sort out this silly nuts business !!!
        
        # top right corner of fretboard (on RH player's guitar)
        #self.nutX2 = self.nutX1 + (self.numstrings - 1) * self.stringXspacing
        #self.nutY2 = self.nutY1

           
        self.NutLine =  "<line x1='" + str(self.nutX1) + "' y1='" + str(self.nutY1) + "' x2='" + str(self.nutX2) + "' y2='" + str(self.nutY2) + "' style='" + self.nutStyle + "' />\r\n"

        # style for all other frets
        self.fretstyle = "stroke:rgb(0,0,0);stroke-width:" + str(self.fretstrokewidth) 
        # style for strings
        self.stringstyle = "stroke:rgb(0,0,0);stroke-width:" + str(self.stringstrokewidth)

        # start X for all frets
        self.fretsX1 = self.nutX1
        # finish X for all frets
        self.fretsX2 = self.nutX1 + (self.stringXspacing * 5)


        # start Y for all strings
        self.stringsY1 = self.fretFirstY # 22
        # finish Y for all strings
        self.stringsY2 = self.stringsY1 + (self.fretYspacing * (self.numFrets - 1)) # initial value only 


        # derived output line for Chord name.
        self.ChordNameLine = "<text x='" + str(self.ChordnameX) + "' y='" + str(self.ChordnameY) + "' font-size='" + str(self.ChordnameFontSize) + "' fill='" + self.ChordnameFill + "'>" + self.Chordname + "</text>\r\n"

        # form text indicating capo position, if any
        if self.Capo != 0:
            self.FretStartText = str(self.Capo) + "fr"
        else:
            self.FretStartText = ""
        
        self.FretStartPositionLine = "<text x='" + str(self.FretStartX) + "' y='" + str(self.FretStartY) + "' font-size='" + str(self.FretStartFontSize) + "' fill='" + self.FretStartFill + "' font-style='" + self.FretStartFontStyle + "'>" + self.FretStartText + "</text>\r\n"

        # open output file to accept chord svg statements
        handle = open(self.Myfile, 'w')
        if handle == None:
            print("Failed to open output file")
            #die("Failed to open output file") #  Myfile ???
            exit()
        else:
            print("file opened " + self.Myfile)
            print(handle)
            

        # begin output of svg tagged XML
        # need to check whether to change default height of containing rectangle and length of strings etc.
        for i in range(self.numstrings):
            if not (self.chord[i] == 'x' or self.chord[i] == 'X' or self.chord[i] == 0):
                spos = self.chord[i]
                if self.Cut != 0:
                    if spos >= self.Cut:
                        adj = self.Capo
                        if adj == 0:
                            adj = 2 # !!!
                    spos = (spos - self.Cut) + adj
                elif self.Capo != 0:
                    spos = spos - self.Capo
                cx = self.nutX1 + (i * self.stringXspacing)
                cy = (self.nutY1 - 5) + (spos * self.fretYspacing) # !!! literal alert!
                while cy > self.stringsY2: # need to lengthen chord?
                    self.numFrets += 1 # adjust num of frets needed
                    # calculate new length of strings
                    self.stringsY2 = self.stringsY1 + (self.fretYspacing * (self.numFrets - 1))
                    # following is important - changes rectangle chord shape sits in, otherwise chord will only partially render
                    self.height = self.height + self.fretYspacing

        # write the svg file header
        handle.write("<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='" + str(self.width) +"' height='" + str(self.height) + "' >\r\n")
        handle.write("<!-- This file was auto-produced using Python SVG Chord generator V2.10 (C) 2012 joebrown.org.uk -->\r\n")
        now = datetime.datetime.now()
        
        handle.write( "<!-- On UTC: " + now.strftime("%Y-%m-%d %H:%M") + " -->\r\n")
        handle.write( "<!-- All rights of the author are reserved -->\r\n\r\n")
        handle.write( self.Comment)
        handle.write ( self.CommentChordname)
        handle.write ( self.ChordNameLine)

        handle.write ( "\r\n<!-- fret start position (capo) - may be empty -->\r\n")
        if self.Capo != 0:
            handle.write( self.FretStartPositionLine)
        # Now, only show 'standard' fret positions on 'totem-pole' diagrams! i.e. not cut-down ones
        if self.Cut == 0:
            if self.numFrets > 5:
                # indicate fret 5 posn
                handle.write ( "\r\n<!-- fret 5 position -->\r\n")
                fretY = self.FretStartY + ( (5  - (self.Capo + self.Cut)) * self.fretYspacing)
                frLine = "<text x='" + str(self.FretStartX) + "' y='" + str(fretY) + "' font-size='" + str(self.FretStartFontSize) + "' fill='" + self.FretStartFill + "' font-style='" + self.FretStartFontStyle + "'>5fr</text>\r\n"
                handle.write( frLine)
            if self.numFrets > 7:
                # indicate fret 7 posn
                handle.write ( "\r\n<!-- fret 7 position -->\r\n")
                fretY = self.FretStartY + ( (7  - (self.Capo + self.Cut)) * self.fretYspacing)
                #frLine = "<text x='FretStartX' y='fretY' font-size='FretStartFontSize' fill='FretStartFill' font-style='FretStartFontStyle'>7fr</text>\r\n"
                frLine = "<text x='" + str(self.FretStartX) + "' y='" + str(fretY) + "' font-size='" + str(self.FretStartFontSize) + "' fill='" + self.FretStartFill + "' font-style='" + self.FretStartFontStyle + "'>7fr</text>\r\n"
                handle.write( frLine)
            if self.numFrets > 9:
                # indicate fret 9 posn
                handle.write ( "\r\n<!-- fret 9 position -->\r\n")
                fretY = self.FretStartY + ( (9  - (self.Capo + self.Cut)) * self.fretYspacing)
                #frLine = "<text x='FretStartX' y='fretY' font-size='FretStartFontSize' fill='FretStartFill' font-style='FretStartFontStyle'>9fr</text>\r\n"
                frLine = "<text x='" + str(self.FretStartX) + "' y='" + str(fretY) + "' font-size='" + str(self.FretStartFontSize) + "' fill='" + self.FretStartFill + "' font-style='" + self.FretStartFontStyle + "'>9fr</text>\r\n"
                handle.write( frLine)
            if self.numFrets > 12:
                # indicate fret 12 posn
                handle.write ( "\r\n<!-- fret 12 position -->\r\n")
                fretY = self.FretStartY + ( (12  - (self.Capo + self.Cut)) * self.fretYspacing)
                #frLine = "<text x='FretStartX' y='fretY' font-size='FretStartFontSize' fill='FretStartFill' font-style='FretStartFontStyle'>12fr</text>\r\n"
                frLine = "<text x='" + str(self.FretStartX) + "' y='" + str(fretY) + "' font-size='" + str(self.FretStartFontSize) + "' fill='" + self.FretStartFill + "' font-style='" + self.FretStartFontStyle + "'>12fr</text>\r\n"
                handle.write( frLine)

        handle.write("\r\n<!-- open/unplayed strings as follows (may be empty) : -->\r\n")
        # process chord - do open/unplayed string instructions 1st
        if self.hand == 'R' or self.hand == 'r':
            # Right-handed, read string info right-to left
            for i in range(self.numstrings):
                if self.chord[i] == 'x' or self.chord[i] == 'X'or self.chord[i] == 0:
                    sx = (self.nutX1  - self.centrefontonstringX ) + (i * self.stringXspacing)
                    handle.write ("<text x='" + str(sx) + "' y='" + str(self.OpenStringIndicatorY) + "' fill='black' font-size='" + str(self.OpenStringIndicatorFontSize) + "'>") 
                    if self.chord[i] == 'x' or self.chord[i] == 'X':
                        handle.write("x")
                    else:
                        handle.write("o")
                    handle.write("</text>\r\n")
        else:
            # Left-handed. Read string info left-to-right
            for i in range(self.numstrings):
                if self.chord[i] == 'x' or self.chord[i] == 'X'or self.chord[i] == 0:
                    sx = (self.nutX2  - self.centrefontonstringX ) - (i * self.stringXspacing)
                    handle.write ("<text x='" + str(sx) + "' y='" + str(self.OpenStringIndicatorY) + "' fill='black' font-size='" + str(self.OpenStringIndicatorFontSize) + "'>") 
                    if self.chord[i] == 'x' or self.chord[i] == 'X':
                        handle.write("x")
                    else:
                        handle.write("o")
                    handle.write("</text>\r\n")


        handle.write("\r\n<!-- finger positions -->")
         
        # barre chord support
        # check for a possible barre chord (i.e. no 'open' or 'unplayed' strings)
        self.barre = "TRUE"
        for i in range(self.numstrings):
            if (self.chord[i] == 0):
                self.barre = "FALSE"

        if self.barre == "TRUE": # potentially, not confirmed
            # a barre chord ?
            for i in range(self.numstrings):
                if self.chord[i] == 'X' or self.chord[i] == 'x':
                    self.barre = "FALSE"

        if (self.barre == "TRUE"): # confirmed now
            # find lowest finger posn.
            self.barrepos = 25 # way, way up fretboard
            for i in range(self.numstrings):
                if self.chord[i] < self.barrepos:
                    self.barrepos = self.chord[i]
            self.lowestfingerpos = self.barrepos # take a copy as barrepos will get adjusted

        # process chord - do fretted strings
        if self.hand == 'L' or self.hand == 'l':
             # left-handed, read string info left to right
            for i in range(self.numstrings):
                if not(self.chord[i] == 'x' or self.chord[i] == 'X'or self.chord[i] == 0):
                    spos = self.chord[i]
                    if self.Cut != 0:
                        if spos >= self.Cut:
                            adj = self.Capo
                            if adj == 0:
                                adj = 2  #  !!! literal alert! 
                            if self.barre == "TRUE" and spos == self.barrepos:
                                self.barrepos = (spos - self.Cut) + adj
                            spos = (spos - self.Cut) + adj
                    elif self.Capo != 0:
                        if self.barre == "TRUE" and spos == self.barrepos:
                            self.barrepos = spos - self.Capo
                        spos = spos - self.Capo

                    cx = self.nutX2 - (i * self.stringXspacing)
                    cy = (self.nutY1 - (self.fretYspacing / 2)) + (spos * self.fretYspacing)
                    handle.write("\r\n<circle cx='" + str(cx) + "' cy='" + str(cy) + "' r='" + str(self.dotradius) + "' stroke='black' stroke-width='1' fill='black'/>")

        else:
            # Right-handed. Read string info right-to-left
            for i in range(self.numstrings):
                if not(self.chord[i] == 'x' or self.chord[i] == 'X' or self.chord[i] == 0):
                    spos = self.chord[i]
                    if self.Cut != 0:
                        if spos >= self.Cut:
                            adj = self.Capo
                            if adj == 0:
                                adj = 2
                            if self.barre == "TRUE" and spos == self.barrepos:
                                self.barrepos = (spos - self.Cut) + adj
                            spos = (spos - self.Cut) + adj
                    elif self.Capo != 0:
                        if self.barre == "TRUE" and spos == self.barrepos:
                            self.barrepos = spos - self.Capo
                        spos = spos - self.Capo
                    cx = self.nutX1 + (i * self.stringXspacing) # !!! is this line the ONLY difference betwixt left and right?
                    cy = (self.nutY1 - (self.fretYspacing / 2)) + (spos * self.fretYspacing)
                    handle.write("\r\n<circle cx='" + str(cx) + "' cy='" + str(cy) + "' r='" + str(self.dotradius) + "' stroke='black' stroke-width='1' fill='black'/>")

        if self.barre == "TRUE":
            cy = (self.nutY1 - 5) + (self.barrepos * self.fretYspacing)
            cx2 = (self.numstrings - 1) * self.stringXspacing
            handle.write ("\r\n\r\n<!-- Barre chord path statement -->\r\n")
            #
            # The following draws an elliptical arc, which works well even when scaled
            # so I feel no compulsion to rip out the literals at this point.
            #
            pathLine = "<path d='M " + str(self.nutX1) + ' ' + str(cy) + " a 15 5 0 1,1 " + str(cx2) + " 0' style='fill:none; stroke:black; stroke-width:" + str(self.barrestrokewidth) + "'/>"
            handle.write(pathLine)


        handle.write("\r\n\r\n<!-- nut or capo position (slightly thicker line) -->\r\n") 
        handle.write(self.NutLine)

        CutStartText = ""
        FretStartY = 0 #local use only
        
        if self.Cut != 0:
            if self.barre == "TRUE":
                # output the actual fret number at which to place barre.
                    CutStartText = str(self.lowestfingerpos) + "fr"
                    FretStartY = self.FretStartY + (self.barrepos * self.fretYspacing)
            else: # not barre chord? then output the fretnumber we've cut the fretboard at
                    CutStartText = str(self.Cut) + "fr"
                    FretStartY = self.FretStartY + (2 * self.fretYspacing) # !!! literal alert!

            FretStartCX = self.FretStartX
            FretStartCFontSize = self.FretStartFontSize
            # this non-obvious piece of code adjusts the offset from the 
            # fretboard to the fret number dsiplay, if this becomes 2 digits
            if self.Cut > 9: # literal, but hey, would you prefer 'NINE'?
                    FretStartCX = FretStartCX - self.FretStartCXDiff
                    FretStartCFontSize = FretStartCFontSize - 2
                    
            handle.write("\r\n<!-- define cut -->\r\n")
            handle.write("<polyline points='")
            py = self.fretFirstY + self.fretYspacing # 32
            for i in range(self.numstrings):
                    px = self.fretsX1 + (i * self.stringXspacing) 
                    handle.write( str(px) + ',' + str(py) + ' ')
                    if py == (self.fretFirstY + self.fretYspacing):
                            py = py - (self.fretYspacing / 2)
                    else:
                            py = self.fretFirstY + self.fretYspacing
                            
            handle.write("' style='fill:none; " + self.fretstyle + "' />\r\n")
            handle.write("<polyline points='")
            py = self.fretFirstY + self.fretYspacing + (self.fretYspacing / 2)
            for i in range(self.numstrings):
                    px = self.fretsX1 + (i * self.stringXspacing) 
                    handle.write( str(px) + ',' + str(py) + ' ')
                    if py == self.fretFirstY + self.fretYspacing + (self.fretYspacing / 2):
                            py = self.fretFirstY + self.fretYspacing
                    else:
                            py = self.fretFirstY + self.fretYspacing + (self.fretYspacing / 2)
                            
            handle.write("' style='fill:none; " + self.fretstyle + "' />\r\n")
            handle.write("\r\n\r\n<!-- fret position up cut neck -->\r\n")
            handle.write("<text x='" + str(FretStartCX) + "' y='" + str(FretStartY) + "' fill='" + self.FretStartFill + "' font-size='" + str(FretStartCFontSize) + "' font-style='" + self.FretStartFontStyle + "'>" + CutStartText + "</text>\r\n")

        handle.write("\r\n<!-- frets -->\r\n")
        for i in range(self.numFrets):
            if not (self.Cut != 0 and i == 1):
                y = self.fretFirstY + (i * self.fretYspacing) 
                handle.write("<line x1='" + str(self.fretsX1) + "' y1='" + str(y) + "' x2='" + str(self.fretsX2) + "' y2='" + str(y) + "' style='" + self.fretstyle + "' />\r\n")

        # now decide how strings must be drawn
        # taking account of a 'cut' fretboard format
        if self.Cut != 0:
            # strings are drawn in two parts
            handle.write("\r\n<!-- strings (to cut) --> \r\n")
            y2 = self.fretFirstY + self.fretYspacing #32
            for i in range(self.numstrings):
                x = self.nutX1 + (i * self.stringXspacing) 
                handle.write("<line x1='" + str(x) + "'  y1='" + str(self.stringsY1) + "' x2='" + str(x) + "'  y2='" + str(y2) + "' style='" + self.stringstyle + "' />\r\n")
                if y2 == (self.fretFirstY + self.fretYspacing):
                    y2 = self.fretFirstY + (self.fretYspacing / 2)
                else:
                    y2 = self.fretFirstY + self.fretYspacing

            handle.write("\r\n<!-- strings (from cut) --> \r\n")
            y1 = self.fretFirstY + self.fretYspacing + (self.fretYspacing / 2) #37
            for i in range(self.numstrings):
                x = self.nutX1 + (i * self.stringXspacing) 
                handle.write("<line x1='" + str(x) + "'  y1='" + str(y1) + "' x2='" + str(x) + "'  y2='" + str(self.stringsY2) + "' style='" + self.stringstyle + "' />\r\n")
                if y1 == (self.fretFirstY + self.fretYspacing + (self.fretYspacing / 2)):
                    y1 = self.fretFirstY + self.fretYspacing
                else:
                    y1 = self.fretFirstY + self.fretYspacing + (self.fretYspacing / 2)
        else:
            # No cut? - strings are drawn as one part each
            handle.write("\r\n<!-- strings -->\r\n")
            for i in range(self.numstrings):
                x = self.nutX1 + (i * self.stringXspacing) 
                handle.write("<line x1='" + str(x) + "'  y1='" + str(self.stringsY1) + "' x2='" + str(x) + "'  y2='" + str(self.stringsY2) + "' style='" + self.stringstyle + "' />\r\n")

        handle.write("\r\n</svg>\r\n") # as Bugs would say: 'That's it folks!'

        handle.close()
        
# "And The Lord said unto Moses 'Come Forth'. but he only came fifth, so all he won was a stick of Licorice." (Source: The Pitmans Bible)

# test module stuff below

def main():
    #args = [0, 2, 2, 1, 0, 0,  0,   0,  'R',   'E',   "First posn E", "Test_E_1.svg"] 
    c = chord([0, 2, 2, 1, 0, 0,  0,   0,  'R',   'E',   "First posn E", "Test_E_1.svg"] )
    print("hello")
    c.draw() # draw the chord and save it to given filename Test_E_1.svg
    print("bye")

if __name__ == "__main__":
    main()
    
