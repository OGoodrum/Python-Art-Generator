from typing import IO, NamedTuple
import random as rd

class Irange(NamedTuple):
    '''Irange class'''
    min: int
    max: int

    def __str__(self) -> str:
        return f'{self.min},{self.max}'

class Frange(NamedTuple):
    '''Frange class'''
    min: float
    max: float

    def __str__(self) -> str:
        return f'{self.min},{self.max}'

#print(__doc__)
class PyArtConfig:
    '''PyArtConfig class'''
    xrange: Irange = Irange(0, 500)
    yrange: Irange = Irange(0, 300)
    radius: Irange = Irange(0, 100)
    radiusx: Irange = Irange(10, 30)
    radiusy: Irange = Irange(10, 30)
    width: Irange = Irange(10, 100)
    height: Irange = Irange(10, 100)
    red: Irange = Irange(0, 255)
    green: Irange = Irange(0, 255)
    blue: Irange = Irange(0, 255)
    opacity: Frange = Frange(0.0, 1.0)
    

    def __init__(self, style: dict) -> None:
        self.shape: Irange = Irange(0, 1)
        self.xrange: Irange = Irange(0, 500)
        self.yrange: Irange = Irange(0, 300)
        self.radius: Irange = Irange(0, 100)
        self.radiusx: Irange = Irange(10, 30)
        self.radiusy: Irange = Irange(10, 30)
        self.width: Irange = Irange(10, 100)
        self.height: Irange = Irange(10, 100)
        self.red: Irange = Irange(0, 255)
        self.green: Irange = Irange(0, 255)
        self.blue: Irange = Irange(0, 255)
        self.opacity: Frange = Frange(0.0, 1.0)
        self.count: Irange = Irange(5, 100)

        if style.get("Size") == "Small":
            self.radius: Irange = Irange(0, 30)
            self.radiusx: Irange = Irange(10, 20)
            self.radiusy: Irange = Irange(10, 20)
            self.width: Irange = Irange(10, 30)
            self.height: Irange = Irange(10, 30)
        elif style.get("Size") == "Large":
            self.radius: Irange = Irange(70, 100)
            self.radiusx: Irange = Irange(20, 30)
            self.radiusy: Irange = Irange(20, 30)
            self.width: Irange = Irange(70, 100)
            self.height: Irange = Irange(70, 100)
        
        if style.get("Colour") == "Purple":
            self.red: Irange = Irange(75, 255)
            self.green: Irange = Irange(0, 0)
            self.blue: Irange = Irange(130, 255)
        elif style.get("Colour") == "Green":
            self.red: Irange = Irange(0, 50)
            self.green: Irange = Irange(50, 255)
            self.blue: Irange = Irange(0, 50)
        elif style.get("Colour") == "Blue":
            self.red: Irange = Irange(0, 50)
            self.green: Irange = Irange(0, 50)
            self.blue: Irange = Irange(50, 255)

        if style.get("Shape") == "Circle":
            self.shape: Irange = Irange(0, 0)
        elif style.get("Shape") == "Rectangle":
            self.shape: Irange = Irange(1, 1)

        if "Count" in style:
            self.count: Irange = Irange(style["Count"], style["Count"])
            
    


class RandomShape:
    '''RandomShape class'''

    cnt: int = -1

    def __init__(self, config: PyArtConfig):
        self.sha: int = rd.randint(config.shape.min, config.shape.max)
        self.x: int = rd.randint(config.xrange.min, config.xrange.max)
        self.y: int = rd.randint(config.yrange.min, config.yrange.max)
        self.radius: int = rd.randint(config.radius.min, config.radius.max)
        self.radiusx: int = rd.randint(config.radiusx.min, config.radiusx.max)
        self.radiusy: int = rd.randint(config.radiusy.min, config.radiusy.max)
        self.width: int = rd.randint(config.width.min, config.width.max)
        self.height: int = rd.randint(config.height.min, config.height.max)
        self.red: int = rd.randint(config.red.min, config.red.max)
        self.green: int = rd.randint(config.green.min, config.green.max)
        self.blue: int = rd.randint(config.blue.min, config.blue.max)
        self.opacity: int = round(rd.uniform(config.opacity.min, config.opacity.max), 2)
        RandomShape.cnt += 1
        

    def as_Part2_line(self) -> str:
        '''as_Part2_Line method'''
        return f"{RandomShape.cnt: >5}{self.sha: >5}{self.x: >5}{self.y: >5}{self.radius: >5}{self.radiusx: >5}{self.radiusy: >5}{self.width: >5}{self.height: >5}{self.red: >5}{self.green: >5}{self.blue: >5}{self.opacity:>5}\n"
    
    def as_svg(self) -> str:
        '''as_svg method'''
        if self.sha == 0:
            line1: str = f'<circle cx="{self.x}" cy="{self.y}" r="{self.radius}" '
            line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.opacity}"></circle>'
            return f"{line1+line2}\n"
        else:
            line1: str = f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" '
            line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.opacity}"></rect>'
            return f"{line1+line2}\n"


    


class CircleShape:
    """Circle class"""
    ccnt: int = 0

    def __init__(self, cir: tuple, col: tuple) -> None:
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
        CircleShape.ccnt += 1

