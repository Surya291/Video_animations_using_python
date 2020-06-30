from manimlib.imports import *
from wifi_creature.wifi_creature import *
import cv2
class one(Scene):
    def construct(self):
        a1 = TextMobject(
            "But, how to classify as activity and \\\\ no-activity based on this data ??")

        student = Alex(color=TEAL_A,flip_at_start= False).to_corner(DOWN + LEFT)
        #student.scale(0.5)
        talk1 = wifi_creatureSays(
        student,a1,
        #bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=ThoughtBubble,
        )

        self.play(talk1)
        self.wait(2)
        self.play(
           FadeOutAndShiftDown(self.mobjects[0]),)
        # self.wait()

        a1_copy = TextMobject("Analysing the CSI Data")
        b1 = TextMobject(
            "\\small {As observed, CSI amplitude fluctuates due of \\\\ human motion and these fluctuations are proportional to intensity \\\\ of human motion. }")
        b2 = TextMobject(
            "We can differentiate them with the ``spikes``\\\\ seen in  the activity graph. \\\\ ",
            " \\small{ We'll consider the statistical parameters:\\\\ Variance and IQR$($Inter Quartile Range$)$ \\\\ across time as features for classification.}")
        b2[0][31:37].set_color(RED)
        b2[1][38:46].set_color(RED)
        b2[1][49:52].set_color(RED)
        b2.arrange(DOWN,buff = 0.5)
        a1_copy.to_edge(UP * 2)
        a1_copy.set_color(BLUE)
        self.play(FadeIn(a1_copy))
        self.wait(0.5)


        b1.next_to(a1_copy, DOWN, buff=0.5)
        b2.next_to(b1, DOWN, buff=0.5)
        #b3.next_to(b2, DOWN, buff=0.5)
        self.play(Write(b1), run_time=2)
        self.wait(1)
        self.play(Write(b2), run_time=2)
        self.wait(1)

        self.play(
            FadeOut(a1_copy),
            FadeOut(b1),
            FadeOut(b2),
            #FadeOut(b3)
        )
        a2 = TextMobject("But why only \\\\Variance and IQR ")

        talk2 = wifi_creatureSays(
        student,a2,
        #bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=ThoughtBubble,
        )

        self.play(talk2)
        self.wait()
        self.play(
           FadeOutAndShiftDown(self.mobjects[0]),)
        b8 = TextMobject(
            " \\small{Since spikes exist in activity \\\\ this increases the spread of values \\\\ which are easily described by\\\\ Variance and IQR }")
        #self.play(Write(a2))
        #self.wait()
        a2_copy = a2.copy()
        a2_copy.to_edge(TOP*0.8)
        a2_copy.set_color(BLUE)
        self.play(ReplacementTransform(a2, a2_copy))
        b8.next_to(a2_copy, DOWN, buff=0.5)
        self.play(Write(b8))
        self.wait(2)
        self.play(
            FadeOut(a2_copy),
            FadeOut(b8)
        )


class two(MovingCameraScene):
    def construct(self):
        a3 = TextMobject("Target Environment")
        b9 = TextMobject(
            "The picture of the environment in which the dataset has \\\\ been captured is shown on the screen")
        img = cv2.imread('CaptureGrid.jpeg')
        img1 = ImageMobject(img)
        Tx = TextMobject("Tx")
        Rx = TextMobject("Rx")
        grid1 = TextMobject("GRID E1")
        grid2 = TextMobject("GRID D2")
        grid3 = TextMobject("GRID C3")
        img1.scale(2)
        a3.to_edge(UP * 2)
        a3.set_color(BLUE)
        b9.next_to(a3, DOWN, buff=0.5)
        img1.next_to(b9, DOWN, buff=0.5)
        b9.next_to(a3, DOWN, buff=0.5)
        self.play(Write(a3))
        self.play(Write(b9))
        self.play(ShowCreation(img1))
        self.wait()
        Tx.scale(0.75)
        Tx.move_to(3 * LEFT + 0.4 * UP)
        arrow1 = Arrow(Tx.get_right(), 1.3 * LEFT + 0.1 * UP, buff=0.1)
        arrow1.set_color(RED)
        self.play(Write(Tx))
        self.play(GrowArrow(arrow1))

        Rx.scale(0.75)
        Rx.move_to(3 * RIGHT + 3 * DOWN)
        arrow2 = Arrow(Rx.get_left(), 1.2 * RIGHT + 3 * DOWN, buff=0.1)
        arrow2.set_color(YELLOW)
        self.play(Write(Rx))
        self.play(GrowArrow(arrow2))

        grid1.scale(0.65)
        grid1.move_to(3 * RIGHT + 0.4 * UP)
        arrow3 = Arrow(grid1.get_left(), 1 * RIGHT + 0.1 * UP, buff=0.1)
        arrow3.set_color(BLUE)
        self.play(Write(grid1))
        self.play(GrowArrow(arrow3))

        grid2.scale(0.65)
        grid2.move_to(3 * RIGHT + 0.3 * DOWN)
        arrow4 = Arrow(grid2.get_left(), 0.3 * RIGHT + 0.6 * DOWN, buff=0.1)
        arrow4.set_color(BLUE)
        self.play(Write(grid2))
        self.play(GrowArrow(arrow4))

        grid3.scale(0.65)
        grid3.move_to(3 * RIGHT + 0.9 * DOWN)
        arrow5 = Arrow(grid3.get_left(), 0.2 * LEFT + 1.1 * DOWN, buff=0.1)
        arrow5.set_color(BLUE)
        self.play(Write(grid3))
        self.play(GrowArrow(arrow5))

        self.camera_frame.save_state()
        self.play(
            self.camera_frame.set_width, img1.get_width() * 1.1,
            self.camera_frame.set_height, img1.get_height() * 1.1,
            self.camera_frame.move_to, img1
        )
        self.wait(4)
        self.play(Restore(self.camera_frame))
        self.play(
            FadeOut(a3),
            FadeOut(b9),
            FadeOut(img1),
            FadeOut(Tx),
            FadeOut(arrow1),
            FadeOut(Rx),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(grid1),
            FadeOut(arrow4),
            FadeOut(grid2),
            FadeOut(grid3),
            FadeOut(arrow5)
        )
        self.wait()


