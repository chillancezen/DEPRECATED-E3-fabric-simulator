#! /usr/bin/python
import yaml
import sys
import os
import json
from pyroute2 import NetNS

def load_config_profile(path):
    with open(path,'r') as stream:
        try:
            return yaml.load(stream)
        except:
            print 'errors occur during parsing configuration file,please check it'
            return list()

def _count_key_value_of_obj(cfg,obj,key,value):
    cnt=0
    for item in cfg:
        _obj=item.keys()[0]
        _attr=item[_obj]
        if _obj != obj:
            continue
        if key in _attr and _attr[key] == value:
            cnt = cnt+1
    return cnt

def _validate_vswitch(cfg):
    for item in cfg:
        obj=item.keys()[0]
        if obj !='vswitch':
            continue
        attr=item[obj]
        if 'name' not in attr or 'type' not in attr:
            return False
        if _count_key_value_of_obj(cfg,'vswitch','name',attr['name']) != 1:
            return False 
    return True
def _validate_lan(cfg):
    for item in cfg:
        obj=item.keys()[0]
        if obj !='lan':
            continue
        attr=item[obj]
        if 'name' not in attr:
            return False
        if _count_key_value_of_obj(cfg,'lan','name',attr['name']) != 1:
            return False
    return True
def _validate_iface(cfg):
    for item in cfg:
        obj=item.keys()[0]
        if obj !='iface':
            continue
        attr=item[obj]
        if 'name' not in attr or 'attached_vswitch' not in attr or 'attached_lan' not in attr:
            return False
        if _count_key_value_of_obj(cfg,'iface','name',attr['name']) != 1:
            return False
        if _count_key_value_of_obj(cfg,'vswitch','name',attr['attached_vswitch']) != 1:
            return False
        if _count_key_value_of_obj(cfg,'lan','name',attr['attached_lan']) != 1:
            return False
    return True
    
def validate_config(cfg):
    return _validate_vswitch(cfg) and _validate_lan(cfg) and _validate_iface(cfg)

def create_vswitch(vs):
    attr=vs['vswitch']
    ns=NetNS(attr['name'])
    #clean the links in the namespace
    links=ns.get_links()
    for link in links:
        try:
            ns.link_remove(link['index'])
        except:
            pass
    print len(links)
if __name__ == '__main__':
    cfg=load_config_profile('./sample.yaml')
    #print _validate_vswitch(cfg)
    #print _validate_lan(cfg)
    #print _validate_iface(cfg)
     #print _count_key_value_of_obj(cfg,'vswitch','name','vswitch2')
    print validate_config(cfg)
    for item in cfg:
        obj=item.keys()[0]
        if obj != 'vswitch':
            continue
        create_vswitch(item)
