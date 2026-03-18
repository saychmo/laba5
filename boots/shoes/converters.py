class FourDigitYearConverter:
    regex = "[0-9]{4}"
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return "%04d" % value

class ShoeSizeConverter:
    regex = '3[5-9]|4[0-7]'  # 35-39 или 40-47
    
    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)