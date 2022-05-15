from js import console
from div import Div
import uuid
parentId = str('hello')
childId = str('world')

# TODO
parent = Element(parentId)
child = Element(childId)
# console.log(parent, child)
def addNumber(*args):
    number = child.element.innerText
    number = int(number) + 1
    child.element.innerText = str(number)

print(Div(id=parentId, className="container", children=[
            'addTest', Div(id=childId, children=['1'])]))

parent.element.onclick = addNumber