
## execute system comand and get output
import os
import subprocess
def pretty_system(cmd):
   p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
   out,err = p.communicate()
   return out


if __name__ == "__main__":
   cmd = 'adb shell "getprop | grep hardwareversion"'
   print ("result:"+pretty_system(cmd))
