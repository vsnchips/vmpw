'''
aubio module for vmpw
Created by Dan Aston
github.com/vsnchips
'''

import pysoundcard as pys
from vmpw.vmpwGLViewport import vmpwGLFrameViewer
 
@liveEditorFactory(rootCons=rootCons)
class vmpwAubio(vmpwGLFrameViewer):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.name="vmpwAubio"
        self.setWindowTitle(self.name)
        self.input=pys.InputStream(device=1)
        self.input.start()
        self.show()
    def update(self):
        self.buffer = self.input.read(512)
