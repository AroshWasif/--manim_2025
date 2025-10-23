
class javaedit(Scene):
    
    def construct(self):
        java_svg = SVGMobject(r"D:\manim code\java with manimm\java-svgrepo-com.svg")
        text = Text(r"Java Introduction").to_edge(UP)
        text.set_color_by_gradient(BLUE,RED)
        uder_line = Underline(text,color=BLUE)
        self.play(Create(java_svg))
        self.play(Write(text))
        self.play(Write(uder_line))
        self.wait(0.8)
        self.play(FadeOut(uder_line,text))

        text_1 = Text(r"What is Java ?").scale(1.4)
        text_1.set_color_by_gradient(BLUE,WHITE)
        text_1.to_edge(UP)
        
        t1 = Text(r"Java is a popular programming language, created in 1995.")
        t2 = Text(r"It is owned by Oracle, and more than 3 billion devices run Java.")
        t3 = Text(r"It is used for:")
        x = VGroup(t1, t2, t3).arrange(direction=DOWN).scale(0.7).next_to(text_1,2*DOWN)
        self.play(ReplacementTransform(java_svg,text_1,run_time=1.4))

        # tt1 =Text("Mobile applications    ")
        # tt2 =Text("Desktop applications   ") 
        # tt3 =Text("    Web applications Games ") 
        # tt4 =Text("And much, much more!   ")
        # x1 = VGroup(tt1,tt2,tt3,tt4).arrange(direction=DOWN, aligned_edge=RIGHT).scale(0.5).next_to(RIGHT,DL)

        self.play(Write(x))

        conditions_text = [
                "• Mobile applications ",
                "• Desktop applications",
                "• Web applications Games",
                "• And much, much more!"
            ]
        

        conditions_list = VGroup(*[Text(cond).scale(0.5 )for cond in conditions_text])
        conditions_list.arrange(DOWN, aligned_edge=LEFT).next_to(x, DOWN, buff=0.7).to_edge(LEFT)

        for condition in conditions_list:
            self.play(FadeIn(condition, shift=UP))
            self.wait(0.5)


        # self.play(Write(x1))
        self.wait(2)
        self.play(FadeOut(text_1,x,conditions_list))

        text3 = Text(r"Java Getting Started").to_edge(UP)
        text3.set_color_by_gradient(BLUE,WHITE)
        under_line2 = Underline(text3,color=BLUE)
        self.play(Write(text3))
        self.play(Write(under_line2))

        '''vs code '''
        vs= SVGMobject(r"D:\2.java\vs-code-svgrepo-com.svg").to_edge(ORIGIN)
        vs.set_color_by_gradient("#32B5F1","#2B9FED","#0F6FB3","#1279B7","#1176B5","#0E69AC","#0F70AF","#0F6DAD","#1791D2","#1173C5")
#         vts = Text(r"Open VScode",color=YELLOW).scale(0.7)
#         vts.next_to(vs,DOWN,buff=0.9)
#         sur_1 = SurroundingRectangle(vts,color=PINK)





#         self.play(
#             Write(vs),
#             Write(vts),
#             Write(sur_1),
#             run_time = 2

# )
#         self.wait(1)
#         self.play(FadeOut(vs,vts,sur_1))
        '''ggg'''
        '''ggg'''
        a_x = Text(r"Open")
        b_x = Text(r"VScode")
        self.add(a_x, b_x)
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    a_x.animate(run_time=1).shift(RIGHT * 8),
                    b_x.animate(run_time=1).shift(LEFT * 8),
                ),
                speedinfo={0.3: 1, 0.4: 0.1, 0.6: 0.1, 1: 1},
                rate_func=linear,
            )
        )
        self.play(FadeOut(a_x,b_x,run_time=0.2))
        self.play(Write(vs))
        self.wait(0.4)
        self.play(FadeOut(vs,run_time=0.3))
        '''hh'''


        code = '''public class Main {
  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}'''

        rendered_code = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "blue"},
        )
        self.play(Create(rendered_code,run_time=4))
        self.wait(1.5)


