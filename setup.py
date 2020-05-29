# Hi There!
# This python script is written to
# install some python modules using
# pip. You can go through the code.

import subprocess
import sys
import get_pip


# Installing Function
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


# Installing PyQt5
try:
    print("[GAME] Trying to import PyQt5")
    import PyQt5
except:
    print("[EXCEPTION] PyQt5 not installed")

    try:
        print("[GAME] Trying to install PyQt5 via pip")
        import pip

        install("PyQt5")
        print("[GAME]PyQt5 has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install PyQt5")
            import pip

            install("PyQt5")
            print("[GAME] PyQt5 has been installed")
        except:
            print("[ERROR 1] PyQt5 could not be installed")

# Installing webbrowser
try:
    print("[GAME] Trying to import webbrowser")
    import webbrowser
except:
    print("[EXCEPTION] webbrowser not installed")

    try:
        print("[GAME] Trying to install webbrowser via pip")
        import pip

        install("webbrowser")
        print("[GAME] webbrowser has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install webbrowser")
            import pip

            install("webbrowser")
            print("[GAME] webbrowser has been installed")
        except:
            print("[ERROR 1] webbrowser could not be installed")

# Installing pyttsx3
try:
    print("[GAME] Trying to import pyttsx3")
    import pyttsx3
except:
    print("[EXCEPTION] pyttsx3 not installed")

    try:
        print("[GAME] Trying to install pyttsx3 via pip")
        import pip

        install("pyttsx3")
        print("[GAME] pyttsx3 has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install pyttsx3")
            import pip

            install("pyttsx3")
            print("[GAME] pyttsx3 has been installed")
        except:
            print("[ERROR 1] pyttsx3 could not be installed")
