#! /bin/bash

exist_netns()
{
    if [ ! $#  -eq 1 ] ; then
        echo 'invalid arguments'
        exit 1
    fi
    for ns in `ip netns`
    do 
        if [ "$ns" == "$1" ] ; then 
            return 0
        fi
    done
    return 1
}

create_netns()
{
    if [ ! $#  -eq 1 ] ; then
        echo 'invalid arguments'
        exit 1
    fi
    exist_netns $1
    if [ ! "$?" -eq 0 ] ; then
       /usr/sbin/ip netns add $1
    else
    #delete all the links in the netns
        for iface in `/usr/sbin/ip netns exec $1 ip li |grep "^[0-9]*: "  |sed 's/^[0-9]*: \(.*:\).*/\1/g' |tr -d ':' |sed 's/@.*//g'`
        do
            /usr/sbin/ip netns exec $1 ip link delete $iface 2> /dev/null
        done
    fi
    
}
delete_netns()
{
    if [ ! $#  -eq 1 ] ; then
        echo 'invalid arguments'
        exit 1
    fi
    exist_netns $1
    if [ "$?" -eq 0 ] ; then
        /usr/sbin/ip netns delete $1
    fi
}
#delete_netns $1
create_netns test1