class java1(Scene):
    def construct(self):
        ver = Text(r"Java Variables").to_edge(UP)
        ver.set_color_by_gradient(BLUE,WHITE,BLUE)
        under_line = Underline(ver,color=BLUE)
        self.play(FadeIn(ver,under_line))
        self.wait(0.5)

        t1 = Text(r"Variables are containers for storing data values.",).next_to(ver,DOWN,buff=0.3)
        t1.scale(0.6)
        t2 = Text(r"In Java, there are different types of variables, for example:").scale(0.6)
        t2.next_to(t1,DOWN,buff=0.3)

        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(1)

        code = '''int myNum = 5;
float myFloatNum = 5.99f;
char myLetter = 'D';
boolean myBool = true;
String myText = "Hello";'''

        rendered_code = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "green"},
        )
        rendered_code.next_to(t2,DOWN,buff=0.5)
        self.play(Create(rendered_code,run_time=4))
        self.wait(1.5)

        code = '''int x = 5;
int y = 6;
int z = 50;
System.out.println(x + y + z);'''

        rendered_code1 = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "green"},
        )
        rendered_code1.next_to(t2,DOWN,buff=0.5)
        self.play(ReplacementTransform(rendered_code,rendered_code1,run_time=1.2))
        self.wait(1.6)

        code = '''int x = 5, y = 6, z = 50;
System.out.println(x + y + z);
//Multiple Variables'''

        rendered_code2 = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "blue"},
        )
        rendered_code2.next_to(t2,DOWN,buff=0.5)
        self.play(ReplacementTransform(rendered_code1,rendered_code2,run_time=1.4))
        self.wait(1)


class Javaifelse2(Scene):
    def construct(self):
        title = Text(r"Java Conditions and If Statements").scale(1)
        
        title.to_edge(UP)
        title.set_color_by_gradient(BLUE,WHITE,BLUE)
        under_line = Underline(title,color=RED)
        self.play(Write(title))
        self.play(Write(under_line))
        self.wait(0.5)

        conditions_text = [
            "• Less than: a < b",
            "• Less than or equal to: a <= b",
            "• Greater than: a > b",
            "• Greater than or equal to: a >= b",
            "• Equal to: a == b",
            "• Not Equal to: a != b"
        ]

        conditions_list = VGroup(*[Text(cond).scale(0.6 )for cond in conditions_text])
        conditions_list.arrange(DOWN, aligned_edge=LEFT).next_to(title, DOWN, buff=1).to_edge(LEFT)

        for condition in conditions_list:
            self.play(FadeIn(condition, shift=UP))
            self.wait(0.5)

        self.wait(2)


class if_Statement3(Scene):
    def construct(self):
        title = Text(r"The if Statement").to_edge(UP)
        title.set_color_by_gradient(BLUE,WHITE,BLUE)

        snake = SVGMobject(r"D:\manim code\New folder\octopus-svgrepo-com.svg").scale(1.7)
        snake.to_corner(DR)
        self.add(snake)
        hat = snake[2] 
        sing = snake[13:15] #upor e sing jabe 
        eye = snake[16:18]

        # চোখকে কয়েকবার হালকা নড়ানো


        code = '''public class Main {
  public static void main(String[] args) {
    int x = 20;
    int y = 18;
    if (x > y) {
      System.out.println("x is greater than y");
    }  
  }
}'''

        rendered_code = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "blue"},
        )
        # self.play(Create(rendered_code,run_time=4))
        rendered_code.scale(0.8)
        # rendered_code.next_to(title,DOWN,buff=0.7)
        rendered_code.to_corner(UL,buff=2)

        

        self.play(Write(title,run_time=0.9),eye.animate.shift(LEFT * 0.15), run_time=1.2)
        self.play(Create(rendered_code,run_time=4),sing.animate.shift(UP * 0.22), run_time=2)



        self.wait(2)


class if_else_statement4(Scene):
    def construct(self):
        title = Text(r"The else if Statement").to_edge(UP)
        title.set_color_by_gradient(BLUE,WHITE,BLUE)
        under_line = Underline(title,color=BLUE)
        self.play(Write(title))
        self.play(Write(under_line))
        self.wait(0.6)
        code = '''public class Main {
  public static void main(String[] args) {
    int time = 22;
    if (time < 10) {
      System.out.println("Good morning.");
    } else if (time < 18) {
      System.out.println("Good day.");
    }  else {
      System.out.println("Good evening.");
    }
  }
}'''

        rendered_code = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "maroon"},
        )
        self.play(Create(rendered_code,run_time=7))
        self.wait(2)