class RectangleShape:
    """Rectangle class"""

    rcnt: int = 0
    
    def __init__(self, pos: tuple, rect: tuple, col: tuple) -> None:
        self.x: int = pos[0]
        self.y: int = pos[1]
        self.width: int = rect[0]
        self.height: int = rect[1]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
        RectangleShape.rcnt += 1
        



class HtmlDocument:
    """An HTML document that allows appending SVG content"""
    TAB: str = "   "  # HTML indentation tab (default: three spaces)

    def __init__(self, file_name: str, win_title: str) -> None:
        self.win_title: str = win_title
        self.__tabs: int = 0
        self.__file: IO = open(file_name, "w")
        self.__write_head()

    def increase_indent(self) -> None:
        """Increases the number of tab characters used for indentation"""
        self.__tabs += 1

    def decrease_indent(self) -> None:
        """Decreases the number of tab characters used for indentation"""
        self.__tabs -= 1

    def append(self, content: str) -> None:
        """Appends the given HTML content to this document"""
        ts: str = HtmlDocument.TAB * self.__tabs
        self.__file.write(f'{ts}{content}\n')

    def __write_head(self) -> None:
        """Appends the HTML preamble to this document"""
        self.append('<html>')
        self.append('<head>')
        self.increase_indent()
        self.append(f'<title>{self.win_title}</title>')
        self.decrease_indent()
        self.append('</head>')
        self.append('<body>')

    def __write_comment(self, comment: str) -> None:
        """Appends an HTML comment to this document"""
        self.append(f'<!--{comment}-->')

    def addSvg(self, canvas: tuple) -> None:
        '''addSvg method'''
        self.svg = SvgCanvas(canvas, self.__file)

    def closeHtml(self) -> None:
        '''closeHtml method'''
        self.append('</body>')
        self.append('</html>')
        self.__file.close()
    
    def genArt(self, config: PyArtConfig) -> None:
        '''genArt method'''
        self.addSvg((500, 300))
        self.svg.openCanvas()

        for x in range(rd.randint(config.count.min, config.count.max)):
            shape: RandomShape = RandomShape(config)
            if shape.sha == 0:
                circle: CircleShape = CircleShape((shape.x, shape.y, shape.radius), (shape.red, shape.green, shape.blue, shape.opacity))
                self.svg.drawCircleLine(circle)
            else:
                rectangle: RectangleShape = RectangleShape((shape.x, shape.y), (shape.width, shape.height), (shape.red, shape.green, shape.blue, shape.opacity))
                self.svg.drawRectangleLine(rectangle)

        self.svg.closeCanvas()



class SvgCanvas:
    """SVG class"""
    def __init__(self, canvas: tuple, f: IO) -> None:
        self.canvas = canvas
        self.f = f
        self.t = 1


    def openCanvas(self) -> None:
        """openSVGcanvas method"""
        ts: str = "   " * self.t
        #super().__write_comment("Define SVG drawing box")
        self.f.write(f'{ts}<svg width="{self.canvas[0]}" height="{self.canvas[1]}">\n')

    def closeCanvas(self) -> None:
        """closeSVGcanvas method"""
        ts: str = "   " * self.t
        self.f.write(f"{ts}</svg>\n")

    def drawCircleLine(self, c: CircleShape) -> None:
        """drawCircle method"""
        ts: str = "   " * self.t
        line1: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" '
        line2: str = f'fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
        self.f.write(f"{ts}{line1+line2}\n")

    def drawRectangleLine(self, r: RectangleShape) -> None:
        """drawRectangle method"""
        ts: str = "   " * self.t
        line1: str = f'<rect x="{r.x}" y="{r.y}" width="{r.width}" height="{r.height}" '
        line2: str = f'fill="rgb({r.red}, {r.green}, {r.blue})" fill-opacity="{r.op}"></rect>'
        self.f.write(f"{ts}{line1+line2}\n")

    def genArt(self) -> None:
        """genART method"""
        self.drawCircleLine(CircleShape((50,50,50), (255,0,0,1.0)))
        self.drawCircleLine(CircleShape((150,50,50), (255,0,0,1.0)))
        self.drawCircleLine(CircleShape((250,50,50), (255,0,0,1.0)))
        self.drawCircleLine(CircleShape((350,50,50), (255,0,0,1.0)))
        self.drawCircleLine(CircleShape((450,50,50), (255,0,0,1.0)))
        self.drawCircleLine(CircleShape((50,250,50), (0,0,255,1.0)))
        self.drawCircleLine(CircleShape((150,250,50), (0,0,255,1.0)))
        self.drawCircleLine(CircleShape((250,250,50), (0,0,255,1.0)))
        self.drawCircleLine(CircleShape((350,250,50), (0,0,255,1.0)))
        self.drawCircleLine(CircleShape((450,250,50), (0,0,255,1.0)))

    # more methods needed here


        


def main() -> None:
    """main method"""
    html: HtmlDocument = HtmlDocument("a434.html", 'My Art')

    #These elements of the dict can be changed to certain things or be left as None if you want that element to be random
    style: dict = {"Size": "Small", "Colour": "Green", "Shape": None, "Count": 1000}
    config: PyArtConfig = PyArtConfig(style)

    html.genArt(config)

    html.closeHtml()


if __name__ == "__main__":
    main()