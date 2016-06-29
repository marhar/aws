# aws

AWS Tools
========

Here's a couple of things I've written to manage AWS deployments.

AWS Shell
---------

The AWS Shell honors the standard AWS profiles.  You can specify which profile on the command line.  The command prompt shows the current profile and region.

Its main advantage over the standard aws program is that it does wildcards and tab completion.  It's also a good (imho) example of boto application programming.

```
--------------------------------------------------
| Welcome to awsh, the AWS shell                 |
| docs: https://github.com/marhar/aws            |
| type "help" for help                  build<6> |
--------------------------------------------------
mhmathadm@us-west-2> help
  ec2:
        instances : print information about instances
           launch : launch an instance
     reservations : display reservations
            start : start one or more instances
             stop : stop one or more instances
          volumes : print information about volumes
  elb:
    loadbalancers : list load balancers
  sqs:
            queue : queue commands
           queues : list queues
  devops:
           config : print information about this profile
          console : open an AWS web console
             curl : curl commands for testing running nodes
             myip : what's my ip address according to amazon?
              ssh : open ssh sessions in tabs
             ssh0 : show ssh commands for running nodes
  awsh:
             help : print help information
             quit : quit the program
            shell : invoke a shell command
  devel:
             div0 : divide by zero, test case for runtime error reporting
```

Instance Watcher
----------------

Dynamically refreshing full-screen status.  The profile can be specified.

```
ec2: (mhmathadm) Wed Sep 23 21:20:17 2015                            build<6>
        id Name          addr     type       zone   state
i-d3464216  adm  52.89.219.53 t2.micro us-west-2b running
i-60a2e6a6 www1 52.24.245.202 t2.micro us-west-2a running
i-c0357606 www2          None t2.micro us-west-2a stopped

elb:
mhmath
    mhmath-1305260662.us-west-2.elb.amazonaws.com
        i-60a2e6a6 : InService (N/A)
        i-c0357606 : OutOfService (Instance)
```

Building on Mac
===============

Because of some GPL restrictions, the system Mac Python doesn't have
a good readline package.

Here's how to build a Mac Python 2.7 base.

```
# make work area
mkdir ~/py
mkdir ~/py/dist
mkdir ~/py/src

# download these to ~/py/dist.  note versions may drift
https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz
https://bootstrap.pypa.io/get-pip.py
http://ftp.gnu.org/gnu/readline/readline-6.3.tar.gz

# unpack
cd ~/py/src
tar xzf ../dist/Python-2.7.11.tgz
tar xzf ../dist/readline-6.3.tar.gz

# build and install readline
cd ~/py/src/readline-6.3
./configure --prefix=$HOME/py
make -j8 install

# build and install Python (it will detect installed readline)
cd ~/py/src/Python-2.7.11
./configure --prefix=$HOME/py
make -j8 install

# install pip
~/py/bin/python ~/py/dist/get-pip.py

# install boto package
~/py/bin/pip install boto

# test awsh
~/py/bin/python awsh
--------------------------------------------------
| Welcome to awsh, the AWS shell                 |
| docs: https://github.com/marhar/aws            |
| type "help" for help                  build<6> |
--------------------------------------------------
```
