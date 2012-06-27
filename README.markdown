MouseEventListener
======

MouseEventListener adds two new callbacks to Sublime Text 2's plugin API:

* `on_pre_click({'event': {'x': screen_x, 'y': screen_y, 'button': button}})`
* `on_post_click(text_point)`

An important thing to note is that the selection is modified not once but twice in between `on_pre_mouse_down` and `on_post_mouse_down`—this is done to determine the `text_point` of the click, as Sublime Text 2 has no API to translate a screen x and y into a `text_point` other than by calling `drag_select` and seeing where the selection ends up.

A second important thing to note is that mouse-up currently cannot be captured using Sublime Text 2's API. Hopefully this will be added in the future. However, this means that drags cannot be detected! other than perhaps by carefully monitoring the selection as it changes and just guessing. Additionally, `on_selection_modified` fires on mouse up in most cases.

Install
-------

This plugin is available through Package Control, which is available here:

    http://wbond.net/sublime_packages/package_control

As far as I know, Package Control does not handle dependencies, so if you depend on this package you may have to mention installing it in your install instructions.
