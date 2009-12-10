from pyLaTeX.HTML import lib
from pyLaTeX.HTML.lib import MacroManager
from pyLaTeX.HTML import *

__config__ = MacroManager.config

MacroManager.newif('ifhtml', initial=1)

class note(Command):
    args = 'data'
    def output(self):
        return '<b>Note:</b><blockquote>%s</blockquote>' % (self)

class centering(Command):
    args = 'data'
    def output(self):
        return '<center>\n%s</center>' %(self)

class vert(Command):
    def output(self):
        return '|'

class text(Command):
    args = 'data'
    def output(self):
        return '%s' %(self)

class abs(Command):
    def output(self):
        return 'abs'

class ulink(Command):
    args = 'label url'
    def output(self):
        return '<a href="%s">%s</a>' %(self.url, self.label)

class sub(Command):
    def output(self):
        return '&gt;'

class menuselection(Command):
    args = 'data'
    def output(self):
        return '<b>%s</b>' %(self)

class mailto(Command):
    args = 'mailaddr'
    def output(self):
        return '<mailto>%s</mailto>' %(self)

class ahrefurl(Command):
    args = 'url'
    def output(self):
        return '<a href="%s">%s</a>' %(self, self)

class url(Command):
    args = 'data'
    def output(self):
        return '%s' %(self)
    
class imgsrc(Command):
    args = '[ sizestr ] url'
    def output(self):
        options = []
        if self.sizestr:
            import re
            instr = '%s' %(self.sizestr)
            for k, v in re.findall(r'([a-z]*)=([a-zA-Z0-9]*)', instr):
                options.append('%s="%s"' %(k, v))
        return '<img src="%s" %s />' %(self.url, ' '.join(options))

class latexonly(Environment):
    def output(self):
        return ''
    
class htmlonly(Environment):
    def output(self):
        return '%s' %(self)
    
    
