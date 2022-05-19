def doc_creator():
    print('<!DOCTYPE html>')
    
def html_open_tag():
    print('<html>')

def html_close_tag():
    print('</html>')

def body_open_tag():
    print('<body>')

def body_close_tag():
    print('</body>')
    
def head_open_tag():
    print('<head>')

def head_close_tag():
    print('</head>')

def script_open_tag_with_source(source):
    print(f'<script src="{source}">')

def script_open_tag():
    print('<script>')

def script_close_tag():
    print('</script>')
    
def div_open_tag(className="",id=""):
    print(f'<div class="{className}" id="{id}">')

def div_close_tag():
    print('</div>')

def table_open_tag(border):
    print(f'<table border="{border}">')

def table_close_tag():
    print('</table>')
    
def td_open_tag():
    print('<td>')

def td_close_tag():
    print('</td>')
    
def tr_open_tag():
    print('<tr>')

def tr_close_tag():
    print('</tr>')
    
def input_tag(type,name="",className="",id="",value=""):
    print(f'<input type="{type}" name="{name}" class="{className}" id="{id}" value={value}>')

def link(rel,path):
    print(f'<link rel="{rel}" href="{path}" />')

def title(title):
    print(f'<title>{title}</title>')

def form_open_tag(action="",method=""):
    print(f'<form action="{action} method="{method}">')

def form_close_tag():
    print(f'</form>')
    
def a_href_opne(path,name,className):
    print(f'<a href="{path}" class="{className}">{name}</a>')

def center_tag(element):
    print(f'<center>{element}</center>')     











