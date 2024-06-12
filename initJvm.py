
from jpype import *
import os
INIT_JVM = None
if not INIT_JVM:
    jarLocation = os.path.join(os.getcwd(), "infodynamics.jar");
    if (not(os.path.isfile(jarLocation))):
        exit("infodynamics.jar not found (expected at " + os.path.abspath(jarLocation) + ") - are you running from demos/python?")
    # Start the JVM (add the "-Xmx" option with say 1024M if you get crashes due to not enough memory space)
    startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=" + jarLocation)
    INIT_JVM = True