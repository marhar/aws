#!/usr/local/sqlminus/bin/python
"""
awshelpers -- some handy aws and print routines

    https://github.com/awsh             :  share and enjoy!
    Mark Harrison, marhar@gmail.com     :
"""

import os,sys,ConfigParser,subprocess

#-----------------------------------------------------------------------
def readconfig(fn):
    """read the aws config file"""

    p=os.path.join(os.getenv('HOME'),'.aws',fn)

    config = ConfigParser.ConfigParser()
    config.read(p)

    config_dict = {}
    for section in config.sections():
        config_dict[section] = dict(config.items(section))
    return config_dict

#-----------------------------------------------------------------------
def P(s):
    """print and flush, with newline"""
    P0(str(s)+'\n')

#-----------------------------------------------------------------------
def P0(s):
    """print and flush, no newline"""
    sys.stdout.write(str(s))
    sys.stdout.flush()

#-----------------------------------------------------------------------
dbgfd=None
def D0(s):
    """debug output, no newline"""
    global dbgfd
    if dbgfd is None:
        dbgfd=open('/tmp/awsh.dbg','a')
        D('================================================== DBGFD')
    dbgfd.write(str(s))
    dbgfd.flush()

#-----------------------------------------------------------------------
def D(s):
    """debug output with newline."""
    D0(str(s)+'\n')

#-----------------------------------------------------------------------
print_is_quiet = False
def V0(s):
    """verbose print and flush, no newline. --quiet to supress"""
    if print_is_quiet is False:
        sys.stdout.write(str(s))
        sys.stdout.flush()

#-----------------------------------------------------------------------
def V(s):
    """verbose print and flush, with newline. --quiet to supress"""
    V0(str(s)+'\n')

#-------------------------------------------------------------------
def tprint(headers,rows):
    """nicely print a result set"""
    headerlen=len(headers)
    maxlen=[len(str(i)) for i in headers]
    for r in rows:
        if len(r) != headerlen:
            raise WrongColumns
        for i in range(len(headers)):
            ts=str(r[i])
            tmpl=len(ts)
            if maxlen[i]<tmpl:
                maxlen[i]=tmpl

    fmt='%%%ds'%(maxlen[0])
    for i in maxlen[1:]:
        fmt+=' | %%%ds'%(i)

    fmt='%%%ds'%(maxlen[0])
    for i in maxlen[1:]:
        fmt+=' %%%ds'%(i)

    P(fmt%tuple(headers))
    for r in rows:
        P(fmt%tuple(r))

#-------------------------------------------------------------------
_ho='\033[H'
_ed='\033[J'
_el='\033[K' 
def tprintx(headers,rows):
    """nicely print a result set"""
    headerlen=len(headers)
    maxlen=[len(str(i)) for i in headers]
    for r in rows:
        if len(r) != headerlen:
            raise WrongColumns
        for i in range(len(headers)):
            ts=str(r[i])
            tmpl=len(ts)
            if maxlen[i]<tmpl:
                maxlen[i]=tmpl

    fmt='%%%ds'%(maxlen[0])
    for i in maxlen[1:]:
        fmt+=' | %%%ds'%(i)

    fmt='%%%ds'%(maxlen[0])
    for i in maxlen[1:]:
        fmt+=' %%%ds'%(i)

    P0(fmt%tuple(headers)+_el+'\n')
    for r in rows:
        P0(fmt%tuple(r)+_el+'\n')
