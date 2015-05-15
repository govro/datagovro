import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import airbrake

# Setup logger
# TODO @palcu: remove these once the project goes public
logger = airbrake.getLogger(api_key='d6652cdfa031e900485e34539212531d', project_id=111438)


class Romania_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'romania_theme')
