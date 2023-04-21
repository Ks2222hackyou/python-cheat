import os, time
from DrawEsp.off.offsets import *
try:
    import dearpygui.dearpygui as gui; import pymem, threading, keyboard, winsound, time, OpenGL, glfw, win32gui, win32api, struct
except:
    print('Error: libraries are not downloaded')
    time.sleep(2)
    print('downloading')
    time.sleep(1)
    os.system('pip install dearpygui')
    os.system('pip install Pymem')
    os.system('pip install keyboard')
    os.system('pip install pywin32')
    os.system('pip install glfw')
    os.system('pip install PyOpenGL')
    print()
    print('---------------')
    print('-restart cheat-')
    print('---------------')   
    time.sleep(3)
    exit()



pm = pymem.Pymem('csgo.exe')
client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
color_list = ['green','blue','red','cyan','white','yellow','pink']


path = os.getcwd()
print(path)
path2s =os.path.join(path, "sounds")
sounds = os.listdir(path2s)

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





def soundtest():


    sound = gui.get_value('snd')
    winsound.PlaySound(f'sounds\{sound}',0 )

def glow():
            if gui.get_value('gl'):
                color = gui.get_value('col')
                if color == 1 or color == 'green':
                
                    
                    try:
                        glow = pm.read_int(client + dwGlowObjectManager)
                        for i in range(0,32):

                            entity = pm.read_int(client + dwEntityList + i *0x10)
                            if entity:
                                entityglowing = pm.read_int(entity+m_iGlowIndex)
                                pm.write_float(glow + entityglowing * 0x38 + 0x8, float(0))
                                pm.write_float(glow + entityglowing * 0x38 + 0xC, float(1))   
                                pm.write_float(glow + entityglowing * 0x38 + 0x10, float(0))    
                                pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))    
                                pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)
                    except:
                        print("restart cheats")
                elif color == 2 or color == 'blue':
                    try:
                        glow = pm.read_int(client + dwGlowObjectManager)
                        for i in range(0,32):
                            entity = pm.read_int(client + dwEntityList + i *0x10)
                            if entity:
                                entityglowing = pm.read_int(entity+m_iGlowIndex)
                                pm.write_float(glow + entityglowing * 0x38 + 0x8, float(0))
                                pm.write_float(glow + entityglowing * 0x38 + 0xC, float(0))   
                                pm.write_float(glow + entityglowing * 0x38 + 0x10, float(1))    
                                pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))    
                                pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)
                    except:
                        print("restart cheats")
                elif color == 3 or color == 'red':
                    try:
                        glow = pm.read_int(client + dwGlowObjectManager)
                        for i in range(0,32):
                            entity = pm.read_int(client + dwEntityList + i *0x10)
                            if entity:
                                entityglowing = pm.read_int(entity+m_iGlowIndex)
                                pm.write_float(glow + entityglowing * 0x38 + 0x8, float(1))
                                pm.write_float(glow + entityglowing * 0x38 + 0xC, float(0))   
                                pm.write_float(glow + entityglowing * 0x38 + 0x10, float(0))    
                                pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))    
                                pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)
                    except:
                        print("restart cheats")    
                elif color == 4 or color == 'cyan':
                    try:
                        glow = pm.read_int(client + dwGlowObjectManager)
                        for i in range(0,32):
                            entity = pm.read_int(client + dwEntityList + i *0x10)
                            if entity:
                                entityglowing = pm.read_int(entity+m_iGlowIndex)
                                pm.write_float(glow + entityglowing * 0x38 + 0x8, float(0))
                                pm.write_float(glow + entityglowing * 0x38 + 0xC, float(1))   
                                pm.write_float(glow + entityglowing * 0x38 + 0x10, float(1))    
                                pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))    
                                pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)
                    except:
                        print("restart cheats")    
                elif color == 5 or color == 'white':
                    try:
                        glow = pm.read_int(client + dwGlowObjectManager)
                        for i in range(0,32):
                            entity = pm.read_int(client + dwEntityList + i *0x10)
                            if entity:
                                entityglowing = pm.read_int(entity+m_iGlowIndex)
                                pm.write_float(glow + entityglowing * 0x38 + 0x8, float(1))
                                pm.write_float(glow + entityglowing * 0x38 + 0xC, float(1))   
                                pm.write_float(glow + entityglowing * 0x38 + 0x10, float(1))    
                                pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))    
                                pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)
                    except:
                        print("restart cheats")    
                elif color == 6 or color == 'yellow':
                    try:
                        glow = pm.read_int(client + dwGlowObjectManager)
                        for i in range(0,32):
                            entity = pm.read_int(client + dwEntityList + i *0x10)
                            if entity:
                                entityglowing = pm.read_int(entity+m_iGlowIndex)
                                pm.write_float(glow + entityglowing * 0x38 + 0x8, float(1))
                                pm.write_float(glow + entityglowing * 0x38 + 0xC, float(1))   
                                pm.write_float(glow + entityglowing * 0x38 + 0x10, float(0))
                                pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))    
                                pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)
                    except:
                        print("restart cheats")    
                elif color == 7 or color == 'pink':
                    try:
                    
                        glow = pm.read_int(client + dwGlowObjectManager)
                        for i in range(0,32):
                            entity = pm.read_int(client + dwEntityList + i *0x10)
                            if entity:
                                entityglowing = pm.read_int(entity+m_iGlowIndex)
                                pm.write_float(glow + entityglowing * 0x38 + 0x8, float(1))
                                pm.write_float(glow + entityglowing * 0x38 + 0xC, float(0)) 
                                pm.write_float(glow + entityglowing * 0x38 + 0x10, float(1))    
                                pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))    
                                pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)
                    except:
                        print("restart cheats")


