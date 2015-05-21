import ckan.model as model
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import airbrake

# Setup logger
# TODO @palcu: remove these once the project goes public
logger = airbrake.getLogger(api_key='d6652cdfa031e900485e34539212531d', project_id=111438)

def get_number_of_files():
    return model.Session.execute("select count(*) from resource where state = 'active'").first()[0]

def get_number_of_external_links():
    return model.Session.execute("select count(*) from resource where state = 'active' and url not LIKE '%data.gov.ro%'").first()[0]

class Romania_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'romania_theme')

    def get_helpers(self):
        return {'get_number_of_files': get_number_of_files,
                'get_number_of_external_links': get_number_of_external_links}
