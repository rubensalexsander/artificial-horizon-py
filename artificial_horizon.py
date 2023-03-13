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

def get_c(angle, a):
    return (sin(angle)/cos(angle))*a

class ArtificialHorizon:
    def __init__(self, vortex, size, angle_x=0, angle_y=0, angle_z=0, tk_canvas=None, pygame_display=None):
        self.vortex = vortex
        self.size = size
        
        self.meta_angle_x = angle_x
        self.meta_angle_y = angle_y
        self.meta_angle_z = angle_z
        self.set_angle(x=angle_x,y=angle_y,z=angle_z)
        
        self.tk_canvas = tk_canvas
        self.pygame_display = pygame_display
        
        if tk_canvas:
            self.__create_tk_lines()
        if self.pygame_display:
            import pygame
            self.pygame = pygame
        
    def set_angle(self, x=None,y=None,z=None):
        if not x==None: self.angle_x = x
        if not y==None: self.angle_y = y
        if not z==None: self.angle_z = z
    
    def get_lines(self):
        space_size = int(self.size/5) #Tamanho do espaço do horizonte artificial
        space_plane = int(self.size/20) #Tamanho do avião do centro
        size_wigs = int(self.size/10) #Tamanho das asas laterais
        
        vertical_vortex = [self.vortex[0], self.vortex[1]+get_c(graus_to_radius(self.angle_x), self.size)] #Vortex com alteração vertical (no eixo x)
        
        lines = []
        
        # Linhas principais
        lines.append([get_p(graus_to_radius(self.meta_angle_y-90), vertical_vortex, space_size), get_p(graus_to_radius(self.meta_angle_y-90), vertical_vortex, self.size)])
        lines.append([get_p(graus_to_radius(self.meta_angle_y-270), vertical_vortex, space_size), get_p(graus_to_radius(self.meta_angle_y-270), vertical_vortex, self.size)])
        # Wigs
        lines.append([get_p(graus_to_radius(self.meta_angle_y-90), vertical_vortex, self.size), get_p(graus_to_radius(self.meta_angle_y), get_p(graus_to_radius(self.meta_angle_y-90), vertical_vortex, self.size), size_wigs)])
        lines.append([get_p(graus_to_radius(self.meta_angle_y-270), vertical_vortex, self.size), get_p(graus_to_radius(self.meta_angle_y), get_p(graus_to_radius(self.meta_angle_y-270), vertical_vortex, self.size), size_wigs)])
        # Center Cross
        lines.append([[self.vortex[0],self.vortex[1]-space_plane], [self.vortex[0],self.vortex[1]-space_size+8]])
        lines.append([[self.vortex[0]-space_plane,self.vortex[1]], [self.vortex[0]-space_size+8,self.vortex[1]]])
        lines.append([[self.vortex[0]+space_plane,self.vortex[1]], [self.vortex[0]+space_size-8,self.vortex[1]]])
        lines.append([[self.vortex[0]-space_plane,self.vortex[1]], [self.vortex[0],self.vortex[1]+space_plane]])
        lines.append([[self.vortex[0]+space_plane,self.vortex[1]], [self.vortex[0],self.vortex[1]+space_plane]])
        
        return lines

    def __create_tk_lines(self):
        self.tk_lines = [self.tk_canvas.create_line(0,0,0,0,fill='green') for i in range(len(self.get_lines()))]
        self.tk_text_angle_x = self.tk_canvas.create_text(self.vortex[0],self.vortex[1]+int(self.size*1.1),fill='green')
        self.tk_text_angle_y = self.tk_canvas.create_text(self.vortex[0]+int(self.size*1.1),self.vortex[1],fill='green')
    
    def __update_artificial_horizon_tk(self, lines):
            for i in lines:
                index = lines.index(i)
                self.tk_canvas.coords(self.tk_lines[index],i[0][0],i[0][1],i[1][0],i[1][1])
            self.tk_canvas.itemconfigure(self.tk_text_angle_x, text=str(int(self.meta_angle_x))+'°')
            self.tk_canvas.itemconfigure(self.tk_text_angle_y, text=str(int(self.meta_angle_y))+'°')
    
    def __update_artificial_horizon_pygame(self, lines):
        for i in lines:
            self.pygame.draw.line(self.pygame_display, 'green', i[0], i[1], 1)
        self.pygame.display.flip()
    
    def update(self, x=None,y=None,z=None):
        #if angle_value: self.set_angle(angle_value)
        self.meta_angle_x += (self.angle_x - self.meta_angle_x)*0.8
        self.meta_angle_y += (self.angle_y - self.meta_angle_y)*0.8
        self.meta_angle_z += (self.angle_z - self.meta_angle_z)*0.8
        lines = self.get_lines()
        if self.tk_canvas: self.__update_artificial_horizon_tk(lines)
        if self.pygame_display: self.__update_artificial_horizon_pygame(lines)
        return lines