def Triggerbot():
    try:  
        if gui.get_value('Triggerbots'):
            localplayer = pm.read_uint(client + dwLocalPlayer)
            if not localplayer: return
            if pm.read_uint(localplayer + m_iHealth) <= 0: return
            crosshair = pm.read_uint(localplayer + m_iCrosshairId)
            localteam = pm.read_uint(localplayer + m_iTeamNum)
            entteam = pm.read_uint(client + dwEntityList + (crosshair -1)* 0x10)
            crosshairtm = pm.read_uint(entteam + m_iTeamNum)
            if localteam == crosshairtm: return
            if gui.get_value('onk') == True:
                if crosshair >= 1 and crosshair <=32 and keyboard.is_pressed(gui.get_value('sss')) and localteam != crosshairtm:  
                    time.sleep(gui.get_value('dl'))
                    pm.write_int(client + dwForceAttack, 6)      
            else:
                if crosshair >= 1 and crosshair <=32:  
                    time.sleep(gui.get_value('dl'))
                    pm.write_int(client + dwForceAttack, 6)
   
    
    
    
    except:
        None
def fov():
    player = pm.read_uint(client + dwLocalPlayer)
    pm.write_int(player + m_iDefaultFOV, gui.get_value('Fovval'))

def bhop():
    if gui.get_value('bh'):
        plr =pm.read_uint(client + dwLocalPlayer)
        if keyboard.is_pressed('space'):
            if pm.read_int(plr + m_fFlags) == 257:             
                pm.write_int((client + dwForceJump), 6)
            elif pm.read_int(plr + m_fFlags) == 256:
                pm.write_int((client + dwForceJump), 4)

def flash():
    if gui.get_value('flash'):
        plr3 = pm.read_int(client + dwLocalPlayer)
        flash_value = plr3 + m_flFlashMaxAlpha
        pm.write_float(flash_value, float(0))

def hitsounds():
    try:  
        if gui.get_value('hit'):
            sound = gui.get_value('snd')
            localplayer = pm.read_uint(client + dwLocalPlayer)
            crosshair = pm.read_uint(localplayer + m_iCrosshairId)
            hits = pm.read_int(client + dwForceAttack)
            if crosshair >= 1 and crosshair <=32 and hits >=5:
                winsound.PlaySound(f'sounds/{sound}',0)
    except:
        None              






def tracers():

        os.system('start DrawEsp/Tracers.py')

        
            

def box():

        os.system('start DrawEsp/BoxEsp.py')


def hp():

    os.system('start DrawEsp/Hp.py')



def Thread():
    while True:
        Triggerbot()
        fov()
        glow()
        bhop()
        flash()
        hitsounds()










    


gui.create_context()
gui.create_viewport(title='SussyCheats Dev Beta V3.01', width=350, height=300, max_height=250, max_width=350, min_height=300, min_width=350)
gui.setup_dearpygui()
gui.set_viewport_always_top(True)


with gui.window(label='Sus', width=350,height=300,no_title_bar=True,no_resize=True, no_move=True, show=True):
    with gui.tab_bar(label='Cheat'):
        
        
        with gui.tab(label='Combat'):
            gui.add_checkbox(label='Triggerbot', tag= 'Triggerbots')
            gui.add_slider_float(label='Deley', tag='dl',default_value=0.001, min_value=0.001, max_value=0.05)
            gui.add_checkbox(label='Triggerbot On Key', tag='onk')
            gui.add_input_text(label='triggerButton', tag= 'sss')

        
       
        with gui.tab(label='Visual'):
            gui.add_slider_int(label='Fov', tag='Fovval',default_value=100,min_value=90,max_value=140)
            gui.add_checkbox(label='GlowEsp',tag='gl')
            gui.add_listbox(label='GlowColors',tag='col',items=color_list)
            gui.add_checkbox(label='NoFalsh', tag='flash')
            gui.add_button(label='Render Tracers',callback=tracers),gui.add_button(label='Render Hp Bar',callback=hp),gui.add_button(label='Render BoxEsp',callback=box)
            gui.add_button(label="""Press "End" key to kill all renders""")

    
        with gui.tab(label='Movement'):
            gui.add_checkbox(label='Bhop', tag='bh')
        
        
        with gui.tab(label='Other'):
            gui.add_checkbox(label='HitSounds',tag='hit')
            gui.add_listbox(label='HitSound',tag='snd', items=sounds)
            gui.add_button(label='Test Sound', callback=soundtest)





gui.show_viewport()
threading.Thread(target=Thread).start()
gui.start_dearpygui()
gui.destroy_context()