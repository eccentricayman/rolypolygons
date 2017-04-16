#ty @fierydarkwraith for the script :P
import math

with open("script", "w") as fd:

    end = ""
    for i in range(0, 60):
        end += "clear\n"
        end += "sphere\n0 0 0 %s\n"%(240 - (i * 4))
        end += "torus\n0 0 0 %s %s\n"%(240 - (i * 4), i * 4)
        end += "ident\n"
        end += "rotate\n y %f\n"%(i*5)
        end += "rotate\n z %f\n"%(i*5)
        end += "rotate\n x %f\n"%(i*5)
        end += "move\n 250 250 0\n"
        end += "apply\n"
        if i < 10:
            end += "save\n anim/00%d.png\n"%(i)
        else:
            end += "save\n anim/0%d.png\n"%(i)
    print end
    fd.write(end)
