# Source Generated with Decompyle++
# File: Label.pyo (Python 2.0)

from ShowBaseGlobal import *
from DirectObject import *
from GuiGlobals import *
ButtonUp = 1
ButtonUpGui = 2
ButtonLit = 3
ButtonDown = 4
ButtonInactive = 5
Sign = 6
SignBlack = 7
ScrollTitle = 8
ScrollItem = 9

def textLabel(string, style, scale = 0.1, width = None, drawOrder = getDefaultDrawOrder(), font = getDefaultFont(), mayChange = 0):
    (label, text) = textLabelAndText(string, style, scale, width, drawOrder, font, mayChange)
    return label


def textLabelAndText(string, style, scale = 0.1, width = None, drawOrder = getDefaultDrawOrder(), font = getDefaultFont(), mayChange = 0):
    text = TextNode()
    text.freeze()
    text.setFont(font)
    text.setAlign(TMALIGNCENTER)
    text.setDrawOrder(drawOrder)
    text.setTextColor(0.0, 0.0, 0.0, 1.0)
    text.setCardColor(1.0, 1.0, 1.0, 1.0)
    text.setCardAsMargin(0.1, 0.1, 0.0, 0.0)
    text.setTransform(Mat4.scaleMat(scale))
    if isinstance(style, types.TupleType) or isinstance(style, VBase4):
        text.setCardColor(style[0], style[1], style[2], style[3])
    elif style == ButtonUp:
        pass
    elif style == ButtonUpGui:
        text.setCardColor(0.25, 0.7, 0.85, 1.0)
    elif style == ButtonLit:
        text.setCardColor(1.0, 1.0, 0.0, 1.0)
    elif style == ButtonDown:
        text.setTextColor(1.0, 1.0, 1.0, 1.0)
        text.setCardColor(0.0, 0.0, 0.0, 1.0)
    elif style == ButtonInactive:
        text.setTextColor(0.4, 0.4, 0.4, 1.0)
        text.setCardColor(0.9, 0.9, 0.9, 1.0)
    elif style == Sign:
        text.setTextColor(1.0, 0.0, 0.0, 1.0)
        text.clearCard()
    elif style == SignBlack:
        text.setTextColor(0.0, 0.0, 0.0, 1.0)
        text.clearCard()
    elif style == ScrollTitle:
        text.setTextColor(1.0, 0.0, 0.0, 1.0)
        text.setCardColor(1.0, 1.0, 1.0, 0.0)
    elif style == ScrollItem:
        pass
    else:
        raise ValueError
    text.setText(string)
    v = text.getCardActual()
    if width != None:
        v = VBase4(-width / 2.0, width / 2.0, v[2], v[3])
        if text.hasCard():
            text.setCardActual(v[0], v[1], v[2], v[3])
        
    
    if mayChange:
        text.thaw()
    else:
        node = text.generate()
        text = node
    label = GuiLabel.makeModelLabel(text, v[0] * scale, v[1] * scale, v[2] * scale, v[3] * scale)
    label.setDrawOrder(drawOrder)
    return (label, text)


def modelLabel(model, geomRect = None, style = None, scale = (0.1, 0.1), drawOrder = getDefaultDrawOrder()):
    topnode = NamedNode('model')
    topnp = NodePath(topnode)
    mi = model.instanceTo(topnp)
    mi.setScale(scale[0], scale[0], scale[1])
    mi.setBin('fixed', drawOrder)
    if style != None:
        color = None
        if isinstance(style, types.TupleType) or isinstance(style, VBase4):
            color = style
        elif style == ButtonInactive:
            color = (0.5, 0.5, 0.5, 1.0)
        
        if color != None:
            mi.setColor(color[0], color[1], color[2], color[3])
            if color[3] != 1.0:
                mi.setTransparency(1)
            
        
    
    if geomRect == None:
        geomRect = (1, 1)
    
    if len(geomRect) == 2:
        label = GuiLabel.makeModelLabel(topnode, geomRect[0] * scale[0], geomRect[1] * scale[1])
    elif len(geomRect) == 4:
        label = GuiLabel.makeModelLabel(topnode, geomRect[0] * scale[0], geomRect[1] * scale[0], geomRect[2] * scale[1], geomRect[3] * scale[1])
    else:
        raise ValueError
    label.setDrawOrder(drawOrder)
    return label

