# aws

AWS Tools
========

Here's a couple of tools I've written to learn about ASW and
make it easier to manage.

AWS Shell
---------

The AWS Shell honors the standard AWS profiles.  You can specify which profile on the command line.  The command prompt shows the current profile and region.

Its main advantage over the standard aws program is that it does wildcards and tab completion.  It's also a good example of boto application programming

    $ ./awsh
    --------------------------------------------------
    | Welcome to awsh, the AWS shell                 |
    | docs: https://github.com/marhar/aws            |
    | type "help" for help                  build<4> |
    --------------------------------------------------
    default@us-west-2> help
    
    Documented commands (type help <topic>):
    ========================================
    EOF     curltest  help       launch  reservations  start  volumes
    config  div0      instances  myip    ssh           stop
 

Instance Status.
   
    default@us-west-2> instances
            id   ip_address instance_type  placement   state
    i-09e9cccc 52.88.208.50      t2.micro us-west-2b running
    i-aa234b6c         None      t2.micro us-west-2a stopped

Instance Control. Wildcards and Tab Completion are supported.

    default@us-west-2> start i-09e9cccc
        starting: Instance:i-09e9cccc

    default@us-west-2> stop *
        stopping: Instance:i-09e9cccc

Troubleshooting.  Conveniently print ssh and curl for all running instances.


    default@us-west-2> ssh
    ssh -i /Users/mh/.aws/default.pem ec2-user@52.88.208.50

    default@us-west-2> curltest
    curl http://52.88.208.50
    curl http://52.88.208.50/cgi-bin/working

Show volume status.

    default@us-west-2> volumes
              id type       zone iops size    status
    vol-939c8c5d  gp2 us-west-2a   24    8    in-use
    vol-2cb91dd8  gp2 us-west-2b    6    2 available
    vol-132484e7  gp2 us-west-2b   24    8    in-use

Instance Watcher
----------------

Dynamically refreshing full-screen status.  The profile can be specified.

    ec2 (default) Sun Sep 13 11:46:07 2015                            build<4>
            id         addr     type       zone   state status alarm
    i-09e9cccc 52.88.208.50 t2.micro us-west-2b running    ___   ___
    i-aa234b6c         None t2.micro us-west-2a stopped    ___   ___
