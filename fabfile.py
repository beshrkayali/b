from fabric.api import *


def prod():
    env.hosts = ['user@ip.ip.ip.ip']
    env.directory = '/'  # the directory of the virtualenv that contains your site on your server
    env.activate = 'source ../bin/activate'


def virtualenv(command):
    with cd(env.directory):
        run(env.activate + '&&' + command)


def push_content():
    local('git add content/.')
    local('git commit -m "Updated content"')
    local('git push origin master')


def push_all():
    local('git add .')
    local('git commit -m "Pushing all updates"')
    local('git push origin master')


def pull():
    with cd(env.directory):
        run('git pull')


def pushpull_content():
    push_content()
    pull()


def pushpull():
    push_all()
    pull()


def generate():
    with cd(env.directory):
        virtualenv('hyde.py -g -s .')


def pushpullgenerate():
    pushpull()
    generate()


def clean():
    with cd(env.directory):
        run('rm -rf ./deploy')


def pushpullcleangenerate():
    pushpull()
    clean()
    generate()
