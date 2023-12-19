| Widgets         | Description |
|-----------------|-----------------------------|
| Label           | It is used to display text or image on the screen |
| Button          | It is used to add buttons to your application |
| Canvas          | It is used to draw pictures and others layouts like texts, graphics etc. |
| ComboBox	      | It contains a down arrow to select from list of available options |
| CheckButton	  | It displays a number of options to the user as toggle buttons from which user can  |select any number of options.
| RadioButton     | It is used to implement one-of-many selection as it allows only one option to be  |selected
| Entry           | It is used to input single line text entry from user |
| Frame           | It is used as container to hold and organize the widgets |
| Message	        | It works same as that of label and refers to multi-line and non-editable text |
| Scale           | It is used to provide a graphical slider which allows to select any value from that  |scale
| Scrollbar       | It is used to scroll down the contents. It provides a slide controller. |
| SpinBox         | It is allows user to select from given set of values |
| Text	        | It allows user to edit multiline text and format the way it has to be displayed |
| Menu            | It is used to create all kinds of menu used by an application |


# Geometry Management
Creating a new widget doesn’t mean that it will appear on the screen. To display it, we need to call a special method: either grid, pack(example above), or place. 

|Method |	Description|
|-------|--------------|
|pack() |	The Pack geometry manager packs widgets in rows or columns.|
|grid() |	The Grid geometry manager puts the widgets in a 2-dimensional table. <br>The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget. |
|place()|	The Place geometry manager is the simplest of the three general geometry managers provided in Tkinter. <br> It allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window.|

# Widgets
Tkinter provides various controls, such as buttons, labels and text boxes used in a GUI application. These controls are commonly called Widgets.  The list of commonly used Widgets are mentioned below –

|S No. |	Widget	| Description |
|-------|---------|---------------|
|1	|Label	|The Label widget is used to provide a single-line caption for other widgets. It can also contain images.|
|2	|Button	|The Button widget is used to display buttons in your application.|
|3	|Entry	|The Entry widget is used to display a single-line text field for accepting values from a user.|
|4	|Menu	|The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.|
|5	|Canvas	|The Canvas widget is used to draw shapes, such as lines, ovals, polygons and rectangles, in your application.|
|6	|Checkbutton	|The Checkbutton widget is used to display a number of options as checkboxes. The user can select multiple options at a time.|
|7	|Frame	|The Frame widget is used as a container widget to organize other widgets.|
|8	|Listbox	|The Listbox widget is used to provide a list of options to a user.|
|9	|Menubutton	|The Menubutton widget is used to display menus in your application.|
|10	|Message	|The Message widget is used to display multiline text fields for accepting values from a  user. |
|11	|Radiobutton	|The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one option at a time. |
|12	|Scale	|The Scale widget is used to provide a slider widget.|
|13	|Scrollbar	|The Scrollbar widget is used to add scrolling capability to various widgets, such as  list boxes.|
|14	|Text	|The Text widget is used to display text in multiple lines.|
|15	|Toplevel	|The Toplevel widget is used to provide a separate window container.|
|16	|LabelFrame	|A labelframe is a simple container widget. Its primary purpose is to act as a spacer or container for complex window layouts.|
|17	|tkMessageBox	|This module is used to display message boxes in your applications.|
|18	|Spinbox	|The Spinbox widget is a variant of the standard Tkinter Entry widget, which can be used to select from a fixed number of values.|
|19	|PanedWindow	|A PanedWindow is a container widget that may contain any number of panes, arranged horizontally or vertically.|