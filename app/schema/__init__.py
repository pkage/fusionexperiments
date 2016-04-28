import datasource, experiment, library, user

def register_models(connection):
	connection.register([datasource.DataSource, user.User, experiment.Experiment, library.Library]);
