class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html() method not implemented for HTMLNode")
    
    def props_to_html(self):
        html_str = ""
        if self.props:
            for key, value in self.props.items():
                html_str =  html_str + f' {key}="{value}"'
        return html_str
    
    def __repr__(self):
        print(f"Tag: {self.tag}")
        print(f"Value: {self.value}")
        print(f"Children: {self.children}")
        print(f"Props: {self.props}")