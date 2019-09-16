#imports


#vars
appname = "appname"


#module specific functions (user functions)


#required plugin functions
def send(data):
    #send logic


def listen():
    app_exfiltrate.log_message(
        'info', "[{1}] Some interesting message {0}".format(config['key'],appname))
    #listen logic


class Plugin:
    def __init__(self, app, conf):
        global app_exfiltrate, config
        config = conf
        app.register_plugin(appname, {'send': send, 'listen': listen})
        app_exfiltrate = app
