
from QtLive.devBox import *
from QtLive.embedded_IPython import *

from vmpw.vmpwMidiPort import vmpwMidiWidget

#Import the context
from vmpw.vmpwGLViewport import dgl

from qt_material import QtStyleTools, apply_stylesheet

@liveEditorFactory(name="VMPW Development",rootCons=rootCons)
class vmpw_app(QMainWindow,QtStyleTools):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(QSplitter())

        #example patch
        midiW=self.midiWidget=vmpwMidiWidget()
        self.layout().addWidget(midiW)
        midiW.show()

        self.show()

the_vmpw=vmpw_app(rootCons=rootCons);the_vmpw.show()

if(__name__ == '__interpreter__' ):
    apply_stylesheet(app,'light_blue.xml')

def vmpw_main():

    global globalTest
    globalTest=20
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app  = QApplication([])
    
    startScript = None
    if (len(sys.argv) > 1 ):
        startScript = sys.argv[1] 
    widget = LiveConsole(workFile=startScript)
    widget.show()
    
    app.exec_()    

if __name__ == '__main__':
    vmpw_main()