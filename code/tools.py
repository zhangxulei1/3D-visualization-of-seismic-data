class Colorbar:
    # 色棒标题, 色棒的摆放:竖or横, 色棒中显示几个数, 色棒中的数值的格式, 色棒中小色块的数量：通常不用这个参数
    def __init__(self, title=None, orientation=None, nb_labels=None, label_fmt=None, nb_colors=None):
        self.title = title
        self.orientation = orientation
        self.nb_labels = nb_labels
        self.label_fmt = label_fmt
        self.nb_colors = nb_colors

    # 默认的色棒是竖着的
    def init_vertical(self):
        self.title = 'value\n'
        self.orientation = 'vertical'
        self.nb_labels = 5
        self.label_fmt = '%-.0f'  # 默认没有小数



class Font:
    # 字体类型, 字体标题的大小, 字体文本的大小
    def __init__(self, font_family=None, font_title_size=None, font_label_size=None):
        self.font_family = font_family
        self.font_title_size = font_title_size
        self.font_label_size = font_label_size

    # 默认状态下
    def init_none(self):
        self.font_family = 'times'
        self.font_title_size = 30
        self.font_label_size = 25