class three(Scene):
    def construct(self):
        a4 = TextMobject("Analysing the CSI Data")
        b10 = TextMobject(
            "Let us compare the variances of 30 sub-carriers across \\\\ time for activity and noactivity in the following grids.")
        b11 = TextMobject(" $\\Rightarrow$ C3 (LOS)")
        b12 = TextMobject("$\\Rightarrow$ D2 (NLOS)")
        b13 = TextMobject("$\\Rightarrow$ E1 (CORNER GRID)")

        d = TextMobject("$\\#$ LOS : Grid in the Line of Sight Region")
        e = TextMobject("$\\#$ NLOS : Grid in the Non-Line of Sight Region")
        d.set_color(BLUE)
        e.set_color(BLUE)
        v1 = VGroup(
            b11,
            b12,
            b13,d,e
        )
        v1.arrange(
            DOWN,  # <- Direction
            aligned_edge=LEFT,
            buff=0.4
        )

        a4.set_color(BLUE)
        a4.move_to(TOP*0.8)
        b10.next_to(a4, DOWN, buff=0.5)
        v1.next_to(b10, DOWN, buff=0.5)
        self.play(Write(a4))
        self.play(Write(b10))
        self.play(Write(v1))
        self.wait(2)
        self.play(
            FadeOut(a4),
            FadeOut(b10),
            FadeOut(v1)
        )


class four(MovingCameraScene):
    def construct(self):
        c1 = TextMobject("GRID - C3\\\\ Motion occured in region in the LOS path\\\\ Huge difference between data !")
        c2 = TextMobject("Receiver--A")
        c3 = TextMobject("Receiver--B")
        c4 = TextMobject("Receiver--C")
        pic_c3_a = cv2.imread('C3_A.png')
        pic_c_a = ImageMobject(pic_c3_a)
        pic_c_a.scale(1.5)

        pic_c3_b = cv2.imread('C3_B.png')
        pic_c_b = ImageMobject(pic_c3_b)
        pic_c_b.scale(1.5)

        pic_c3_c = cv2.imread('C3_C.png')
        pic_c_c = ImageMobject(pic_c3_c)
        pic_c_c.scale(1.5)

        v2 = Group(
            pic_c_a,
            pic_c_b,
            pic_c_c
        )
        v2.arrange(
            RIGHT,
            aligned_edge=UP,
            buff=0.2
        )
        c1.set_color(BLUE)
        c1.to_edge(UP)
        v2.next_to(c1, DOWN, buff=1.5)
        c2.next_to(pic_c_a, DOWN, buff=0.5)
        c3.next_to(pic_c_b, DOWN, buff=0.5)
        c4.next_to(pic_c_c, DOWN, buff=0.5)
        self.play(Write(c1))
        self.play(ShowCreation(v2))
        self.play(Write(c2), Write(c3), Write(c4))
        self.wait(2)
        self.camera_frame.save_state()
        self.play(
            self.camera_frame.set_width, pic_c_a.get_width() * 1.1,
            self.camera_frame.set_height, pic_c_a.get_height() * 1.1,
            self.camera_frame.move_to, pic_c_a
        )
        self.wait(2)
        self.play(
            self.camera_frame.set_width, pic_c_b.get_width() * 1.1,
            self.camera_frame.set_height, pic_c_b.get_height() * 1.1,
            self.camera_frame.move_to, pic_c_b
        )
        self.wait(2)
        self.play(
            self.camera_frame.set_width, pic_c_c.get_width() * 1.1,
            self.camera_frame.set_height, pic_c_c.get_height() * 1.1,
            self.camera_frame.move_to, pic_c_c
        )
        self.wait(2)
        self.play(Restore(self.camera_frame))
        self.wait(1)
        self.play(
            FadeOut(v2),
            FadeOut(c1),
            FadeOut(c2),
            FadeOut(c3),
            FadeOut(c4)
        )