class java_switch5(Scene):
    def construct(self):
        Title = Text("Java Switch Statements").to_edge(UP)
        Title.set_color_by_gradient(BLUE,WHITE,BLUE)
        unede = Underline(Title,color=TEAL)
        self.play(Write(Title))
        self.play(Write(unede))
        t1 = Text(r"Instead of writing many if..else statements, you can use ").scale(0.7)
        t2 = Text(r"the switch statement.The switch statement selects one of ").scale(0.7)
        t3 = Text(r"many code blocks to be executed:").scale(0.7)
        t1.next_to(Title,DOWN,buff=1.2)
        t2.next_to(t1,DOWN,buff=0.2)
        t3.next_to(t2,DOWN,buff=0.2)
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))

        self.wait(2)
        self.play(FadeOut(t1,t2,t3))

        code = '''int number = 7;

switch (number % 2) {
    case 0:
        System.out.println("Even number");
        break;
    case 1:
        System.out.println("Odd number");
        break;
}'''

        rendered_code = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "maroon"},
        )
        # rendered_code.scale(0.6)
        rendered_code.next_to(Title,DOWN,buff=0.3)
        self.play(Create(rendered_code,run_time=4))
        self.wait(2)


class java_loop6(Scene):
    def construct(self):
        Title = Text(r"Java While Loop").to_edge(UP)
        Title.set_color_by_gradient(TEAL,WHITE,TEAL)
        under_line = Underline(Title,color=BLUE)
        self.play(Write(Title))
        self.play(Write(under_line))
        self.wait(0.6)

        
        while_loop= Text(r"Java-এর while loop হল এমন একটি control structure যা কোনো নির্দিষ্ট ",font="Kalpurush").scale(0.7).next_to(Title,DOWN,buff=1.2)
        while_loop1= Text(r"condition true থাকা পর্যন্ত বারবার একটি block of code execute করে।",font="kalpurush").scale(0.7).next_to(while_loop,DOWN,buff=0.3)
        self.play(Write(while_loop))
        self.play(Write(while_loop1))
        self.wait(1.4)
        self.play(FadeOut(while_loop,while_loop1))

        code = '''public class Main {
  public static void main(String[] args) {
    int i = 0;
    while (i < 5) {
      System.out.println(i);
      i++;
    }  
  }
}
'''

        rendered_code = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "maroon"},
        )
        # rendered_code.scale(0.6)
        # rendered_code.next_to(Title,DOWN,buff=0.3)
        rendered_code.to_corner(UL,buff=1.5)
        self.play(Create(rendered_code,run_time=5))
        self.wait(2)


class forloop7(Scene):
    def construct(self):
        snake = SVGMobject(r"D:\manim code\New folder\octopus-svgrepo-com.svg").scale(1.7)
        snake.to_corner(DR)
        


        Title = Text(r"Java For Loop").to_edge(UP)
        Title.set_color_by_gradient(TEAL,WHITE,TEAL)
        under = Underline(Title,color=BLUE)
        self.play(Write(Title))

        self.play(Write(under))
        self.wait(0.5)

        for_loop= Text(r"Java For Loop হলো একটি iteration control structure যা আপনাকে ",font="Kalpurush").scale(0.7).next_to(Title,DOWN,buff=1.2)

        for_loop1= Text(r"নির্দিষ্ট সংখ্যক বার একটি block of code execute করতে দেয় ",font="kalpurush").scale(0.7).next_to(for_loop,DOWN,buff=0.3)
        self.play(Write(for_loop))
        self.play(Write(for_loop1))
        self.wait(1.3)
        self.play(FadeOut(for_loop,for_loop1))


        code = '''public class Main {
  public static void main(String[] args) {
    for (int i = 0; i < 5; i++) {
      System.out.println(i);
    }  
  }
}'''

        rendered_code = Code(
            code_string=code,
            language="c++",
            background="window",
            background_config={"stroke_color": "blue"},
        )
        self.add(snake)
        hat = snake[2] 
        sing = snake[13:15] #upor e sing jabe 
        eye = snake[16:18]
        rendered_code.scale(0.8)
        rendered_code.to_corner(UP,buff=1.5)
        self.play(Create(rendered_code,run_time=4),eye.animate.shift(LEFT * 0.15), run_time=2)
        self.play(eye.animate.shift(UP * 0.10), run_time=2)
        self.wait(2)

        

        code = '''// Outer loop
for (int i = 1; i <= 2; i++) {
  System.out.println("Outer: " + i); 
  // Inner loop
  for (int j = 1; j <= 3; j++) {
    System.out.println(" Inner: " + j);
  }
}'''

        rendered_code1 = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "blue"},
        )
        rendered_code1.scale(0.7)
        self.play(ReplacementTransform(rendered_code,rendered_code1))
        self.play(hat.animate.shift(UP * 0.22), run_time=2)
        self.wait(2)
      

