from turtle import *

supp = Screen()
setup(1400, 700)
hideturtle()
colormode(255)

class Ambiente:
    """
    Muestra el dibujo dentro del cuadro.
    """
    def pisoVerde():
        """"""
        """Punto de inicio"""
        penup()
        goto(-640, -340)
        a = position()
        pendown()

        # Caracteristicas
        speed(2)
        pensize(1)
        color("green", "lightgreen")

        """Trazo (superior)""" 
        begin_fill()
        circle(100, 44)
        dot(10, 255, 0, 0)
        b = position()

        forward(100)
        dot(10, 255, 0, 0)
        c = position()

        right(19)
        forward(60)
        dot(10, 255, 0, 0)
        d = position()

        right(19)
        forward(40)
        dot(10, 255, 0, 0)
        e = position()

        right(8)
        forward(200)
        dot(10, 255, 0, 0)
        f = position()

        circle(100, 20)
        g = position()

        right(19)
        forward(70)
        dot(10, 255, 0, 0)
        h = position()

        right(10)
        forward(100)
        dot(10, 255, 0, 0)
        i = position()

        right(-10)
        forward(60)
        dot(10, 255, 0, 0)
        j = position()

        right(-8)
        forward(40)
        dot(10, 255, 0, 0)
        k = position()

        right(8)
        forward(70)
        dot(10, 255, 0, 0)
        l = position()

        right(-10)
        forward(50)
        dot(10, 255, 0, 0)
        m = position()
        
        right(8)
        forward(100)
        dot(10, 255, 0, 0)
        n = position()

        right(3)
        forward(300)
        dot(10, 255, 0, 0)
        o = position()

        right(10)
        forward(20)
        dot(10, 255, 0, 0)
        p = position()

        right(5)
        forward(30)
        dot(10, 255, 0, 0)
        q = position()

        right(-8)
        forward(10)
        dot(10, 255, 0, 0)
        r = position()
        
        goto(700, -260)
        dot(10, 255, 0, 0)
        s = position()
        
        """Cubierto inferior"""
        penup()
        speed(20)
        goto(700,-340) # 3er puntp del cuadro
        dot(10, 255, 0, 0)
        t = position()

        goto(-640,-340) # 1er punto del cuadro
        dot(10, 255, 0, 0)
        u = position()
        pendown()
        end_fill()

        """Imprimir corrdenadas"""
        print("\n")
        print([{x: y} 
        for x, y in zip("abcedfghijklmnopqrstu", 
        [a, b, c, e, d, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u])])
    

    def Fachada():
        """"""
        """Punto de inicio"""
        speed(20)
        penup()
        goto(57.97,-236.43) # Base Iz
        pendown()

        # Caracteristicas
        speed(2)
        pensize(3)
        color("gray")

        """Trazo (bordes)"""
        # begin_fill()
        goto(57.97, 136.43) # Sup Iz
        dot(10, 255, 0, 0)

        goto(616.85, 136.43) # Sup Der
        dot(10, 255, 0, 0)

        goto(616.85, -233.68) # Base Der
        dot(10, 255, 0, 0)

        """Cubierto inferior (pasto)"""
        penup()
        speed(20)
        goto(97.67,-231.55) 
        goto(167.66,-232.77) 
        goto(217.05,-224.95) 
        goto(57.97,-236.43)
        pendown()
        # end_fill()

    def Trasfondo():
        """"""
        """Punto de inicio"""
        speed(20)
        penup()
        goto(57.97, 136.43)
        pendown()

        """Trazo (lineas)"""
        speed(2)
        goto(116.10, 146.43) # Atras Iz
        dot(10, 255, 0, 0)

        goto(674.98, 146.43) # Atras Der
        dot(10, 255, 0, 0)
        goto(616.85, 136.43) # Adelante

        penup()
        goto(674.98, 146.43) # Atras Der
        pendown()

        goto(674.98,-248.17) # Base 

    def Wentana():
        """"""
        """Punto de inicio"""
        penup()
        goto(302, 0)
        dot(10, 255, 0, 0)
        pendown()

        # caracteristicas
        speed(20)
        color("lightblue")
        pensize(2)

        """Trazo (borde)"""
        goto()



class Description:
    def titulo():
        """Muestra los titulos"""
        supp.title("Python draw")
        penup()
        goto(-640, 240)
        pendown()

        color("darkred")
        write("UN DIBUJO HECHO EN TURTLE", font=("Cambria Math", 20, "normal"))

    def cuadro():
        """Muestra el cuadro donde se dibujará dentro."""
        speed(6)
        penup()
        goto(-640, -340)
        pendown()

        """Trazo (bordes)"""
        pensize(5)
        color("black")
        print("\nPuntos del cuadro:")
        for i in range(4):
            if i % 2 == 0:
                forward(1340)
            else:
                forward(600)
            left(90)
            print(position(), end=" ")




Description.titulo()
Description.cuadro()
Ambiente.pisoVerde()
Ambiente.Fachada()
Ambiente.Trasfondo()

mainloop()