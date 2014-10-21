# -*- coding: utf-8 -*-

from fabric.api import run, cd, env, local

env.hosts = ['python@androidgreetings.ru']
project_path = '/home/python/androidgreetings'


def push_deploy():
    local('git push')
    deploy()


def deploy():	
	with cd(project_path):
		run('git pull')
		run('sudo supervisorctl restart androidgreetings')
