import os

class config_parser():
    def __init__(self, cfgdict):
        for k in cfgdict.keys():
            setattr(self, k, cfgdict[k])

    def get(self, key, default=None):
        try:
            r = eval("self.%s" % key)
            return r
        except:
            return default

def load_config():
    base_test_folder = os.getcwd()
    config_file_path = os.path.join(base_test_folder, "config", "config.py")
    cfgdata = file(config_file_path, "U").read()

    conf_dict = {}
    exec cfgdata in conf_dict
    config = config_parser(conf_dict)
    return config

qaconfig = load_config()
print qaconfig.abc