

import os, signal, subprocess, sys, tty, termios

sigmap = {
    '\x15': signal.SIGUSR1,     # ctrl-u
    '\x1c': signal.SIGQUIT,     # ctrl-\
    '\x08': signal.SIGHUP,      # ctrl-h
    '\x09': signal.SIGINT,      # ctrl-i
    }
# setup tty
fd = sys.stdin.fileno()
old_tc = termios.tcgetattr(fd)
tty.setraw(fd)
# spawn command as a child proc
cmd = sys.argv[1:]
proc = subprocess.Popen(["python", "PiBoo_gpiozero.py"])
while 1:
    try:
        ch = sys.stdin.read(1)
        # example of ansi escape to move cursor down and to column 0
        print '\033[1Eyou entered', repr(ch)
        if ch == 'q':
            break
        signum = sigmap.get(ch)
        if signum:
            os.kill(proc.pid, signum)
    finally:
        pass
termios.tcsetattr(fd, termios.TCSANOW, old_tc)
sys.exit()