class five(MovingCameraScene):
    def construct(self):
        c5 = TextMobject("GRID - D2\\\\ Motion occured in region in from NLOS Path. \\\\ Nevertheless, there is some difference in data")
        c6 = TextMobject("Receiver--A")
        c7 = TextMobject("Receiver--B")
        c8 = TextMobject("Receiver--C")
        pic_d2_a = cv2.imread('D2_A.png')
        pic_d_a = ImageMobject(pic_d2_a)
        pic_d_a.scale(1.5)

        pic_d2_b = cv2.imread('D2_B.png')
        pic_d_b = ImageMobject(pic_d2_b)
        pic_d_b.scale(1.5)

        pic_d2_c = cv2.imread('D2_C.png')
        pic_d_c = ImageMobject(pic_d2_c)
        pic_d_c.scale(1.5)

        v3 = Group(
            pic_d_a,
            pic_d_b,
            pic_d_c
        )
        v3.arrange(
            RIGHT,
            aligned_edge=UP,
            buff=0.2
        )
        c5.set_color(BLUE)
        c5.to_edge(UP)
        v3.next_to(c5, DOWN, buff=1.5)
        c6.next_to(pic_d_a, DOWN, buff=0.5)
        c7.next_to(pic_d_b, DOWN, buff=0.5)
        c8.next_to(pic_d_c, DOWN, buff=0.5)
        self.play(Write(c5))
        self.play(ShowCreation(v3))
        self.play(Write(c6), Write(c7), Write(c8))
        self.wait(2)
        self.camera_frame.save_state()
        self.play(
            self.camera_frame.set_width, pic_d_a.get_width() * 1.1,
            self.camera_frame.set_height, pic_d_a.get_height() * 1.1,
            self.camera_frame.move_to, pic_d_a
        )
        self.wait(2)
        self.play(
            self.camera_frame.set_width, pic_d_b.get_width() * 1.1,
            self.camera_frame.set_height, pic_d_b.get_height() * 1.1,
            self.camera_frame.move_to, pic_d_b
        )
        self.wait(2)
        self.play(
            self.camera_frame.set_width, pic_d_c.get_width() * 1.1,
            self.camera_frame.set_height, pic_d_c.get_height() * 1.1,
            self.camera_frame.move_to, pic_d_c
        )
        self.wait(2)
        self.play(Restore(self.camera_frame))
        self.wait(1)
        self.play(
            FadeOut(v3),
            FadeOut(c5),
            FadeOut(c6),
            FadeOut(c7),
            FadeOut(c8)
        )


class six(MovingCameraScene):
    def construct(self):
        c9 = TextMobject("GRID - E1\\\\ Motion occured in region farthest from LOS path\\\\ Thus data is close to  ``NO HUMAN PRESENCE`` ")
        c10 = TextMobject("Receiver--A")
        c11 = TextMobject("Receiver--B")
        c12 = TextMobject("Receiver--C")
        pic_e1_a = cv2.imread('E1_A.png')
        pic_e_a = ImageMobject(pic_e1_a)
        pic_e_a.scale(1.5)

        pic_e1_b = cv2.imread('E1_B.png')
        pic_e_b = ImageMobject(pic_e1_b)
        pic_e_b.scale(1.5)

        pic_e1_c = cv2.imread('E1_C.png')
        pic_e_c = ImageMobject(pic_e1_c)
        pic_e_c.scale(1.5)

        v4 = Group(
            pic_e_a,
            pic_e_b,
            pic_e_c
        )
        v4.arrange(
            RIGHT,
            aligned_edge=UP,
            buff=0.2
        )
        c9.set_color(BLUE)
        c9.to_edge(UP)
        v4.next_to(c9, DOWN, buff=1.5)
        c10.next_to(pic_e_a, DOWN, buff=0.5)
        c11.next_to(pic_e_b, DOWN, buff=0.5)
        c12.next_to(pic_e_c, DOWN, buff=0.5)
        self.play(Write(c9))
        self.play(ShowCreation(v4))
        self.play(Write(c10), Write(c11), Write(c12))
        self.wait(2)
        self.camera_frame.save_state()
        self.play(
            self.camera_frame.set_width, pic_e_a.get_width() * 1.1,
            self.camera_frame.set_height, pic_e_a.get_height() * 1.1,
            self.camera_frame.move_to, pic_e_a
        )
        self.wait(2)
        self.play(
            self.camera_frame.set_width, pic_e_b.get_width() * 1.1,
            self.camera_frame.set_height, pic_e_b.get_height() * 1.1,
            self.camera_frame.move_to, pic_e_b
        )
        self.wait(2)
        self.play(
            self.camera_frame.set_width, pic_e_c.get_width() * 1.1,
            self.camera_frame.set_height, pic_e_c.get_height() * 1.1,
            self.camera_frame.move_to, pic_e_c
        )
        self.wait(2)
        self.play(Restore(self.camera_frame))
        self.wait(1)
        self.play(
            FadeOut(v4),
            FadeOut(c9),
            FadeOut(c10),
            FadeOut(c11),
            FadeOut(c12)
        )


