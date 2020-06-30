  #!/usr/bin/env python

from manimlib.imports import *
from wifi_creature.wifi_creature import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=10,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):

        example_text = TextMobject(
            "Should we name it triNETRA?",
            tex_to_color_map={"tri": RED,"?" :RED,"NETRA" : BLUE}
        )
        '''
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        '''

        #group = VGroup(example_text, example_tex)
        group = VGroup(example_text)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(FadeInFromDown (example_text))
        #self.play(Write(example_tex))
        self.wait(5)

class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()


class wifi_creature(Scene):
    def construct(self):
        creature = SVGMobject("wifi_creature.svg")\
                .scale(4)

        '''
        creature[2].set_color(BLACK)
        creature[3].set_color(BLACK)
        creature[4].set_color(RED)
        creature[5].set_color(RED)
        creature[6].set_color(RED)
        creature[7].set_color(RED)
        creature[8].set_color(BLACK)
        '''
        self.add(creature)

# See old_projects folder for many, many more
class NumberScene(Scene):
    def construct(self):
        Ale=Alex().to_edge(DOWN)
        palabras_ale = TextMobject("Hmmm..")
        get_me_name = TextMobject("LOL..")
        self.add(Ale)
        teto = wifi_creatureSays(
            Ale, palabras_ale,
            bubble_kwargs={"height": 2, "width": 2.76},
            target_mode="speaking"
        )
        self.play(teto)

        self.wait()
        self.play(Blink(Ale))
        self.remove()
        self.wait(3)


        self.play(wifi_creatureSays(
            Ale, get_me_name,
            bubble_kwargs = {"height" : 3, "width" : 4},
            target_mode="speaking"
        ))

        self.wait(1)
        self.play(Blink(Ale))
        self.wait(1)
        #self.play(shrug())
        self.play(Blink(Ale))
        self.wait(1)

class SVGTest(Scene):
    def construct(self):
        creature= SVGMobject("github.svg")\
                .scale(3)

        '''
        
        creature[2].set_color(BLACK)
        creature[3].set_color(BLACK)
        creature[4].set_color(RED)
        creature[5].set_color(BLUE)
        creature[6].set_color(RED)
        creature[7].set_color(RED)
        creature[8].set_color(BLACK)
        for i in creature:
            if(i!=creature[5]):

                self.play(Write(i))
                self.wait(0.35)
        '''


        self.play(Write(creature))
class mcqueen(Scene):
    def construct(self):
        prof = Alex(color=RED_E, flip_at_start=False).move_to(LEFT)

        t3 = TextMobject("Ka-Ciao!!")
        t3.set_color(RED_E)
        t3.scale(2)
        talk3 = wifi_creatureSays(
        prof,t3.scale(2),
        bubble_kwargs={"height": 2.5, "width": 6,"fill_color": YELLOW_B,"stroke_color": BLACK},

        content_introduction_class=Write,
        target_mode="speaking",
        bubble_class=SpeechBubble,
        )

        self.play(talk3)
        prof.look_at(2*UP + RIGHT)
        self.add(prof)
        self.wait(3)
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
        grp.arrange(UP+RIGHT)
        self.play(Write(grp))
        self.wait()
        Txt = TextMobject("Surya291")
        self.play(Write(Txt.next_to(grp,DOWN,buff=1)))
        self.wait(3)






class Matrix_exam(Scene):
    def construct(self): #no usar siempre frac


        l1 = Line(UP*0.5+LEFT * 5, UP*0.5+RIGHT *5)
        l2 = Line(DOWN*0.5+LEFT * 5, DOWN*0.5+RIGHT * 5)
        #l3 = DashedLine(UP*1+LEFT*(3.5-0.2),DOWN*1+LEFT*(3.5-0.2))
        #l4 = DashedLine(UP * 1 + RIGHT * (3.5-0.2), DOWN * 1 + RIGHT * (3.5-0.2))

        rect = Rectangle(height = 1,width = 10,color = 'RED')

        text = VGroup(

            *[SmallDot(LEFT*(i*0.5 + 2)) for i in range(2,5)],
            *[SmallDot(RIGHT * (i * 0.5 +2)) for i in range(2, 5)],
        )
        text.add(l1)
        text.add(l2)
        #text.add(l3)
        #text.add(l4)
        text.add(rect)
        real = TexMobject("H_{1,A,t} \quad",
                          "H_{1,B,t}\quad",
                          " H_{1,C,t}")

        self.play(Write(text))

        self.wait()

        self.play(Write(real))
        self.wait()

