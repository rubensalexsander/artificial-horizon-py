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
    def __init__(self, vortex, size, angle=0, tk_canvas=None, pygame_display=None):
        self.vortex = vortex
        self.size = size
        self.set_angle(angle)
        self.meta_angle = angle
        
        self.tk_canvas = tk_canvas
        self.pygame_display = pygame_display
        
        if tk_canvas:
            self.__create_tk_lines()
        if self.pygame_display:
            import pygame
            self.pygame = pygame
        
    def set_angle(self, value):
        self.angle = value
    
    def get_lines(self):
        space_size = int(self.size/5) #Tamanho do espaço do horizonte artificial
        space_plane = int(self.size/20) #Tamanho do avião do centro
        size_wigs = int(self.size/10) #Tamanho das asas laterais
        lines = []
        lines.append([get_p(graus_to_radius(self.meta_angle-90), self.vortex, space_size), get_p(graus_to_radius(self.meta_angle-90), self.vortex, self.size)])
        lines.append([get_p(graus_to_radius(self.meta_angle-270), self.vortex, space_size), get_p(graus_to_radius(self.meta_angle-270), self.vortex, self.size)])
        lines.append([get_p(graus_to_radius(self.meta_angle-90), self.vortex, self.size), get_p(graus_to_radius(self.meta_angle), get_p(graus_to_radius(self.meta_angle-90), self.vortex, self.size), size_wigs)])
        lines.append([get_p(graus_to_radius(self.meta_angle-270), self.vortex, self.size), get_p(graus_to_radius(self.meta_angle), get_p(graus_to_radius(self.meta_angle-270), self.vortex, self.size), size_wigs)])
        '''lines.append([[self.vortex[0],self.vortex[1]-space_plane], [self.vortex[0],self.vortex[1]-space_size+5]])
        lines.append([[self.vortex[0]-space_plane,self.vortex[1]], [self.vortex[0]-space_size+5,self.vortex[1]]])
        lines.append([[self.vortex[0]+space_plane,self.vortex[1]], [self.vortex[0]+space_size-5,self.vortex[1]]])'''
        lines.append([[self.vortex[0],self.vortex[1]-space_plane], [self.vortex[0],self.vortex[1]-space_size+8]])
        lines.append([[self.vortex[0]-space_plane,self.vortex[1]], [self.vortex[0]-space_size+8,self.vortex[1]]])
        lines.append([[self.vortex[0]+space_plane,self.vortex[1]], [self.vortex[0]+space_size-8,self.vortex[1]]])
        lines.append([[self.vortex[0]-space_plane,self.vortex[1]], [self.vortex[0],self.vortex[1]+space_plane]])
        lines.append([[self.vortex[0]+space_plane,self.vortex[1]], [self.vortex[0],self.vortex[1]+space_plane]])
        
        return lines

    def __create_tk_lines(self):
        self.tk_lines = [self.tk_canvas.create_line(0,0,0,0,fill='green') for i in range(len(self.get_lines()))]
        self.tk_text = self.tk_canvas.create_text(self.vortex[0]+int(self.size*1.1),self.vortex[1],fill='green')
        print(self.tk_text)
    
    def __update_artificial_horizon_tk(self, lines):
            for i in lines:
                index = lines.index(i)
                self.tk_canvas.coords(self.tk_lines[index],i[0][0],i[0][1],i[1][0],i[1][1])
            self.tk_canvas.itemconfigure(self.tk_text, text=str(int(self.meta_angle)))
    
    def __update_artificial_horizon_pygame(self, lines):
        for i in lines:
            self.pygame.draw.line(self.pygame_display, 'green', i[0], i[1], 1)
        self.pygame.display.flip()
    
    def update(self, angle_value=None):
        if angle_value: self.set_angle(angle_value)
        self.meta_angle += (self.angle - self.meta_angle)*0.9
        lines = self.get_lines()
        if self.tk_canvas: self.__update_artificial_horizon_tk(lines)
        if self.pygame_display: self.__update_artificial_horizon_pygame(lines)
        return lines
