import os

from pyrap import session

import pyrap
from pyrap.layout import ColumnLayout, RowLayout, StackLayout
from pyrap.ptypes import Color, Pixels, Image
from pyrap.widgets import Shell, Label, Composite, Button


class MultiPage:
    '''My pyRAP application'''

    def __init__(self):
        self.visible = 0  # initialize variable that indicates which page is visible

    def main(self, **kwargs):
        self._shell = Shell(maximized=True, titlebar=False)
        self._shell.bg = Color('red')
        self._shell.on_resize += self._shell.dolayout

        comp_mainframe = Composite(self._shell.content)
        comp_mainframe.layout = RowLayout(halign='fill', valign='fill', flexrows=1, vspace=0)

        # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        # HEADER - we may not need this.. or maybe we do. You decide.
        # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        comp_header = Composite(comp_mainframe)
        comp_header.layout = ColumnLayout(halign='fill', valign='fill', equalwidths=True, padding=Pixels(0))
        comp_header.bg = Color('black')

        btn_switch1 = Button(comp_header, text='Back', halign='fill', valign='fill')
        btn_switch = Button(comp_header, text='Next', halign='fill', valign='fill')
        lbl_header = Label(comp_header, text='<b>Click button to switch pages!</b>', markup=True, halign='fill', valign='fill')
        lbl_header.bg = 'transp'
        lbl_header.color = Color('white')

        # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        # BODY - this is the 'main' composite that for the content. The visibility of the composites inside changes
        # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        self.comp_body = Composite(comp_mainframe, border=True)
        self.comp_body.layout = StackLayout(halign='fill', valign='fill')
        self.comp_body.bg = Color('white')

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # HOME PAGE #
        self.comp_home = Composite(self.comp_body)
        self.comp_home.layout = RowLayout(flexrows=0, halign='fill', valign='fill')
        #self.comp_home.bg = Color('blue')
        self.comp_home.bgimg = Image(os.path.join('..', 'controls', 'images', 'al2.jpg'))
        self.comp_home.visible = True
        lbl_wnd = Label(self.comp_home, text='Page 1 Google Search, also referred to as <br /> Google Web Search or simply Google, <br />'
                                   'is a web search engine developed by Google LLC. <br /> '
                                             'It is the most used search engine on the World Wide Web across all platforms, <br />'
                                             'with 92.74% market share as of October 2018,<br /> handling more than 3.5 billion searches each day.'
                                   'The order of search results returned by Google is based, <br /> '
                                             'in part, on a priority rank system called "PageRank". <br />'
                                             'Google Search also provides many different options for ', markup=True, halign='fill', orientation=RWT.HORIZONTAL)
        #lbl_wnd = Label(cmp_dialog, text='Blafasel <b> This is really important</b>', markup=True, valign='fill', halign='fill')
        lbl_wnd.bg = Color('red')
        btn_showdialog = Button(self.comp_home, text='Show Dialog', halign='fill', valign='fill')

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # ANOTHER PAGE #
        self.comp_second = Composite(self.comp_body)
        self.comp_second.layout = RowLayout(flexrows=0, halign='fill', valign='fill')
        self.comp_second.bg = Color('green')
        self.comp_second.visible = False
        Label(self.comp_second, text='<b>Page 2</b>', markup=True)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # THIRD PAGE #
        self.comp_third = Composite(self.comp_body)
        self.comp_third.layout = RowLayout(flexrows=0, halign='fill', valign='fill')
        self.comp_third.bg = Color('yellow')
        self.comp_third.visible = False
        Label(self.comp_third, text='<b>Page 3</b>', markup=True)



        def resize_bg (*_):

            w = session.runtime.display.width.value
            h = session.runtime.display.height.value
            self.comp_home.bgimg = self.comp_home.bgimg.resize(width= Pixels(w), height=Pixels(h))
            self.comp_second.bgimg = self.comp_second.bgimg.resize(width=Pixels(w), height=Pixels(h))
            self.comp_third.bgimg = self.comp_third.bgimg.resize(width=Pixels(w), height=Pixels(h))
            #self.comp_four.bgimg = self.comp_four.bgimg.resize(width=Pixels(w), height=Pixels(h))
            print(w,h)
            self._shell.dolayout()


        # LISTENER FUNCTION TO SWITCH PAGE VISIBILITY
        def open_menu(*_):
            self.visible = (
                                       self.visible + 1) % 4  # if you don't understand this, learn about the modulo operator (Euclidean division)

            # switch the three pages all around
            self.comp_home.visible = self.visible == 0
            self.comp_home.layer = (0 - self.visible) % 4
            self.comp_second.visible = self.visible == 1
            self.comp_second.layer = (1 - self.visible) % 4
            self.comp_third.visible = self.visible == 2
            self.comp_third.layer = (2 - self.visible) % 4
            #self.comp_four.visible = self.visible == 3
            #self.comp_four.layer = (3 - self.visible) % 4

        # LISTENER FUNCTION TO SWITCH PAGE VISIBILITY
        def back_menu(*_):
            self.visible = (
                                       self.visible - 1) % 4  # if you don't understand this, learn about the modulo operator (Euclidean division)

            # switch the three pages all around
            self.comp_home.visible = self.visible == 0
            self.comp_home.layer = (0 - self.visible) % 4
            self.comp_second.visible = self.visible == 1
            self.comp_second.layer = (1 - self.visible) % 4
            self.comp_third.visible = self.visible == 2
            self.comp_third.layer = (2 - self.visible) % 4
            #self.comp_four.visible = self.visible == 3
            #self.comp_four.layer = (3 - self.visible) % 4

        def showdialog(*_):
            # this will create a new dialog every time the button is clicked. You can also create it when setting
            # up the layout and set its visibility to false after calling wnd_dialog.show(), then set the visibility
            # to true in the listener function that is called when the button is clicked (will only work if the window
            # was hidden before. Closing the window will destroy the widget and an error will be thrown when trying
            # to make it visible again.
            wnd_dialog = Shell(parent=self._shell, titlebar=True, border=True, resize=False, modal=True,
                               halign='center', valign='center')
            wnd_dialog.create_content()
            wnd_dialog.content.bg = Color('white')

            w = session.runtime.display.width.value
            h = session.runtime.display.height.value
            wnd_dialog.bounds = w / 2 - 200, h / 2 - 150, 400, 300

            cmp_dialog = Composite(wnd_dialog.content)
            cmp_dialog.layout = RowLayout(valign='fill', halign='fill', flexrows=0)

            lbl_wnd = Label(cmp_dialog, text='Blafasel <b> This is really important</b>', markup=True, valign='fill', halign='fill')
            lbl_wnd.bg = Color('red')

            def dosomething(*_):
                lbl_wnd.text = '<b>I did something!</b>'

            btn_dosomething = Button(cmp_dialog, text='Do something', valign='fill', halign='fill')
            btn_dosomething.on_select += dosomething

            wnd_dialog.show()

        # assign listener function to button click
        btn_switch.on_select += open_menu
        btn_switch1.on_select += back_menu
        btn_showdialog.on_select += showdialog

        self._shell.show()


def main():
    pyrap.register(clazz=MultiPage,
                   entrypoints={'start': MultiPage.main},
                   path='kidsApp',
                   name='Space Station for kids!')
    pyrap.run()


if __name__ == '__main__':
    main()
