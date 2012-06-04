# adapted http://www.jython.org/jythonbook/en/1.0/appendixB.html#working-with-classpath 
import java

def addFile(path):
    url = java.io.File(path).toURL()
    addURL = java.net.URLClassLoader.getDeclaredMethod("addURL", java.net.URL)
    addURL.setAccessible(True)
    addURL.invoke(java.lang.ClassLoader.getSystemClassLoader(), url)
    return url