class java_Array8(Scene):
    def construct(self):
        Title = Text(r"Java Arrays").to_edge(UP)
        Title.set_color_by_gradient(BLUE,WHITE,BLUE)
        under = Underline(Title,color=BLUE)
        self.play(Write(Title))
        self.play(Write(under))
        self.wait(0.6)

        # tt = Text(r" 🧠 Java Array-এর মূল বৈশিষ্ট্য:",font="Kalpurush").scale(0.7).next_to(Title,DOWN,buff=1.2)
        # t1 = Text(r"Instead of writing many if..else statements, you can use ").scale(0.7)
        tt = Text(r"Arrays are used to store multiple values in a single variable,").scale(0.7).next_to(Title,DOWN,buff=1.2)
        tt2 =Text(r"instead of declaring separate variables for each value.").scale(0.7).next_to(tt,DOWN,buff=0.3)
        tt3 = Text(r"To declare an array, define the variable type with square brackets:").scale(0.7).next_to(tt2,DOWN,buff=0.3)
        

        
        self.play(Write(tt))
        self.play(Write(tt2))
        self.play(Write(tt3))
        self.wait(1.3)
        code = '''String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};'''

        rendered_code = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "white"},
        )
        rendered_code.next_to(tt3,DOWN,buff=0.5)
        self.play(Create(rendered_code,run_time=2))


        self.wait(2)
        # self.play(FadeOut(tt,tt2,tt3,rendered_code))


class java_Array9(Scene):
        def construct(self):
            Title = Text(r"Java Arrays").to_edge(UP)
            Title.set_color_by_gradient(BLUE,WHITE,BLUE)
            under = Underline(Title,color=BLUE)
            self.add(Title)
            self.add(under)
            self.wait(0.4)
            array_tt = Text(r"🧠 Java Array-এর মূল বৈশিষ্ট্য:",font="kalpurush").scale(0.8).next_to(Title,DOWN,buff=0.6)
            self.play(Write(array_tt))

            


            conditions_text = [
                "• Same type values: সব elements একই data type-এর হয় (যেমন int[], String[])",
                "• Fixed size: একবার array তৈরি হলে তার size পরিবর্তন করা যায় না",
                "• Indexing starts at 0: প্রথম element-এর index হয়"
            ]
        

            conditions_list = VGroup(*[Text(cond,font="Kalpurush").scale(0.5 )for cond in conditions_text])
            conditions_list.arrange(DOWN, aligned_edge=LEFT).next_to(array_tt, DOWN, buff=0.7).to_edge(LEFT)

            for condition in conditions_list:
                self.play(FadeIn(condition, shift=UP))
                self.wait(0.5)
            
            sor = SurroundingRectangle(conditions_list,color=BLUE)
            self.play(Write(sor))

            self.wait(2)


