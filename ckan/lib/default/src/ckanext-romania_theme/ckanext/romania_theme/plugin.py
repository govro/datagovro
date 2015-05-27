import ckan.model as model
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import airbrake

# Setup error logger
if os.getenv('AIRBRAKE_API_KEY'):
    logger = airbrake.getLogger(api_key=os.getenv('AIRBRAKE_API_KEY'),
                                project_id=os.getenv('AIRBRAKE_PROJECT_ID'))

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
