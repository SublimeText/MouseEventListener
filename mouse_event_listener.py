import sublime, sublime_plugin

class DragSelectCallbackCommand(sublime_plugin.TextCommand):
	def run_(self, edit, args):
		for c in sublime_plugin.all_callbacks.setdefault('on_pre_mouse_down',[]):
			c.on_pre_mouse_down(args)
		
		#We have to make a copy of the selection, otherwise we'll just have
		#a *reference* to the selection which is useless if we're trying to
		#roll back to a previous one. A RegionSet doesn't support slicing so
		#we have a comprehension instead.
		old_sel = [r for r in self.view.sel()]
		
		#Only send the event so we don't do an extend or subtract or
		#whatever. We want the only selection to be where they clicked.
		self.view.run_command("drag_select", {'event': args['event']})
		new_sel = self.view.sel()
		click_point = new_sel[0].a
		
		#Restore the old selection so when we call drag_select it will
		#behave normally.
		new_sel.clear()
		for r in old_sel:
			new_sel.add(r)
		
		#This is the "real" drag_select that alters the selection for real.
		self.view.run_command("drag_select", args)
		
		#Expose click-event-arguments to on_post_mouse_down
		for c in sublime_plugin.all_callbacks.setdefault('on_post_mouse_down',[]):
			c.on_post_mouse_down(args, click_point)

class MouseEventListener(sublime_plugin.EventListener):
	#If we add the callback names to the list of all callbacks, Sublime
	#Text will automatically search for them in future imported classes.
	#You don't actually *need* to inherit from MouseEventListener, but
	#doing so forces you to import this file and therefore forces Sublime
	#to add these to its callback list.
	sublime_plugin.all_callbacks.setdefault('on_pre_mouse_down', [])
	sublime_plugin.all_callbacks.setdefault('on_post_mouse_down', [])

"""
class MouseEventProcessor(MouseEventListener):
	def on_pre_mouse_down(self, args):
		print "on pre-click!", args
	def on_post_mouse_down(self, point):
		print "on post-click!", point
"""
