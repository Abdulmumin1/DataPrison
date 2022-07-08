from manager import full_path
import os, json
#e8a202
colors = {
    'cover': '#101019',
    'primary': "#181825",
    'secondary': "#e8a202",
    "white": "#fff"
}

scroll_var = """QScrollBar::vertical{width:6px;}
        QScrollBar::handle:vertical{background:#181825; opacity:.3; min-height:0px;}
        QScrollBar::handle:vertical:active{background:#e8a202; border-radius:5px;}
        QScrollBar::add-line:vertical{height:0px; subcontrol-position:bottom;}
        QScrollBar::sub-line:vertical{height:0px; subcontrol-position:top;}
        """
scroll_hor = """QScrollBar::horizontal{height:6px;}
        QScrollBar::handle:horizontal{background:#181825; min-height:0px;}
        QScrollBar::handle:horizontal:active{background:#e8a202; border-radius:5px;}
        QScrollBar::add-line:horizontal{height:0px; subcontrol-position:bottom;}
        QScrollBar::sub-line:horizontal{height:0px; subcontrol-position:top;}
        """

class Handle():
    def __init__(self):

        self.global_function = {}
        self.config_file = os.path.join(full_path, 'config.json')
        self.delete_func_components()
        
    def delete_func_components(self):
        self.delete_queue = None
        self.full_delete = True
    def register_function(self, name, func):
        self.global_function[name] = func

    def get_function(self, name):
        return self.global_function.get(name)

    def update_entry(self, entry, value):
        if not os.path.exists(self.config_file):
            config_file = {}
        else:
            config_file = json.load(open(self.config_file))
        config_file[entry] = value
        json.dump(config_file, open(self.config_file, 'w'))       

    def get_config_entry(self, entry):
        if not os.path.exists(self.config_file):
            return [457, 632]
        config_file = json.load(open(self.config_file))
        value = config_file.get(entry)
        return value

    

handle = Handle()
