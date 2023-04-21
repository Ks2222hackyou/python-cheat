import glfw
import win32gui
import OpenGL.GL as gl
import win32con
from random import randint, choice
import pymem
import struct, keyboard
from off.offsets import *
pm = pymem.Pymem('csgo.exe')
client = pymem.pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
dwForceJump = 0x52BBD48
dwLocalPlayer = 0xDEA964
dwEntityList = 0x4DFFFB4
dwGlowObjectManager = 0x535AA70
m_iGlowIndex = 0x10488
dwForceAttack = 0x322DDEC
m_iCrosshairId = 0x11838
m_iTeamNum = 0xF4
m_flFlashMaxAlpha = 0x1046C
m_iDefaultFOV = 0x333C
m_iHealth = 0x100
m_vecOrigin = 0x138
dwViewMatrix = 0x4DF0DE4
m_fFlags = 0x104
# Offsets Update offsets with https://github.com/frk1/hazedumper/blob/master/csgo.hpp

class Vector2:
    def __init__(self, _x,_y) -> None:
        self.x = _x
        self.y = _y
 
class Vector3:
    def __init__(self, _x,_y,_z) -> None:
        self.x = _x
        self.y = _y
        self.z = _z
 
screenSize = Vector2(2560,1440)
 
class hack:
 
    def __init__(self) -> None:
        self.pm = pymem.Pymem('csgo.exe')
        self.client = pymem.pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
 
    def local_player(self):
        return self.pm.read_int(self.client + dwLocalPlayer)
    
    def entity_health(self, entity):
        return self.pm.read_int(entity + m_iHealth)
    
    def entity_team(self, entity):
        return self.pm.read_int(entity + m_iTeamNum)
    
    def entity_position(self, entity):
        position_in_bytes = self.pm.read_bytes(entity + m_vecOrigin, 12)
        pos = struct.unpack("fff", position_in_bytes)
        return Vector3(pos[0], pos[1], pos[2])

    def world_to_screen(self, position: Vector3, matrix):
        x_ = position.x * matrix[0] + position.y * matrix[1] + position.z * matrix[2] + matrix[3]
        y_ = position.x * matrix[4] + position.y * matrix[5] + position.z * matrix[6] + matrix[7]
        z = position.x * matrix[12] + position.y * matrix[13] + position.z * matrix[14] + matrix[15]

    
        if z < 0.01:
            return None
    
        pos_vec = Vector3(0, 0, 0)
        pos_vec.z = z
    
        x_ *= 1.0 / pos_vec.z
        y_ *= 1.0 / pos_vec.z
    
        pos_vec.x = screenSize.x / 2
        pos_vec.y = screenSize.y / 2
    
        pos_vec.x += 0.5 * x_ * screenSize.x + 0.5
        pos_vec.y -= 0.5 * y_ * screenSize.y + 0.5
 
        return pos_vec
 
glfw.init()
glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, True)
glfw.window_hint(glfw.FLOATING, True)
glfw.window_hint(glfw.DECORATED, False) # make sure to set to false
 
window = glfw.create_window(2560, 1440, 'Box Esp', None , None)
glfw.make_context_current(window)
gl.glOrtho(0, screenSize.x, 0, screenSize.y, -1, 1)
 
handle = win32gui.FindWindow(0, 'Box Esp')
 
exStyle = win32gui.GetWindowLong(handle, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(handle, win32con.GWL_EXSTYLE, exStyle | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
 
entity = hack()
colors = [(255,0,0),(0,255,0),(0,0,255)]
color = (choice(colors))

def main():
    while True:
        glfw.swap_buffers(window)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        glfw.poll_events()
        
        if keyboard.is_pressed('end'): exit(0)
    

    
        View_Matrix_Bytes = entity.pm.read_bytes(entity.client + dwViewMatrix, 64)
        View_Matrix = struct.unpack('ffffffffffffffff', View_Matrix_Bytes)

        for x in range(32):
            Entity = entity.pm.read_int(entity.client + dwEntityList + x * 0x10)
            if not Entity:
                continue
    
            Entity_Health = entity.entity_health(Entity) / 100

            
            if Entity_Health <= 0:
                continue
    
            Entity_Pos = entity.entity_position(Entity)
            Entity_Pos.z += 35
            Entity_2d_Position = entity.world_to_screen(Entity_Pos, View_Matrix)
            if not Entity_2d_Position:
                continue
    
            if Entity_2d_Position.x <= 0 or Entity_2d_Position.x > screenSize.x:
                continue
            if Entity_2d_Position.y <= 0 or Entity_2d_Position.y > screenSize.y:
                continue
        
            
            
            gl.glLineWidth(2)
            
            gl.glBegin(gl.GL_LINES)

            color1 = (100,100,100)
            gl.glColor3b(*color1)

        
            

            
            gl.glVertex2d(Entity_2d_Position.x - 20, (screenSize.y -  Entity_2d_Position.y)- 30)
            gl.glVertex2d(Entity_2d_Position.x + 20, (screenSize.y -  Entity_2d_Position.y)- 30)
            gl.glVertex2d(Entity_2d_Position.x - 20, (screenSize.y -  Entity_2d_Position.y)- 30)
            gl.glVertex2d(Entity_2d_Position.x - 20, (screenSize.y -  Entity_2d_Position.y) + 30)
            gl.glVertex2d(Entity_2d_Position.x - 20, (screenSize.y -  Entity_2d_Position.y)+ 30)
            gl.glVertex2d(Entity_2d_Position.x + 20, (screenSize.y -  Entity_2d_Position.y)+ 30)
            gl.glVertex2d(Entity_2d_Position.x + 20, (screenSize.y -  Entity_2d_Position.y)- 30)
            gl.glVertex2d(Entity_2d_Position.x + 20, (screenSize.y -  Entity_2d_Position.y) + 30)
            


            
            
            gl.glEnd()

            

main()


