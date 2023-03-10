from math import sin, cos

PI = 3.14159265

def radius_to_graus(radius):
      return (radius*180)/PI

def graus_to_radius(graus):
  return graus * (PI/180)

def get_p(angle, vortex, h):
    a = sin(angle)*h
    b = cos(angle)*h
    return [vortex[0]+a, vortex[1]+b]

class ArtificialHorizon:
    def __init__(self, vortex, size, angle=0, tk_canvas=None, pygame_instance=None):
        self.vortex = vortex
        self.size = size
        self.set_angle(angle)
        
        self.tk_canvas = tk_canvas
        self.pygame_instance = pygame_instance
        
        if tk_canvas:
            self.__create_tk_lines()
        
    def set_angle(self, value):
        self.angle = value
    
    def get_lines(self):
        space_size = int(self.size/5)
        space_plane = int(self.size/18)
        size_wigs = int(self.size/6)
        line1 = [get_p(graus_to_radius(self.angle-90), self.vortex, space_size), get_p(graus_to_radius(self.angle-90), self.vortex, self.size)]
        line2 = [get_p(graus_to_radius(self.angle-270), self.vortex, space_size), get_p(graus_to_radius(self.angle-270), self.vortex, self.size)]
        line3 = [line1[1], get_p(graus_to_radius(self.angle), line1[1], size_wigs)]
        line4 = [line2[1], get_p(graus_to_radius(self.angle), line2[1], size_wigs)]
        line5 = [[self.vortex[0],self.vortex[1]-space_plane], [self.vortex[0],self.vortex[1]-space_size+5]]
        line6 = [[self.vortex[0]-space_plane,self.vortex[1]], [self.vortex[0]-space_size+5,self.vortex[1]]]
        line7 = [[self.vortex[0]+space_plane,self.vortex[1]], [self.vortex[0]+space_size-5,self.vortex[1]]]
        return [line1, line2, line3, line4, line5, line6, line7]

    def __create_tk_lines(self):
        self.line1 = self.tk_canvas.create_line(0,0,0,0,fill='green')
        self.line2 = self.tk_canvas.create_line(0,0,0,0,fill='green')
        self.line3 = self.tk_canvas.create_line(0,0,0,0,fill='green')
        self.line4 = self.tk_canvas.create_line(0,0,0,0,fill='green')
        self.line5 = self.tk_canvas.create_line(0,0,0,0,fill='green')
        self.line6 = self.tk_canvas.create_line(0,0,0,0,fill='green')
        self.line7 = self.tk_canvas.create_line(0,0,0,0,fill='green')
    
    def update_artificial_horizon_tk(self, lines):
            self.tk_canvas.coords(self.line1,
                            lines[0][0][0],lines[0][0][1],lines[0][1][0],lines[0][1][1])
            self.tk_canvas.coords(self.line2,
                            lines[1][0][0],lines[1][0][1],lines[1][1][0],lines[1][1][1])
            self.tk_canvas.coords(self.line3,
                            lines[2][0][0],lines[2][0][1],lines[2][1][0],lines[2][1][1])
            self.tk_canvas.coords(self.line4,
                            lines[3][0][0],lines[3][0][1],lines[3][1][0],lines[3][1][1])
            self.tk_canvas.coords(self.line5,
                            lines[4][0][0],lines[4][0][1],lines[4][1][0],lines[4][1][1])
            self.tk_canvas.coords(self.line6,
                            lines[5][0][0],lines[5][0][1],lines[5][1][0],lines[5][1][1])
            self.tk_canvas.coords(self.line7,
                            lines[6][0][0],lines[6][0][1],lines[6][1][0],lines[6][1][1])
    
    def update_artificial_horizon_pygame(self, lines):
        for i in lines:
            self.pygame_instance.draw.line(self.screen, 'green', i[0], i[1], 1)
    
    def update(self, angle_value=None):
        if angle_value: self.set_angle(angle_value)
        lines = self.get_lines()
        if self.tk_canvas:
            self.update_artificial_horizon_tk(lines)
        if self.pygame_display:
            self.update_artificial_horizon_pygame(lines)
