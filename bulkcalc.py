import json
from statistics import mode
import os

MODDIR = os.path.join(os.path.dirname(__file__))
MODDIR = MODDIR.replace('./', '')
print(MODDIR)
if len(MODDIR) < 1:
    MODDIR = "."
confPATH = str(MODDIR) + "/Configuration/config.json"
aliasesPATH = str(MODDIR) + "/Configuration/aliases.json"
presetsPATH = str(MODDIR) + "/Configuration/presets.json"
print("Welcome to the bulk calculator.",
      "\nType -h for a list of commands or immediately enter a number to start calculating.")
# Loading defaults
ajson = open(aliasesPATH, "r")
aliases = json.load(ajson)
djson = open(confPATH, "r")
defaults = json.load(djson)
for i in aliases["toggles"]:
    i = i.strip("-")
    globals()["%s_enable" % i] = defaults["bulkcalcdefs"][i]
breakcode = int("0")
currentindex = int("1")
nums_sum = float("0")
nums_multiply = float("1")
nums_subtract = float("0")
nums_mode = float()
nums_listinputs = []
commandaliases = list(aliases)
commandlist = []
for i in commandaliases:
    commandlist.append(aliases[i])
commandlist = tuple(commandlist)
# Defining functions


def parseinput(input):
    global nums_mode, nums_sum, nums_subtract, nums_avg, nums_multiply, currentindex, cmdin, handlecommand
    args = list(input.strip().split(" "))
    argsin = []
    argsin += args
    for i in args:
        try:
            inputfloat = float(i)
            nums_sum += inputfloat
            nums_avg = float(nums_sum / currentindex)
            nums_multiply = nums_multiply * inputfloat
            nums_subtract = nums_subtract - inputfloat
            nums_listinputs.append(inputfloat)
            nums_mode = mode(nums_listinputs)
            currentindex += 1
            argsin.remove(i)
        except ValueError:
            pass
    cmdin = argsin
    while len(cmdin) > 0:
        command = cmdin[0]
        handlecommand(command)
        

def finalize():
    finalizestring = str()
    presetjson = open(presetsPATH, "r")
    pjson = json.load(presetjson)
    for c in commandlist[1]:
        c = c.strip("-")
        if globals()['%s_enable' % c]:
            finalizestring += str(pjson[c]) + str(globals()['nums_%s' % c])
    if len(finalizestring) < 2:
        finalizestring = "\n---Done---\n" "There was nothing to process. "
        "Please pass a valid action as a command to process entered numbers." "\nRestart the program."
    else:
        finalizestring = "\n---Done---" + finalizestring
    presetjson.close()
    print(finalizestring)


def getordinal(number):
    number = int(number)
    if len(str(number)) >= 1:
        if int(str(repr(number)[-1])) == 1:
            numsuffix = str("st")
        elif int(str(repr(number)[-1])) == 2:
            numsuffix = str("nd")
        elif int(str(repr(number)[-1])) == 3:
            numsuffix = str("rd")
        else:
            numsuffix = str("th")
    if len(str(number)) >= 2:
        if int(str(repr(number)[-2] + repr(number)[-1])) in (11, 12, 13):
            numsuffix = str("th")
    return numsuffix


