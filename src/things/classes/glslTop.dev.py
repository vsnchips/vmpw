import vmpw.vmpwGLViewport as *
import vmpw.vmpwGLViewport
vgl = vmpw.vmpwGLViewport.vmpwGLFrameViewer()
vgl.show()
import time
devgl = liveDevify(vgl,self.ipyConsole)
print(devgl)

def init(state,eID=-1,glslFile=None):
    global ECSdata
    if (glslFile is None):
        raise FileNotFoundError
    state.entityID=eID
    
    ECSdata['shaders']['glslFile'] = vsnshader.fileShader(glslFile)

import vsnchips_gl.vsnchips_shader as vsnshader
def paint(state):
    global uniforms
    global shaders