class seven(Scene):
    def construct(self):
        a14 = TextMobject("\\texttt{ I have observed a few trends\\\\ in these graphs !!}")

        student = Alex(color=PINK,flip_at_start= True).to_corner(DOWN + RIGHT)
        #student.scale(0.5)
        talk1 = wifi_creatureSays(
        student,a14,
        #bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=ThoughtBubble,
        )

        self.play(talk1)
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects])


        a14_copy = TextMobject("Wini's Observations")
        b14 = TextMobject(
            "There is a clear difference in Variance of activity \\\\ and noactivity data for all the three receivers in LOS \\\\condition i.e grid C3")
        b15 = TextMobject(
            "In the NLOS condition i.e grid D2, the difference between \\\\\ activity and noactivity data is a bit less when compared to LOS \\\\ case, but one can still distinguish classify the data \\\\ succesfully for Receiver A and B")
        b16 = TextMobject(
            "For the extreme NLOS condition i.e grid E1, one cannot \\\\ distinguish between the variance data of activity and\\\\ noactivity for receivers A and C. But data from receiver B\\\\ can be used to cla ssify the data as activity and noactivity")

        b17 = TextMobject("The same can be observed for IQR as well .")

        a14_copy.to_edge(UP * 2)
        a14_copy.set_color(BLUE)
        b14.next_to(a14_copy, DOWN, buff=0.5)
        b15.next_to(b14, DOWN, buff=0.5)
        b16.next_to(a14_copy, DOWN, buff=0.5)
        b17.next_to(b16, DOWN, buff=0.5)
        self.play(ReplacementTransform(a14, a14_copy))
        self.wait()
        self.play(Write(b14))
        self.wait()
        self.play(Write(b15))
        self.wait()
        b15_copy = b15.copy()
        b15_copy.shift(DOWN * 0.5)
        self.play(FadeOut(b15),FadeOut(b14))
        self.play(Write(b16))
        self.wait()
        self.play(Write(b17))
        self.wait()
        self.play(
            FadeOut(b16),FadeOut(b17),FadeOut(a14_copy)
        )
        self.wait()

class eight(Scene):
    def construct(self):
        a17 = TextMobject("\\texttt{Which ML model to use ??}")
        student = Alex(color=TEAL_A,flip_at_start= False).to_corner(DOWN )
        #student.scale(0.5)
        talk1 = wifi_creatureSays(
        student,a17,
        #bubble_kwargs={"height": 2, "width": 3.5},
        content_introduction_class=FadeIn,
        target_mode="speaking",
        bubble_class=ThoughtBubble,
        )

        self.play(talk1)
        self.wait(2)
        a17_copy = TextMobject("One-Class SVM")
        a17_copy.to_edge(UP * 2)
        a17_copy.set_color(BLUE)
        self.play(
           FadeOutAndShiftDown(self.mobjects[0]),FadeInFromDown(a17_copy))


        b19 = TextMobject(
            "The problem with this data is that the ratio of noactivity and \\\\ activity datapoints is 1:60")
        b20 = TextMobject(
            "In order to resolve this issue of imbalanced learning,\\\\ we have used \\texttt{One-Class SVM Classifier},\\\\ which creates a decision  boundary\\\\ using only activity datapoints")

        b19.next_to(a17_copy, DOWN, buff=0.5)
        b20.next_to(b19, DOWN, buff=0.5)
        b20[0][56:78].set_color(BLUE)
        #self.play(Write(a17))
        #self.wait()
        self.wait(0.5)
        self.play(Write(b19))
        self.wait(0.7)
        self.play(Write(b20), run_time=5)
        self.wait()

        self.play(
            FadeOut(a17_copy),
            FadeOut(b19),
            FadeOut(b20)
        )

class Analysis(one,two,three,four,five,six,seven,eight):
    def construct(self):
        one.construct(self)
        two.construct(self)
        three.construct(self)
        four.construct(self)
        five.construct(self)
        six.construct(self)
        seven.construct(self)
        eight.construct(self)