class mathod10(Scene):
    def construct(self):
        Title = Text(r"Java Methods").to_edge(UP)
        Title.set_color_by_gradient(BLUE_C,WHITE,BLUE_C)
        under = Underline(Title,color=RED_C)

  
        man = SVGMobject(r"D:\manim code\charecter\man.svg")

        
        # self.play(Create(man))
        eye = man[4:6]

        eye_pata = man[7]
        

        self.play(
            Write(Title),
            Write(man)
        )
        self.play(Write(under),eye.animate.shift(UP * 0.10))

        self.wait(0.3)

        # t= Text(r"Java-এর while loop হল এমন একটি control structure যা কোনো নির্দিষ্ট ",font="Kalpurush").scale(0.7).next_to(Title,DOWN,buff=1.2)
        t2=Text(r"Java-এর method হলো এমন একটি কোড ব্লক যা নির্দিষ্ট কাজ সম্পাদন করে। ",font="Kalpurush").scale(0.7).next_to(Title,DOWN,buff=1.2)
        t =Text(r"এগুলো class-এর ভিতরে define করা হয় এবং যখন প্রয়োজন হয় তখন ",font="Kalpurush").scale(0.7).next_to(t2,DOWN,buff=0.3)
        t3 = Text(r"call করা হয়।",font="Kalpurush").scale(0.7).next_to(t,DOWN,buff=0.3)
        self.play(Write(t2),man.animate.shift(DOWN * 2), run_time=2)
        self.play(Write(t),eye.animate.shift(UP * 0.10), run_time=2)
        self.play(Write(t3),eye.animate.shift(DOWN * 0.10), run_time=2)
        self.wait(1.2)


        java = Text(r"JAVA code").scale(0.7)
        pyhton = Text(r"PYTHON code").scale(0.7)
        java.set_color_by_gradient(BLUE,RED)
        java.to_corner(UL,buff=1.5)
        pyhton.set_color_by_gradient(BLUE,RED)
        pyhton.to_corner(UR,buff=1.5)

        # self.play(Write(java))
        # self.play(Write(pyhton))
        code = '''public class Main {
  static void myMethod() {
    System.out.println("I just got executed!");
  }

  public static void main(String[] args) {
    myMethod();
  }
}'''

        rendered_code1 = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "blue"},
        )
        rendered_code1.scale(0.7)
        # rendered_code1.next_to(java,DOWN,buff=1.4)
        rendered_code1.to_corner(LEFT)




        code = '''def my_Method():

    print("I just got executed!")

my_Method()'''

        rendered_code = Code(
            code_string=code,
            language="python",
            background="window",
            background_config={"stroke_color": "blue"},
        )
        rendered_code.scale(0.7)
        # rendered_code.to_corner(UR)
        rendered_code.to_corner(RIGHT)
        self.play(FadeOut(t2,t,t3))

        self.play(man.animate.shift(DOWN * 0.9), run_time=2)
        self.play(Write(java),eye.animate.shift(UP * 0.05), run_time=2)
        self.play(Write(pyhton),eye.animate.shift(UP * 0.05), run_time=2)
        self.play(
            Create(rendered_code1,run_time=4),
            Create(rendered_code,run_time=4)
            #TransformFromCopy(rendered_code1,java,run_time=2),
            #TransformFromCopy(rendered_code,pyhton,run_time=2)
        )
        # self.play(eye.animate.shift(UP * 0.10), run_time=2)
        self.play(eye.animate.shift(DOWN * 0.10), run_time=2)
        self.wait(2)

        self.play(FadeOut(java,pyhton,rendered_code1,rendered_code))
        self.play(man.animate.shift(RIGHT*4), run_time=2)

        tt = Text("Java Method Parameters").scale(0.7)
        tt.to_corner(UL,buff=1.5)
        tt.set_color_by_gradient(GREEN,PURPLE,GREEN)
        self.play(Write(tt),eye.animate.shift(UP * 0.10), run_time=2)


        code = '''public class Main {
  static void myMethod(int x ,int y) {
    System.out.println(x + y);  
  }
  public static void main(String[] args) {
    myMethod(10,5);
    myMethod(12,6);
  }
}'''

        rend = Code(
            code_string=code,
            language="java",
            background="window",
            background_config={"stroke_color": "blue"},
        )
        c1 = Ellipse(color=WHITE).scale(0.4)
        c2 = Ellipse(color=WHITE).scale(0.2)
        c3 = Ellipse(color=WHITE).scale(0.1)
        
        c1.move_to([2,-1.8,0])
        c2.next_to(c1,DR,buff=0.01)
        c3.next_to(c2,DR,buff=0.01)

        self.play(
            Write(c1),
            Write(c2),
            Write(c3)
        )
        rend.scale(0.8)
        rend.to_corner(LEFT)
        self.play(Create(rend,run_time=9),eye.animate.shift(LEFT * 0.10), run_time=2)
        
        self.wait(3)

