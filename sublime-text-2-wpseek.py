# written by Oliver Schlöbe (www.schloebe.de)
# based on Stackoverflow Search Plugin by Eric Martel (emartel@gmail.com / www.ericmartel.com)

# available commands
#   wpseek_com_open_selection
#   wpseek_com_search_selection
#   wpseek_com_search_from_input

import sublime, sublime_plugin, subprocess, webbrowser

def SearchWPSFor(text):
    url = 'http://wpseek.com/' + text.replace(' ','%20') + '/'
    webbrowser.open_new_tab(url)

def OpenWPSFunctionReference(text):
    url = 'http://wpseek.com/' + text.replace(' ','%20') + '/'
    webbrowser.open_new_tab(url)

class WPSeekComOpenSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            OpenWPSFunctionReference(text)

class WPSeekComSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)            
            SearchWPSFor(text)

class WPSeekComSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search wpseek.com for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchWPSFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass