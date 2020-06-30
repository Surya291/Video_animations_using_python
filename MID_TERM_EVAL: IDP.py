'''
Released under GNU GPL
 By K.Surya Prakash ee18btech11026@iith.ac.in
    V.Sai Ashok  ee18btech11040@iith.ac.in

Video link : https://drive.google.com/file/d/1aG34mZQG-dbbrvnTk9yEOAPd0K_rFBEU/view

'''


from manimlib.imports import *
from wifi_creature.wifi_creature import * ## For creature animations !!
from intro import *


class config(SVGMobject):
    a = OmegaCreature()
    a.CONFIG = {
        "color": RED,
    }
class matrix(MovingCameraScene):
    def construct(self):
        d1 = Dot()
        #d1.scale(3)
        d2 = d1.copy()
        d3 = d1.copy()
        d4 = d1.copy()
        d5 = d1.copy()
        d6 = d1.copy()
        text = TextMobject("CSI Representation")
        text.set_color(YELLOW)
        text.move_to(0.8*TOP)
        x = Vector(13 * (RIGHT))
        y = Vector(8* (UP))
        x.move_to(3*DOWN)
        y.move_to(4.2*LEFT)
        xt = TextMobject("Time Domain")
        yt = TextMobject("Frequency Domain")
        xt.set_color(RED)
        yt.set_color(BLUE)
        xt.next_to(x,DOWN)
        yt.rotate_in_place(np.pi/2)
        yt.next_to(y, LEFT)

        self.play(Write(x),Write(y),Write(xt),Write(yt),Write(text))



        m1 = TexMobject("""
             \\left[ \\begin{array}{ccc}
H_{1,A,t} & H_{1,B,t} & H_{1,C,t} \\\\
\cdot & \cdot & \cdot\\\\
\cdot & \cdot & \cdot\\\\
H_{15,A,t} & H_{15,B,t} & H_{15,C,t} \\\\
\cdot & \cdot & \cdot\\\\
\cdot & \cdot & \cdot\\\\
H_{30,A,t} & H_{30,B,t} & H_{30,C,t} \\\\
                \\end{array} \\right]
            
        """)

        m2 = TexMobject("""
                     \\left[ \\begin{array}{ccc}
        H_{1,A,t+1} & H_{1,B,t+1} & H_{1,B,t+1} \\\\
        \cdot & \cdot & \cdot\\\\
        \cdot & \cdot & \cdot\\\\
        H_{15,A,t+1} & H_{15,B,t+1} & H_{15,C,t+1} \\\\
        \cdot & \cdot & \cdot\\\\
        \cdot & \cdot & \cdot\\\\
        H_{30,A,t+1} & H_{30,B,t+1} & H_{30,C,t+1} \\\\
                        \\end{array} \\right]

                """)




        #m2.next_to(m1, RIGHT)
        m = VGroup(d1,d2,d3,m1,m2,d4,d5,d6)

        m.scale(0.4)
        m.arrange(RIGHT,buff = 0.4)
        #self.play(Write(m))
        m.move_to(2* RIGHT)

        self.play(FadeIn(m),run_time = 2)
        b1_1 =Brace(m[3],LEFT,buff = SMALL_BUFF )
        b1_2 = Brace(m[3],UP,buff = SMALL_BUFF)

        #b = Brace(m,DOWN,buff = LARGE_BUFF)
        b1_1_t1 = b1_1.get_text("30 \\\\ subcarriers")
        b1_2_t1 = b1_2.get_text("3 Receivers")
        #


        n = VGroup(b1_1, b1_2, b1_1_t1, b1_2_t1)
        #n.move_to(RIGHT)

        #self.add(b)

        t = TextMobject("t")
        t1 = TextMobject("t+1")
        t.next_to(m[3],3*DOWN)
        t1.next_to(m[4], 3*DOWN)
        self.play(
            Write(t),
            Write(t1)
        )

        self.wait()

        # Save the state of camera
        self.camera_frame.save_state()

        # Animation of the camera
        self.play(
            # Set the size with the width of a object
            self.camera_frame.set_width, m1.get_width() * 2.5,
            # Move the camera to the object
            self.camera_frame.move_to, m1,
            GrowFromCenter(b1_1),
            FadeIn(b1_1_t1),
            GrowFromCenter(b1_2),
            FadeIn(b1_2_t1)
        )
        self.wait(2)

        # Restore the state saved
        #self.play(Restore(self.camera_frame))

        self.play(
            #self.camera_frame.set_height, m2.get_width() * 0.8 ,
            self.camera_frame.move_to, m2
        )
        self.wait()

        self.play(Restore(self.camera_frame))

        self.wait()

        #######################################333


