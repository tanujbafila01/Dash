import dash
import dash_core_components as dcc
import dash_html_components as html

#Start the application

app = dash.Dash()

# HTML of project
# The contents of html are rerefed as children, they can either be a single element of a list. 
# html.H1 applies header 1 to the text.
# Graph comes from dash core component
# Figure is a typical plotly graph.
# Data consits of either single dictionary or a list of dictionaries.
app.layout = html.Div(children=
	[html.H1('Dash tutorial'),
	dcc.Graph(id='example',
		figure={
			'data':[
				{'x':[1,2,3,4,5],'y':[5,6,7,2,1],'type':'line','name':'boats'},
				{'x':[1,2,3,4,5],'y':[8,3,2,3,5],'type':'bar','name':'cars'},
				],
			'layout':{
				'title':'Basic Dash Example'
				}
			})
	])



if __name__=='__main__':
	app.run_server(debug=True)
