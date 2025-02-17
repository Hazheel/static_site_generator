class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        for k, v in self.props.items():
            result += f" {k}={v} "
        return result

    def __repr__(self):
        result = ""
        if self.value is not None:
            result += self.value + "\n"
        if self.tag is not None:
            result += self.tag + "\n"
        if self.children is not None:
            for child in self.children:
                result += f" {child}"
            result += "\n"
        if self.props is not None:
            result += self.props_to_html()
        return result