def handlecommand(cmd):
    global cmdin
    global commandlist
    global currentindex
    global breakcode
    # Check if command is a toggleable option
    if cmd in commandlist[1]:
        option = cmd.strip("-")
        if globals()['%s_enable' % option]:
            print(str(option).upper(), "is now toggled off.")
            globals()['%s_enable' % option] = False
        else:
            print(str(option).upper(), "is now toggled on.")
            globals()['%s_enable' % option] = True
    # Other commands
    # Help command
    elif cmd in commandlist[0]:
        try:
            args = cmdin[1]
            hcmd = args
            if len(args) == 1:
                hcmd = str("-" + hcmd)
            elif (len(args) > 2) & (not args[:2] == "--"):
                if args[:1] == '-':
                    hcmd = str("-" + hcmd)
                else:
                    hcmd = str("--" + hcmd)
            if hcmd in commandlist[0]:
                print("Usage: --help [command]. Gives a list of commands when [command] is not provided. "
                      "Please do not type [ ] around the command you want to get info for. ")
            elif hcmd in commandlist[1]:
                print("This is a toggle-able command. If you toggle it, it temporarily changes (gets enabled/ disabled)"
                      ". To set it to be on/ off by default, type in -h --configure")
                if hcmd == "--sum":
                    print("Toggles 'SUM' on/ off. When on, the bulkcalculator outputs the sum of all numbers you "
                          "inputted when you finish inputting.")
                if hcmd == "--subtract":
                    print("Toggles 'SUBTRACT' on/ off. When on, the bulkcalculator outputs the total of "
                          "each number being subtracted from the number before it.")
            else:
                print("Unknown command. For a list of commands, only type in -h")
            cmdin.pop(1)
        except:
            print("Here's a list of all the options you can input as commands ([optional], <mandatory>):")
            print("-h [command] (prints this menu | gives more information about a command - example: -h avg)"
                  "\n--configure (setup the defaults)"
                  "\n--defaults (lists the defaults)"
                  "\nTemporary (toggle) Commands:"
                  "\n--subtract (subtracts each number from the number before it)"
                  "\n--sum (adds all numbers)"
                  "\n--multiply (multiplies all numbers)"
                  "\n--avg (calculates the average of all numbers)"
                  "\n--mode (gives the modal number - if more than one number have the highest frequency, "
                  "it'll output the first you inputted of those."
                  "\nMiscellaneous commands:"
                  "\n--quit (terminates the script, no output)"
                  "\n--end (ends the script, giving an output)")
    # Exit command
    elif cmd in commandlist[2]:
        print("Terminating program.")
        quit()
    # End command
    elif (cmd in commandlist[3]) | (cmd.strip("") == ""):
        if currentindex > 1:
            if currentindex == 2:
                print("Processing 1 number..")
            elif currentindex > 2:
                print("Processing %s numbers.." % int(currentindex - 1))
            breakcode = -1
        elif currentindex == 1:
            print("To quit the application, type -q\nType in at least one number or a command. "
                  "For a list of commands, type in -h.")
    # Configure command
    elif cmd in commandlist[4]:
        # I skidded argslength from someone on stackoverflow
        try:
            argslength = [n for n, l in enumerate(cmdin[1:]) if l.startswith('-')][0]
            print(argslength)
        except:
            argslength = len(cmdin[1:])
        if argslength == 0:
            print("Nothing to configure.")
        else:
            for i in range(argslength):
                if (cmdin[1].endswith("=True")) | (cmdin[1].endswith("=False")):
                    opt = str((cmdin[1]).replace("=True", "").replace("=False", ""))
                    if str("--" + opt) in commandlist[1]:
                        cjson = open(confPATH, "w")
                        if cmdin[1].endswith("=True"):
                            print("Set " + opt + " to ON by default. This change has been immediately implemented, you can temporarily reverse it by entering --" + opt)
                            defaults["bulkcalcdefs"][opt] = True
                            json.dump(defaults, cjson)
                            cjson.close()
                        else:
                            print("Set " + opt + " to OFF by default. This change has been immediately implemented, you can temporarily reverse it by entering --" + opt)
                            defaults["bulkcalcdefs"][opt] = False
                            json.dump(defaults, cjson)
                            cjson.close()
                    else:
                        print("Unknown option: " + opt)
                    cmdin.pop(1)
        for i in aliases["toggles"]:
            i = i.strip("-")
            globals()["%s_enable" % i] = defaults["bulkcalcdefs"][i]
    # List defaults command
    elif cmd in commandlist[5]:
        for i in defaults["bulkcalcdefs"]:
            print(i + " - on by default: " + str(defaults["bulkcalcdefs"][i]))
    elif not(cmd in commandlist):
        print("Unrecognized input, please try again")
    cmdin.remove(cmd)


while breakcode != -1:
    if currentindex == 1:
        fullprompt = str("Enter the first number or type a command (Enter to proceed): ")
    elif currentindex > 1:
        fullprompt = str("Enter the " + str(currentindex) + str(getordinal(currentindex)) + " number (Enter to proceed or finish): ")
    inputToStr = str(input(fullprompt))
    parseinput(inputToStr)
finalize()


# Goals and additional options:
# Round to (dp, sf, nInt)
# Random roll through numbers
# Mean, median, frequency, range
# Frequency range
# Frequency limit: number of entries (descending or ascending)
# Frequency sort
# Show list of numbers you just entered
# "\n--alias <command> (lists the command's aliases)")
#                ['--defaults', '--list-defaults', '--show-defaults', '--defs'],
#               '--mean', '--median', '--range', '--limit-freq', '--freq-show', '--freq-from-to',
#               '--configure', '--defaults')