class Intro(Scene):
    def construct(self):
        Title = TextMobject("Passive Human Motion \\\\Detection")
        Title.to_edge(UP * 2)
        T2 = TextMobject("Using ", "Wi-Fi", " Sensing")
        T2[1:3].set_color(BLUE)
        T2.next_to(Title, 5 * DOWN)
        # Title.to_edge(UP)
        self.play(Write(Title.scale(2)))
        self.wait(0.5)
        self.play(FadeInFromDown(T2.scale(2)))
        self.wait(2)
        ##########################################
        ## DEFING THE CREATURE
        winee = OmegaCreature()

        wini = Alex(
            color=ORANGE).to_corner(DOWN + LEFT)
        wini.scale(1.25)
        doubt = TextMobject("Wi-Fi", "Sensing", "????")
        doubt[0:2].set_color(BLUE)
        doubt[2].set_color(RED)
        doubt.arrange(DOWN)
        # doubt[2].next_to(doubt[0:2],DOWN )
        doubt.scale(1.7)

        change1 = Transform(T2[1], doubt[0])
        change2 = Transform(T2[2], doubt[1])

        ###########################################
        self.play(
            ShowCreation(wini),
            FadeOut(T2[0]),
            FadeOutAndShift(Title)
        )
        self.wait()  ################################

        talk = wifi_creatureSays(
            wini, doubt,
            winee=winee,
            bubble_class=ThoughtBubble,
            bubble_kwargs={"height": 5, "width": 7},
            content_introduction_class=FadeIn,
            target_mode="speaking"
        )
        self.play(change1, change2)

        self.wait(0.01)
        self.play(talk)
        self.wait(0.25)
        self.play(Blink(wini))
        self.wait()
        '''

        self.play(
           FadeOutAndShiftDown(self.mobjects[2]),)
        self.wait()
        '''
        q1 = TextMobject("What is Wi-Fi Sensing ??")
        q1_copy = q1.copy()
        q1_copy.to_edge(UP * 2)
        q1_copy.set_color(BLUE)
        print(self.mobjects)
        self.play(ReplacementTransform(doubt, q1_copy), FadeOut(self.mobjects[2][0:2]), FadeOut(self.mobjects[1]),
                  FadeOut(self.mobjects[0]))
        self.wait()

        p1 = TextMobject(
            "\\small {Wi-Fi Sensing is the use, by a Wi-Fi Sensing capable STA(s) of \\\\recieved Wi-Fi signals to detect feature(s) of an intended target(s) \\\\ in a given environment.}")
        p2 = TextMobject(
            "\\small{Features can be motion, presence or  proximity, gesture, \\\\people counting,geometry, velocity, etc.}")
        p3 = TextMobject("\\small{Target can be object, human, animal, etc.}")
        p4 = TextMobject(
            "\\small{Environment can be anything within a few centimeters/meters \\\\ of a device, room,house/enterprise, etc.}")
        self.wait()

        p1.next_to(q1_copy, DOWN, buff=0.5)
        p2.next_to(p1, DOWN, buff=0.5)
        p3.next_to(p2, DOWN, buff=0.5)
        p4.next_to(p3, DOWN, buff=0.5)
        self.play(Write(p1), run_time=2)
        self.wait(1)
        self.play(Write(p2), run_time=2)
        self.wait(1)
        self.play(Write(p3))
        self.wait(1)
        self.play(Write(p4), run_time=2)
        self.wait(1)
        self.play(
            FadeOut(q1_copy),
            FadeOut(p1),
            FadeOut(p2),
            FadeOut(p3),
            FadeOut(p4)
        )

        q4 = TextMobject("Applications of Wi-Fi Sensing!!!")
        q4_copy = TextMobject("Applications of Wi-Fi Sensing")
        p13 = TextMobject("Gesture recognition")
        p14 = TextMobject("Room sensing and presence detection")
        p15 = TextMobject("Activity detection")
        p16 = TextMobject("Facial or body recognititon")
        p17 = TextMobject("Gaming control")
        p18 = TextMobject("Robot 3D vision")

        self.play(Write(q4))
        self.wait()

        q4_copy.to_edge(UP * 2)
        q4_copy.set_color(BLUE)
        self.play(ReplacementTransform(q4, q4_copy))
        p13.next_to(q4_copy, DOWN, buff=0.5)
        p14.next_to(p13, DOWN, buff=0.5)
        p15.next_to(p14, DOWN, buff=0.5)
        p16.next_to(p15, DOWN, buff=0.5)
        p17.next_to(p16, DOWN, buff=0.5)
        p18.next_to(p17, DOWN, buff=0.5)
        self.play(Write(p13), run_time=2)
        self.wait(1)
        self.play(Write(p14), run_time=2)
        self.wait(1)
        self.play(Write(p15), run_time=2)
        self.wait(1)
        self.play(Write(p16), run_time=2)
        self.wait(1)
        self.play(Write(p17), run_time=2)
        self.wait(1)
        self.play(Write(p18), run_time=2)
        self.wait(1)
        self.play(
            FadeOut(q4_copy),
            FadeOut(p13),
            FadeOut(p14),
            FadeOut(p15),
            FadeOut(p16),
            FadeOut(p17),
            FadeOut(p18)
        )

        q2 = TextMobject("Why should we use Wi-fi Sensing ??")
        q2_copy = TextMobject("Why should we use Wi-fi Sensing ??")
        p5 = TextMobject("\\small {Wi-Fi is ubiquitous in homes and enterprises.}")
        p6 = TextMobject("\\small{Expand the use of Wi-Fi to applications beyond just communication.}")
        p7 = TextMobject(
            "\\small{No need of dedicated hardware as any Wi-Fi-compliant device \\\\ can potentially implement any Wi-Fi sensing functionalities using \\\\ only software upgrade.}")
        p8 = TextMobject(
            "\\small{Wi-Fi can overcome drawbacks from alternative technologies \\\\ Camera: field of view, privacy, power consumption \\\\ Ultrasonic/laser: objects can block}")
        self.play(Write(q2))
        self.wait()
        q2_copy.to_edge(UP * 2)
        q2_copy.set_color(BLUE)
        self.play(ReplacementTransform(q2, q2_copy))
        p5.next_to(q2_copy, DOWN, buff=0.5)
        p6.next_to(p5, DOWN, buff=0.5)
        p7.next_to(p6, DOWN, buff=0.5)
        p8.next_to(p7, DOWN, buff=0.5)
        self.play(Write(p5))
        self.wait(1)
        self.play(Write(p6))
        self.wait(1)
        self.play(Write(p7), run_time=3)
        self.wait(2)
        self.play(Write(p8), run_time=3)
        self.wait(2)
        self.play(
            FadeOut(q2_copy),
            FadeOut(p5),
            FadeOut(p6),
            FadeOut(p7),
            FadeOut(p8)
        )

        q3 = TextMobject("Why does Wi-fi Sensing work ??")
        q3_copy = TextMobject("Why does Wi-fi Sensing work ??")
        p9 = TextMobject(
            "\\small {WiFi sensing is the use of 802.11 signals to sense (e.g. detect) \\\\ events/changes in the environment. Often with signal processing and \\\\ machine learning.}")
        p10 = TextMobject("\\small{A STA (Tx) transmits 802.11 signal to a STA (Rx) in a \\\\ multipath-rich venue.}")
        p11 = TextMobject(
            "\\small{802.11 signal bounces back and forth in the venue generating lots \\\\ of multipaths.}")
        p12 = TextMobject(
            "\\small{Although undesirable to communications, the bouncing of the \\\\802.11 signal effectively “scan” or “sense” the venue.}")
        p13 = TextMobject(
            "\\small{By monitoring the multipaths , it is possible to detect target \\\\ events and changes in the venue.}")

        self.play(Write(q3))
        self.wait()
        q3_copy.to_edge(UP * 2)
        q3_copy.set_color(BLUE)
        self.play(ReplacementTransform(q3, q3_copy))
        p9.next_to(q3_copy, DOWN, buff=0.5)
        p10.next_to(p9, DOWN, buff=0.5)
        p11.next_to(p10, DOWN, buff=0.5)
        p12.next_to(q3_copy, DOWN, buff=0.5)
        p13.next_to(p12, DOWN, buff=0.5)
        self.play(Write(p9))
        self.wait(1)
        self.play(Write(p10))
        self.wait(1)
        self.play(Write(p11), run_time=3)
        self.wait(1)
        self.play(FadeOut(p11), FadeOut(p9),
                  FadeOut(p10), )
        self.play(Write(p12), run_time=3)
        self.wait(1)
        self.play(Write(p13), run_time=3)
        self.wait(2)
        self.play(
            FadeOut(q3_copy),
            FadeOut(p12),
            FadeOut(p13)
        )
        self.wait()

