import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Romania_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'romania_theme')