def create_creature(self):
    wini = Alex(winee).to_corner(DOWN + LEFT)
    doubt = TextMobject("Hmm..")
    change = Transform(text, doubt)
    self.play(ShowCreation(wini))
    talk = wifi_creatureSays(
        wini, doubt,
        bubble_kwargs={"height": 2, "width": 2.76},
        target_mode="speaking"
    )
    self.play(change, talk)

    self.wait()
    self.play(Blink(wini))
    self.wait()

class CSI_intro(Scene):
    def construct(self):

        t = TextMobject("But how do we monitor", "changes in multipaths","????")
        t2 = TextMobject("But how do we monitor" ," changes in ", "multipaths ????")
        t2[2].next_to(t2[0:2],DOWN)
        t2.move_to(3.2*UP)
        t.arrange(DOWN)

        wini = Alex(color=PINK,flip_at_start= True).to_corner(DOWN + RIGHT)
        wini.scale(1.35)
        talk = wifi_creatureSays(
        wini,t,

        bubble_kwargs={"height": 5, "width": 7},
        content_introduction_class=Write,
        target_mode="speaking"
        )
        self.play(ShowCreation(wini),talk)
        self.wait(0.8)
        #self.remove_foreground_mobject(t)
        #self.remove_foreground_mobjects(talk)
        self.play(Blink(wini))
        self.wait(0.7)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects],
            Transform(t[0:2].copy(), t2[0:2].copy()),
            Transform(t[2].copy(), t2[2].copy())

            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(2)
        v1 = Vector(1.5*(DOWN+LEFT))
        v2 = Vector(1.5*(DOWN+RIGHT))

        v1.next_to(t2[2], 2.5*DOWN + 0.4*LEFT)
        v2.next_to(t2[2], 2.5 * DOWN + 0.2 * RIGHT)
        #brace = Brace(vector, DOWN)
        #length = TextMobject("Length")
        #length.next_to(brace, DOWN)
        group = VMobject()
        #group.add(v1, brace, length)
        group.add(v1,v2)
        group.set_color(PINK)
        #group.rotate_in_place(5*np.pi/6)
        v1.get_center = lambda : v1.get_start()
        v2.get_center = lambda: v2.get_end()
        self.play(Write(group))
        self.wait()
        txt_grp = VMobject()
        RSSI = TextMobject("RSSI")
        CSI = TextMobject("CSI")
        RSSI.next_to(v1.get_end(),DOWN,buff=0.7)
        CSI.next_to(v2.get_end(), DOWN,buff=0.7)
        RSSI.scale(2)
        CSI.scale(2)
        txt_grp.add(RSSI,CSI)
        txt_grp.set_color(BLUE_E)
        txt2 = txt_grp.copy()
        txt2.move_to(2*UP)
        #txt_grp.scale(2)
        self.play(Write(txt_grp))
        self.wait()
        self.play(FadeOut(group),Transform(txt_grp,txt2))
        self.wait(2)
        #################################################################################
        wht = TextMobject("Which one to \\\\choose ?")
        wht.scale(0.7)
        blacky = Alex(color=GREY_BROWN, flip_at_start=False).move_to(2.7*DOWN )
        blacky.scale(0.5)
        talk2 = wifi_creatureSays(
            blacky, wht,

        bubble_kwargs = {"height": 2, "width": 3},
        content_introduction_class = FadeIn,
        target_mode = "speaking"
        )

        self.play(talk2)
        self.wait(1.5)
        self.play(FadeOut(self.mobjects[3][1]),FadeOut(self.mobjects[3][2]))
        #self.play(*[FadeOut(m) for m in self.mobjects])


        pt1 = TextMobject("$\\Rightarrow$ An estimated measurement of how good ",
                          "a device can hear from any AP.",
                          "\\\\ ",
                          "$\\Rightarrow$ Indicates the received power level after",
                          "  any possible loss at the antennas. ","Hence, describing the channel's nature.",
                          "\\\\",
                          )
        pt1.arrange(DOWN,aligned_edge  = LEFT)
        pt1.scale(0.6)
        pt1.next_to(txt2[0],DOWN)
        blacky.look_at(txt2[0])
        for i in pt1:
            self.play(Write(i),Blink(blacky))
        self.wait(1.5)
        pt2 = TextMobject("$\\Rightarrow$ It describes how a signal propagates",
                          "from a Tx to Rx",
                          "\\\\",
                          "$\\Rightarrow$  It is considered to be more stable  ",
                          " and robust to complex conditions",
                          #" environmental conditions ",
                          "\\\\",
                          " $\\Rightarrow$ Since CSI related to each subcarrier",
                          " of the OFDM signal can be extracted,  ",
                          "the system will have more information ","for effective learning.")
        pt2.arrange(DOWN,aligned_edge  = LEFT)
        pt2.scale(0.6)
        pt2.next_to(txt2[1],DOWN)
        blacky.look_at(txt2[1])
        for i in pt2:
            self.play(Write(i),Blink(blacky))
        self.wait(1.5)

        # ZigZag: my_objects.py - line 110
        wrong = ZigZag(txt2[0],color=RED,stroke_width=10)
        correct = FreehandRectangle(txt2[1],margin=0.2,color=RED,)
        self.bring_to_back(correct)

        opinion = TextMobject("CSI"," will be a good pick!!")
        opinion[0].set_color(GOLD_E)
        talk3 = wifi_creatureSays(
            blacky, opinion,
            bubble_class=ThoughtBubble,
            bubble_kwargs={"height": 1, "width":5 },
            content_introduction_class=FadeIn,
            target_mode="speaking"
        )
        self.play(talk3,ShowCreation(wrong,run_time=1,rate_func=linear),ShowCreation(correct,run_time = 3))
        self.wait(2)
class CSI_detail(Scene):
    def construct(self):
        CSI = TextMobject("CSI : Channel State Information")
        CSI.scale(2)
        CSI.set_color(BLUE_E)
        CSI.move_to(0.8*TOP)
        self.play(Write(CSI))
        pt1 = TextMobject("$\\Rightarrow$ For a Wi-Fi system , CSI is a 3D matrix\\\\ of complex values representing the amplitude attenuation \\\\ and phase shift of multipath channels")

        pt3 = TextMobject("$\\Rightarrow$ Its core technologies include\\\\MIMO (multi-input and multi-output) and \\\\ OFDM(Orthogonal frequency-division multiplexing) . ")
        #pt3.arrange(DOWN,buff = 0.1)
        pt4 = TextMobject("$\\Rightarrow$ CSI represents the frequency response of \\\\ each subcarrier for every antenna pair .")
        #pt4.arrange(DOWN,buff = 0.1)
        pt = Group(pt1,pt3,pt4)
        pt.arrange(DOWN,buff = 0.7)
        pt.next_to(CSI,DOWN,buff = 0.7)
        for i in pt:
            self.play(Write(i,run_time=4))
        self.wait(2)
        #matrix.construct(self)

class CSI_look(Scene):
    def construct(self):
        student = Alex(color=TEAL_A,flip_at_start= False).to_corner(DOWN + LEFT)
        student.scale(0.5)
        t = TextMobject("But how is\\\\ CSI shaped ?")
        t.scale(0.7)
        talk1 = wifi_creatureSays(
        student,t,
        bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=ThoughtBubble,
        )

        prof = Alex(color=GREEN_SCREEN,flip_at_start= True).to_corner(DOWN + RIGHT)
        prof.scale(1)
        t = TextMobject("For a 1:Tx , 3:Rx \\\\ scenario ...  ")
        t.scale(0.7)

        talk2 = wifi_creatureSays(
        prof,t,
        bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=SpeechBubble,
        )
        t3 = TextMobject("CSI will be a 2D matrix \\\\with time as the \\\\ 3rd dimension\\\\ Like this ..")
        talk3 = wifi_creatureSays(
        prof,t3,
        bubble_kwargs={"height": 3, "width": 4.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=SpeechBubble,
        )



        self.add(student,prof)


        self.play(talk1,runtime = 2)
        self.wait(1.5)
        self.play(talk2,runtime = 2)
        self.wait()
        self.play(FadeOut(self.mobjects[1][1:3]))
        self.wait()
        self.play(talk3,runtime=2)
        self.wait()


class CSI_def(Scene):
    def construct(self):
        formula = TexMobject("H_{i,j,k}")
        formula.scale(2)
        formula.set_color(RED)
        formula.move_to(LEFT)

        #formula2 = TextMobject("$=$ jk$ \\abs{ ljhj}$ kljj$\\angle{-78.2039)$")
        formula2 = TexMobject(" = ","|","H_{i,j,k}","|"," \\angle{}","H_{i,j,k}")
        formula2.scale(2)
        formula2.set_color(RED)
        f = VGroup(formula,formula2)
        f.arrange(RIGHT)
        v1 = Vector(1.5*RIGHT)
        v2 = Vector(1.5 * RIGHT)
        v3 = Vector(1.5 * RIGHT)
        v1.rotate_in_place(np.pi / 4)
        v3.rotate_in_place(-np.pi / 4)
        v1.move_to(UP+RIGHT)
        v2.move_to(1.3*RIGHT)
        v3.move_to(DOWN+RIGHT)
        v = VGroup(v1,v2,v3)
        v.next_to(formula,RIGHT)
        t1 = TextMobject("i : Sub-carrier index")
        t2 = TextMobject("j : Receiver index")
        t3 = TextMobject("k : time index")
        t1.next_to(v1.get_end(), RIGHT)
        t2.next_to(v2.get_end(), RIGHT)
        t3.next_to(v3.get_end(), RIGHT)

        t = VGroup(t1,t2,t3)
        t.set_color(PINK)


        prof = Alex(color=BLUE_E,flip_at_start= True).move_to(3.95*DOWN +5*RIGHT)
        prof.scale(0.5)
        talk = TextMobject("Remember , CSI is a \\\\ complex quantity ")
        talk.scale(0.7)

        talk2 = wifi_creatureSays(
        prof,talk,
        bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=SpeechBubble,
        )

        t3 = TextMobject("From now on we'll use \\\\ the CSI's magnitude for detecting \\\\ human presence ..")
        t3.scale(2)
        talk3 = wifi_creatureSays(
        prof,t3.scale(2),
        bubble_kwargs={"height": 2.5, "width": 6},
        content_introduction_class=Write,
        target_mode="speaking",
        bubble_class=SpeechBubble,
        )

        self.play(FadeIn(formula))
        self.wait()
        self.play(Write(v))
        self.wait(0.5)
        self.play(Write(t))

        self.wait()
        self.add(prof)
        self.play(FadeOut(v),FadeOut(t),talk2)
        self.wait()
        self.play(FadeIn(f[1][0:2]),FadeIn(f[1][3:5]))
        self.wait(0.25)
        self.play(Transform(f[0].copy(),f[1][2]),Transform(f[0].copy(),f[1][5]))

        self.wait()
        print(self.mobjects)
        self.play(FadeOut(self.mobjects[1][1:3]),FadeOut(f[0]),FadeOut(f[1][0]),FadeOut(f[1][4:6]),FadeOut(self.mobjects[5]),talk3)
        self.wait()

class ZigZag(VMobject):
    CONFIG = {
        "margin":0.4,
        "sign":1
    }
    def __init__(self,path,partitions=10,**kwargs):
        VMobject.__init__(self,**kwargs)
        rect = Rectangle(
            width  = path.get_width() + self.margin,
            height = path.get_height() + self.margin
            )
        rect.move_to(path)
        w = rect.get_width()
        h = rect.get_height()
        alpha = w / h
        hp = int(np.ceil(partitions / (2 * (alpha + 1))))
        wp = int(np.ceil(alpha * hp))
        sides = VGroup(*[
            Line(rect.get_corner(c1),rect.get_corner(c2))
            for c1,c2 in zip([UL,UR,DR,DL],[UR,DR,DL,UL])
            ])
        total_points = []
        for side,points in zip(sides,[wp,hp,wp,hp]):
            for p in range(points):
                total_points.append(side.point_from_proportion(p/points))
        total_points.append(total_points[0])
        middle = int(np.floor(len(total_points)/2))
        draw_points = []
        for p in range(2,middle):
            draw_points.append(total_points[-p*self.sign])
            draw_points.append(total_points[p*self.sign])
        self.set_points_smoothly(draw_points)

class FreehandDraw(VMobject):
    CONFIG = {
        "sign":1,
        "close":False,
        "dx_random":7,
        "length":0.06
    }
    def __init__(self,path,partitions=120,**kwargs):
        VMobject.__init__(self,**kwargs)
        coords = []
        for p in range(int(partitions)+1):
            coord_i = path.point_from_proportion((p*0.989/partitions)%1)
            coord_f = path.point_from_proportion((p*0.989/partitions+0.001)%1)
            reference_line = Line(coord_i, coord_f).rotate(self.sign*PI/2, about_point=coord_i)
            normal_unit_vector = reference_line.get_unit_vector()
            static_vector = normal_unit_vector*self.length
            random_dx = random.randint(0,self.dx_random)
            random_normal_vector = random_dx * normal_unit_vector / 100
            point_coord = coord_i + random_normal_vector + static_vector
            coords.append(point_coord)
        if self.close:
            coords.append(coords[0])
        self.set_points_smoothly(coords)

# FreehandRectangle depends of FreehandDraw
class FreehandRectangle(VMobject):
    CONFIG = {
        "margin":0.7,
        "partitions":120,
    }
    def __init__(self,texmob,**kwargs):
        VMobject.__init__(self,**kwargs)
        rect = Rectangle(
            width  = texmob.get_width() + self.margin,
            height = texmob.get_height() + self.margin
            )
        rect.move_to(texmob)
        w = rect.get_width()
        h = rect.get_height()
        alpha = w / h
        hp = np.ceil(self.partitions / (2 * (alpha + 1)))
        wp = np.ceil(alpha * hp)
        sides = VGroup(*[
            Line(rect.get_corner(c1),rect.get_corner(c2))
            for c1,c2 in zip([UL,UR,DR,DL],[UR,DR,DL,UL])
            ])
        total_points = []
        for side,p in zip(sides,[wp,hp,wp,hp]):
            path = FreehandDraw(side,p).points
            for point in path:
                total_points.append(point)
        total_points.append(total_points[0])
        self.set_points_smoothly(total_points)




class act_noact(Scene):
    def construct(self):
        img2 = ImageMobject("activity_high.png")
        img1 = ImageMobject("noactivity_high.png")
        img1.to_corner(LEFT,buff = 2.2)
        img2.to_corner(RIGHT,buff = 2.2)
        head = TextMobject("An illustration of how human motion \\\\impacts CSI's magnitude")
        head.move_to(0.8*TOP)
        head.set_color(BLUE_E)
        t1 = TextMobject("CSI values when \\\\ no human presence")
        t2 = TextMobject("CSI values when \\\\ a human is moving in a room")
        t1.next_to(img1,5*DOWN)
        t2.next_to(img2, 5*DOWN)
        self.play(Write(head),)
        self.wait()
        self.play(FadeIn(img1.scale(2)),Write(t1,runtime= 5))

        self.wait(1.5)
        self.play(FadeIn(img2.scale(2)),Write(t2,runtime= 5))
        self.wait(1.5)

class CSI_and_human(Scene):
    def construct(self):
        student = Alex(color=TEAL_A,flip_at_start= False).to_corner(DOWN + LEFT)
        student.scale(0.5)
        t = TextMobject("But how does \\\\human motion\\\\ effect CSI ???")
        t.scale(0.7)
        talk1 = wifi_creatureSays(
        student,t,
        #bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=ThoughtBubble,
        )

        prof = Alex(color=GREEN_SCREEN,flip_at_start= True).to_corner(DOWN + RIGHT)
        prof.scale(1)
        t = TextMobject("As human moves , his body\\\\ acts as an obstacle to the signal\\\\ and thus create reflections !")
        #t.scale(0.7)

        talk2 = wifi_creatureSays(
        prof,t,
        #bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=SpeechBubble,
        )
        t3 = TextMobject("These reflections inturn \\\\increases the multipaths\\\\ and effect CSI\\\\ like this !!!")
        talk3 = wifi_creatureSays(
        prof,t3,
        #bubble_kwargs={"height": 3, "width": 4.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=SpeechBubble,
        )



        self.add(student,prof)


        self.play(talk1,runtime = 2)
        self.wait(1.5)
        self.play(FadeOut(self.mobjects[1][1:3]))
        self.wait(0.1)
        self.play(talk2,runtime = 2)
        self.wait(2.7)

        self.play(FadeOut(self.mobjects[1][1:3]))
        self.wait(0.5)
        self.play(talk3,runtime=2)
        self.wait(2)
        print(self.mobjects)

class result(Scene):
    def construct(self):
        t1 = TextMobject("Here are the obtained results ")
        t1.move_to(0.8*TOP)
        t1.set_color(RED)

        t2 = TextMobject("With a One Class SVM model:")
        t3 = TextMobject("Average"," prediction accuracy ", "achieved : 95 \\%")
        t4 = TextMobject("BLUE : NO HUMAN MOVEMENT")
        t5 = TextMobject("ORANGE: HUMAN MOVEMENT")
        t4.set_color(BLUE_E)
        t5.set_color(ORANGE)
        t6 = TextMobject("Apart from this we exploited the idea "," of CSI being a time-series data ")

        t7 = TextMobject("We implemented an elementary\\\\ LSTM : LONG SHORT TERM MEMORY\\\\model to the CSI data")
        t8 = TextMobject("RESULT : An"," accuracy"," of 96.8\\%")
        t8[1].set_color(PINK)
        t6.arrange(DOWN)
        #t7.arrange(DOWN)
        t6[1][-15:-4].set_color(PINK)
        t7[0][25:30].set_color(PINK)


        g2 = VGroup(t6,t7,t8)
        g2.arrange(DOWN,buff = 1)

        t3[1].set_color(PINK)
        grp = Group()
        grp.add(t1,t2,t3)
        g = VGroup()
        g.add(t4,t5)
        g.arrange(RIGHT)
        grp.arrange(DOWN)
        copy = grp.copy()
        copy.move_to(TOP*0.7)
        g.next_to(copy[2],DOWN)
        g.scale(0.7)
        self.play(Write(t1),Write(t2),Write(t3))
        self.play(Transform(grp,copy))
        self.wait(1.5)
        img1 = ImageMobject("actual.png")
        img2 = ImageMobject("predicted.png")
        img = Group(img1,img2).scale(2.2)
        img.arrange(RIGHT)
        img.move_to(DOWN)
        self.play(Write(g),FadeIn(img))
        self.wait(3)
        self.play(
        *[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.play(Write(g2))
        self.wait(4)

class what_next(Scene):
    def construct(self):
        student = Alex(color=RED_E,flip_at_start= False).to_corner(DOWN + LEFT)
        t = TextMobject("What next ??").scale(2)
        t.set_color(RED)
        copy=t.copy()
        copy.move_to(TOP*0.8)
        talk1 = wifi_creatureSays(
        student,t,
        #bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=Write,
        target_mode="speaking",
        bubble_class=SpeechBubble,
        )
        txt1 = TextMobject("$\\Rightarrow$ Keen on exploiting the phase part of CSI.")
        txt2 = TextMobject("$\\Rightarrow$ Analysing a much complex dataset.\\\\" ,"  A dataset which describes human motion in different rooms .")
        txt2.arrange(DOWN,aligned_edge  = LEFT,buff = 0.1)
        txt3 = TextMobject("$\\Rightarrow$ To improve LSTM by applying signal preprocessing methods.")
        self.play(talk1)
        self.wait(1.5)
        self.play(Transform(t,copy),FadeOutAndShiftDown(self.mobjects[0][0:2]))
        self.wait()
        grp = VGroup(txt1,txt2,txt3)
        grp.arrange(DOWN,aligned_edge  = LEFT,buff = 0.8)

        grp.next_to(copy,2*DOWN)
        for  i in grp:

            self.play(Write(i))
        self.wait(2)

class credits(Scene):
    def construct(self):
        b = TextMobject("By...")

        b.move_to(0.8*TOP).scale(2).set_color(RED)

        l = TextMobject(">>> Special Thanks <<<")
        l.scale(1.5).set_color(RED)

        t1 = TextMobject("K. SURYA Prakash : ee18btech11026$@$iith.ac.in")
        t2 = TextMobject("V. Sai ASHOK : ee18btech11044$@$iith.ac.in")
        t3 = TextMobject("C. PRANAY Prakash : ee18btech11009$@$iith.ac.in")
        t4 = TextMobject("Dr. Sai DHIRAJ Amuru : Project Mentor")
        t5 = TextMobject("GYRUS (COMPANY) : DataSet Provider")



        t = VGroup(t1,t2,t3)
        t.arrange(DOWN,buff = 0.4)
        t.next_to(b,2.4*DOWN)

        t2 = VGroup(l,t4,t5)
        t2.arrange(DOWN,buff  = 0.4)
        t2.next_to(t[2],3*DOWN)
        self.play(Write(b))
        for i in t:
            self.play(FadeIn(i))
        self.wait()
        for i in t2:
            self.play(Write(i))
        self.wait()


class GitHub(SVGMobject):
    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        SVGMobject.__init__(self,
        file_name = "git.svg",
        fill_opacity = 1,
        stroke_width = 1,
        height = 4,
        stroke_color = WHITE,
        **kwargs)

class git_icon(Scene):
    def construct(self):
        icon = GitHub()
        grp = VGroup(icon)
        copy = grp.copy()
        copy.move_to(4.5*LEFT)
        head = TextMobject("For more information...")
        head.set_color(BLUE_E).move_to(0.8*TOP)
        Txt = TextMobject("Surya291$/$WiFi$\\_$Sensing",stroke_width= 4).set_color(TEAL_D).scale(1.5)
        self.play(Write(head),Write(grp))
        self.wait(0.5)
        self.play(Transform(grp,copy),Write(Txt.next_to(copy,RIGHT,buff=0.5)))
        self.wait(3)

class Last(result,what_next,credits,git_icon):
    def construct(self):
        result.construct(self)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(1.2)
        what_next.construct(self)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(1.2)
        credits.construct(self)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(1.2)
        git_icon.construct(self)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(1.2)


class All(Intro,CSI_intro,CSI_detail,CSI_look,matrix,CSI_def,CSI_and_human,act_noact,Analysis,Last):
    def construct(self):
        Intro.construct(self)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(1.2)


        CSI_intro.construct(self)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(1.2)

        CSI_detail.construct(self)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(1.2)

        CSI_look.construct(self)
        self.wait(1.5)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]


            # All mobjects in the screen are saved in self.mobjects
        )

        matrix.construct(self)
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        CSI_def.construct(self)
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        CSI_and_human.construct(self)
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        act_noact.construct(self)
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        Analysis.construct(self)
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        Last.construct(self)
        self.wait()



        ##################################################


        ##################################################









